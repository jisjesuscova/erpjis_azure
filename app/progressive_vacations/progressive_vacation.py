from app.models.models import EmployeeLaborDatumModel, ProgressiveVacationModel, DocumentEmployeeModel
from app.helpers.helper import Helper
from datetime import datetime, date
from app import db
from sqlalchemy import func
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum

class ProgressiveVacation():
    @staticmethod
    def get(rut = '', id = '', status_id = []):
        if rut != '':
            if len(status_id) > 0:
                vacations = ProgressiveVacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == ProgressiveVacationModel.document_employee_id)\
                    .add_columns(ProgressiveVacationModel.no_valid_days, ProgressiveVacationModel.document_employee_id, ProgressiveVacationModel.id, ProgressiveVacationModel.rut, ProgressiveVacationModel.since, ProgressiveVacationModel.until, ProgressiveVacationModel.days, DocumentEmployeeModel.status_id, ProgressiveVacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==36, DocumentEmployeeModel.status_id.in_(status_id)).order_by(db.desc(DocumentEmployeeModel.added_date))
            else:
                vacations = ProgressiveVacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == ProgressiveVacationModel.document_employee_id)\
                    .add_columns(ProgressiveVacationModel.no_valid_days, ProgressiveVacationModel.document_employee_id, ProgressiveVacationModel.id, ProgressiveVacationModel.rut, ProgressiveVacationModel.since, ProgressiveVacationModel.until, ProgressiveVacationModel.days, ProgressiveVacationModel.no_valid_days, ProgressiveVacationModel.added_date, ProgressiveVacationModel.updated_date, ProgressiveVacationModel.support, DocumentEmployeeModel.status_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==36).order_by(db.desc(DocumentEmployeeModel.added_date))

            return vacations
        else:
            vacation = ProgressiveVacationModel.query.filter_by(id=id).first()

            return vacation

    @staticmethod
    def get_by_major(rut = '', id = '', status_id = '', limit = ''):
        if limit == '':
            if rut != '':
                vacations = ProgressiveVacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == ProgressiveVacationModel.document_employee_id)\
                        .add_columns(ProgressiveVacationModel.no_valid_days, ProgressiveVacationModel.document_employee_idProgressiveVacationModel.document_employee_id, ProgressiveVacationModel.id, ProgressiveVacationModel.rut, ProgressiveVacationModel.since, ProgressiveVacationModel.until, ProgressiveVacationModel.days, DocumentEmployeeModel.status_id, ProgressiveVacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==36, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(DocumentEmployeeModel.added_date))

                return vacations
            else:
                vacation = ProgressiveVacationModel.query.filter_by(id=id).first()

                return vacation
        else:
            vacations = ProgressiveVacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == ProgressiveVacationModel.document_employee_id)\
                        .add_columns(ProgressiveVacationModel.no_valid_days, ProgressiveVacationModel.document_employee_id, ProgressiveVacationModel.id, ProgressiveVacationModel.rut, ProgressiveVacationModel.since, ProgressiveVacationModel.until, ProgressiveVacationModel.days, DocumentEmployeeModel.status_id, ProgressiveVacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==36, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(DocumentEmployeeModel.added_date)).limit(limit)

            return vacations

    @staticmethod
    def get_total(rut = '', status_id = ''):
        vacation_count = ProgressiveVacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == ProgressiveVacationModel.document_employee_id)\
                        .add_columns(ProgressiveVacationModel.document_employee_id, ProgressiveVacationModel.id, ProgressiveVacationModel.rut, ProgressiveVacationModel.since, ProgressiveVacationModel.until, ProgressiveVacationModel.days, DocumentEmployeeModel.status_id, ProgressiveVacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==36, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(DocumentEmployeeModel.added_date))

        count = vacation_count.count()

        if count > 1:
            vacations = ProgressiveVacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == ProgressiveVacationModel.document_employee_id)\
                    .add_columns(ProgressiveVacationModel.rut, func.sum(ProgressiveVacationModel.days).label('total_days'))\
                    .filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==36, DocumentEmployeeModel.status_id > status_id)\
                    .group_by(ProgressiveVacationModel.rut)\
                    .order_by(db.desc(DocumentEmployeeModel.added_date)).limit(1)

            return vacations
        else:
            return count


    @staticmethod
    def legal(rut):
        employee_labor_data = EmployeeLaborDatum.get(rut)
        employee_extra_data = EmployeeExtraDatum.get(rut)

        if employee_extra_data != None:
            entrance_company_months = Helper.months(employee_labor_data.entrance_company, date.today())
            years = Helper.months_to_years(entrance_company_months)
            if employee_extra_data.recognized_years != None:
                total_years =  int(years) + int(employee_extra_data.recognized_years)
            else: 
                total_years = years

            progressive_vacation_days = Helper.progressive_vacation_days(total_years, employee_extra_data.progressive_vacation_level_id)

            return progressive_vacation_days
        else:
            return 0

    @staticmethod
    def taken_days(rut):
        taken_days = Helper.get_taken_progressive_days(rut)

        return taken_days

    @staticmethod
    def balance(legal, taken_days):
        return legal - taken_days
    
    @staticmethod
    def store(data, document_employee_id):
        days = Helper.days(data['since'], data['until'], data['no_valid_days'])

        progressive_vacation = ProgressiveVacationModel()
        progressive_vacation.document_employee_id = document_employee_id
        progressive_vacation.rut = data['rut']
        progressive_vacation.since = data['since']
        progressive_vacation.until = data['until']
        progressive_vacation.days = days
        progressive_vacation.no_valid_days = data['no_valid_days']
        progressive_vacation.support = ''
        progressive_vacation.added_date = datetime.now()
        progressive_vacation.updated_date = datetime.now()

        db.session.add(progressive_vacation)
        try:
            db.session.commit()

            return progressive_vacation
        except Exception as e:
            return {'msg': 'Data could not be stored'}