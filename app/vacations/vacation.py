from app.models.models import VacationModel, EmployeeLaborDatumModel, DocumentEmployeeModel
from app.helpers.helper import Helper
from app import db
from datetime import datetime, date
from sqlalchemy import func

class Vacation():
    @staticmethod
    def get(rut = '', id = '', status_id = ''):
        if rut != '':
            if status_id != '':
                vacations = VacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                    .add_columns(VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id==status_id).order_by(db.desc(DocumentEmployeeModel.added_date))
            else:
                 vacations = VacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                    .add_columns(VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6).order_by(db.desc(DocumentEmployeeModel.added_date))

            return vacations
        else:
            vacation = VacationModel.query.filter_by(id=id).first()

            return vacation

    @staticmethod
    def get_by_major(rut = '', id = '', status_id = '', limit = ''):
        if limit == '':
            if rut != '':
                vacations = VacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                        .add_columns(VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(DocumentEmployeeModel.added_date))

                return vacations
            else:
                vacation = VacationModel.query.filter_by(id=id).first()

                return vacation
        else:
            vacations = VacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                        .add_columns(VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(DocumentEmployeeModel.added_date)).limit(limit)

            return vacations

    @staticmethod
    def get_total(rut = '', status_id = ''):
        vacation_count = VacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                        .add_columns(VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(DocumentEmployeeModel.added_date))

        count = vacation_count.count()

        if count > 1:
            vacations = VacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                    .add_columns(VacationModel.rut, func.sum(VacationModel.days).label('total_days'))\
                    .filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id > status_id)\
                    .group_by(VacationModel.rut)\
                    .order_by(db.desc(DocumentEmployeeModel.added_date)).limit(1)

            return vacations
        else:
            return vacations

    @staticmethod
    def get_by_document(id):

        vacation = VacationModel.query.filter_by(document_employee_id=id).first()

        return vacation
        
    @staticmethod
    def store(data, document_employee_id):
        days = Helper.days(data['since'], data['until'], data['no_valid_days'])

        vacation = VacationModel()
        vacation.document_employee_id = document_employee_id
        vacation.rut = data['rut']
        vacation.since = data['since']
        vacation.until = data['until']
        vacation.days = days
        vacation.no_valid_days = data['no_valid_days']
        vacation.support = ''
        vacation.added_date = datetime.now()
        vacation.updated_date = datetime.now()

        db.session.add(vacation)
        try:
            db.session.commit()

            return vacation
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def update(id = '', document_employee_id = '', data = []):

        days = Helper.days(data['since'], data['until'], data['no_valid_days'])
        
        vacation = VacationModel.query.filter_by(document_employee_id=document_employee_id).first()
        vacation.since = data['since']
        vacation.until = data['until']
        vacation.days = days
        vacation.no_valid_days = data['no_valid_days']
        vacation.updated_date = datetime.now()

        db.session.add(vacation)
        try:
            db.session.commit()

            return vacation
        except Exception as e:
            return {'msg': 'Data could not be stored'}
        
    @staticmethod
    def delete(id):
        vacation = VacationModel.query.filter_by(id=id).first()

        db.session.delete(vacation)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0
    
    @staticmethod
    def legal(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()
        months = Helper.months(employee_labor_data.entrance_company, date.today())
        vacation_days = Helper.vacation_days(months, employee_labor_data.extreme_zone_id)

        return vacation_days
    
    @staticmethod
    def taken_days(rut):
        taken_days = Helper.get_taken_days(rut)

        return taken_days
    
    @staticmethod
    def balance(legal, taken_days):
        return legal - taken_days
    
    @staticmethod
    def upload(id, file):
        vacation = VacationModel.query.filter_by(id=id).first()
        vacation.support = file
        vacation.updated_date = datetime.now()

        db.session.add(vacation)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0