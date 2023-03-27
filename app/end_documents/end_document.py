from flask import request
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.models.models import EndDocumentModel, DocumentEmployeeModel, OldDocumentEmployeeModel
from app.helpers.helper import Helper
from app.vacations.vacation import Vacation
from app import db
from datetime import datetime

class EndDocument():
    @staticmethod
    def get(rut):
        status_id = Helper.is_active(rut)

        if status_id == 1:
            end_documents = EndDocumentModel.query\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(DocumentEmployeeModel.status_id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.number_holidays, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .all()
        else:
            end_documents = EndDocumentModel.query\
                .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(OldDocumentEmployeeModel.status_id, EndDocumentModel.id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.number_holidays, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .all()

        return end_documents

    @staticmethod
    def get_by_id(id):
        end_documents = EndDocumentModel.query\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(DocumentEmployeeModel.status_id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.number_holidays, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.id==id)\
                .first()

        return end_documents

    @staticmethod
    def get_by_rut(rut):
        status_id = Helper.is_active(rut)

        if status_id == 1:
            end_documents = EndDocumentModel.query\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(DocumentEmployeeModel.status_id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.number_holidays, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .first()
        else:
            end_documents = EndDocumentModel.query\
                .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == EndDocumentModel.document_employee_id)\
                .add_columns(OldDocumentEmployeeModel.status_id, EndDocumentModel.id, EndDocumentModel.added_date, EndDocumentModel.document_employee_id, EndDocumentModel.causal_id, EndDocumentModel.rut, EndDocumentModel.number_holidays, EndDocumentModel.voluntary_indemnity, EndDocumentModel.indemnity_years_service, EndDocumentModel.fertility_proportional, EndDocumentModel.substitute_compensation, EndDocumentModel.total)\
                .filter(EndDocumentModel.rut==rut)\
                .first()

        return end_documents

    @staticmethod
    def substitute_compensation(rut):
        employee_labor_datum = EmployeeLaborDatum.get(rut)

        gratification = Helper.gratification(employee_labor_datum.salary)

        result = int(employee_labor_datum.salary) + int(employee_labor_datum.collation) + int(employee_labor_datum.locomotion) + int(gratification)

        return result

    @staticmethod
    def indemnity_years_service(rut, exit_company):
        employee_labor_datum = EmployeeLaborDatum.get(rut)

        gratification = Helper.gratification(employee_labor_datum.salary)
        years = Helper.get_end_document_total_years(employee_labor_datum.entrance_company, exit_company)
        result = (int(employee_labor_datum.salary) + int(employee_labor_datum.collation) + int(employee_labor_datum.locomotion) + int(gratification)) * int(years)

        return result

    @staticmethod
    def fertility_proportional(rut, exit_company, number_holidays):
        employee_labor_datum = EmployeeLaborDatum.get(rut)
        legal = Vacation.legal(rut)
        taken_days = Vacation.taken_days(rut)
        balance = Vacation.balance(legal, taken_days)
        start_date = exit_company
        end_date = Helper.calculate_end_document_end_date(start_date, balance)
        end_date_split = Helper.split(str(end_date), " ")
        weekends_between_dates = Helper.weekends_between_dates(start_date, end_date_split[0])
        total = int(balance) + int(weekends_between_dates) - int(number_holidays)
        vacation_day_value = Helper.vacation_day_value(employee_labor_datum.salary)

        result = int(vacation_day_value) * int(total)

        if result < 0:
            result = 0
            
        return result

    @staticmethod
    def store(id, data):
        end_document = EndDocumentModel()
        end_document.document_employee_id = id
        end_document.causal_id = data['causal_id']
        end_document.rut = data['rut']
        end_document.number_holidays = data['number_holidays']
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