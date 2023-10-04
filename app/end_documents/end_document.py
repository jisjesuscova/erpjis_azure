from flask import request
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.models.models import EndDocumentModel, DocumentEmployeeModel, OldDocumentEmployeeModel
from app.helpers.helper import Helper
from app.vacations.vacation import Vacation
from app import db
from datetime import datetime
from app.hr_settings.hr_setting import HrSetting

class EndDocument():
    @staticmethod
    def get(rut):
        status_id = Helper.is_active(rut)

        if status_id == 1:
            end_documents = EndDocumentModel.query\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(DocumentEmployeeModel.status_id, EndDocumentModel.id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.fertility_proportional_days, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .all()
        else:
            end_documents = EndDocumentModel.query\
                .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(OldDocumentEmployeeModel.status_id, EndDocumentModel.id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.fertility_proportional_days, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .all()

        return end_documents

    @staticmethod
    def get_by_id(id):
        end_documents = EndDocumentModel.query\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(EndDocumentModel.id, DocumentEmployeeModel.status_id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.fertility_proportional_days, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.id==id)\
                .first()

        return end_documents

    @staticmethod
    def get_by_rut(rut):
        status_id = Helper.is_active(rut)

        if status_id == 1:
            end_documents = EndDocumentModel.query\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(EndDocumentModel.id, DocumentEmployeeModel.status_id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.fertility_proportional_days, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .first()
        else:
            end_documents = EndDocumentModel.query\
                .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(EndDocumentModel.id, OldDocumentEmployeeModel.status_id, EndDocumentModel.id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.fertility_proportional_days, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .first()

        return end_documents

    @staticmethod
    def substitute_compensation(rut):
        hr_settings = HrSetting.get()

        employee_labor_datum = EmployeeLaborDatum.get(rut)

        gratification = Helper.gratification(employee_labor_datum.salary)

        if gratification > hr_settings.top_gratification:
            gratification = hr_settings.top_gratification

        result = int(employee_labor_datum.salary) + int(employee_labor_datum.collation) + int(employee_labor_datum.locomotion) + int(gratification)

        return result

    @staticmethod
    def indemnity_years_service(rut, exit_company):
        hr_settings = HrSetting.get()

        employee_labor_datum = EmployeeLaborDatum.get(rut)

        gratification = Helper.gratification(employee_labor_datum.salary)

        if gratification > hr_settings.top_gratification:
            gratification = hr_settings.top_gratification

        years = Helper.get_end_document_total_years(employee_labor_datum.entrance_company, exit_company)
        if years > 11:
            years = 11

        result = (int(employee_labor_datum.salary) + int(employee_labor_datum.collation) + int(employee_labor_datum.locomotion) + int(gratification)) * int(years)

        return result

    @staticmethod
    def fertility_proportional(rut, exit_company, balance, number_holidays):
        employee_labor_datum = EmployeeLaborDatum.get(rut)
        start_date = exit_company
        end_date = Helper.add_business_days(start_date, balance, number_holidays)
        end_date_split = Helper.split(str(end_date), " ")
        weekends_between_dates = Helper.count_weekends(start_date, end_date_split[0])
        total = int(balance) + int(weekends_between_dates) + int(number_holidays)
        vacation_day_value = Helper.vacation_day_value(employee_labor_datum.salary)

        result = int(vacation_day_value) * int(total)

        if result < 0:
            result = 0
            
        return result
    
    @staticmethod
    def total_vacations(rut, exit_company, balance, number_holidays):
        start_date = exit_company
        end_date = Helper.add_business_days(start_date, balance, number_holidays)
        end_date_split = Helper.split(str(end_date), " ")
        weekends_between_dates = Helper.count_weekends(start_date, end_date_split[0])
        total = int(balance) + int(weekends_between_dates) + int(number_holidays)
        result = int(total)

        if result < 0:
            result = 0
            
        return result

    @staticmethod
    def store(id, data):
        end_document = EndDocumentModel()
        end_document.document_employee_id = id
        end_document.causal_id = data['causal_id']
        end_document.rut = data['rut']
        end_document.fertility_proportional_days = data['fertility_proportional_days']
        end_document.voluntary_indemnity = Helper.remove_from_string(".", data['voluntary_indemnity'])
        end_document.indemnity_years_service = Helper.remove_from_string(".", data['indemnity_years_service'])
        end_document.substitute_compensation = Helper.remove_from_string(".", data['substitute_compensation'])
        end_document.fertility_proportional = Helper.remove_from_string(".", data['fertility_proportional'])
        end_document.total = Helper.remove_from_string(".", data['total'])
        end_document.added_date = datetime.now()
        end_document.updated_date = datetime.now()

        db.session.add(end_document)
        db.session.commit()
        
        return end_document.id

    @staticmethod
    def update(old_id, new_id):
        end_document_qty = EndDocumentModel.query.filter_by(document_employee_id=old_id).count()

        if end_document_qty > 0:
            end_document = EndDocumentModel.query.filter_by(document_employee_id=old_id).first()
            end_document.document_employee_id = new_id

            db.session.add(end_document)
            db.session.commit()
            
            return end_document.id

    @staticmethod
    def delete(id):
        end_document_qty = EndDocumentModel.query.filter_by(id=id).count()

        if end_document_qty > 0:
            end_document = EndDocumentModel.query.filter_by(id=id).first()

            db.session.delete(end_document)
            try:
                db.session.commit()

                return end_document
            except Exception as e:
                return {'msg': 'Data could not be stored'}

    @staticmethod
    def upload(id, file):
        old_document_employee = OldDocumentEmployeeModel.query.filter_by(id=id).first()
        old_document_employee.support = file
        old_document_employee.status_id = 4
        old_document_employee.updated_date = datetime.now()

        db.session.add(old_document_employee)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0