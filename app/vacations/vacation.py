from app.models.models import VacationModel, TotalVacationDaysModel, EmployeeExtraModel, EmployeeLaborDatumModel, DocumentEmployeeModel, OldVacationModel, OldDocumentEmployeeModel
from app.helpers.helper import Helper
from app import db
from datetime import datetime, date
from sqlalchemy import func
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum

class Vacation():
    @staticmethod
    def get(rut = '', id = '', status_id = []):
        if rut != '':
            if len(status_id) > 0:
                vacations = VacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                    .add_columns(VacationModel.no_valid_days, VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id.in_(status_id)).order_by(db.desc(VacationModel.since))
            else:
                vacations = VacationModel.query\
                    .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                    .add_columns(VacationModel.no_valid_days, VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, VacationModel.no_valid_days, VacationModel.added_date, VacationModel.updated_date, VacationModel.support, DocumentEmployeeModel.status_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6).order_by(db.desc(VacationModel.since))

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
                        .add_columns(VacationModel.no_valid_days, VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(VacationModel.since))

                return vacations
            else:
                vacation = VacationModel.query.filter_by(id=id).first()

                return vacation
        else:
            vacations = VacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                        .add_columns(VacationModel.no_valid_days, VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(VacationModel.since)).limit(limit)

            return vacations

    @staticmethod
    def get_total(rut = '', status_id = ''):
        vacation_count = VacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                        .add_columns(VacationModel.document_employee_id, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id, VacationModel.document_employee_id).filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, DocumentEmployeeModel.status_id > status_id).order_by(db.desc(DocumentEmployeeModel.added_date))

        count = vacation_count.count()

        if count >= 1:
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

            return 1
        except Exception as e:
            return 0

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
    def request(id = '', data = ''):

        days = Helper.days(data['since'], data['until'], data['no_valid_days'])
        
        vacation = VacationModel.query.filter_by(document_employee_id=id).first()
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
    def end_document_update(old_id, new_id):
        vacation = VacationModel.query.filter_by(document_employee_id=old_id).first()
        vacation.document_employee_id = new_id

        db.session.add(vacation)
        db.session.commit()
        
        return vacation.id
        
    @staticmethod
    def delete(id):
        vacation = VacationModel.query.filter_by(document_employee_id=id).first()

        db.session.delete(vacation)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def delete_by_document_id(id):
        vacation = VacationModel.query.filter_by(document_employee_id=id).first()

        db.session.delete(vacation)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    def calculate_total_vacation_days():
        total_vacation_days = TotalVacationDaysModel.query.filter_by(id=1).first()

        total = total_vacation_days.total_employee_vacation_days - (total_vacation_days.total_days - total_vacation_days.total_no_valid_days)

        return total

    @staticmethod
    def legal(rut):
        employee_labor_data = EmployeeLaborDatum.get(rut)
        employee_extra_data = EmployeeExtraDatum.get(rut)
        months = Helper.months(employee_labor_data.entrance_company, date.today())
        vacation_days = Helper.vacation_days(months, employee_extra_data.extreme_zone_id)

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

    @staticmethod
    def old_data_get(rut = '', order_id = ''):
        old_vacations = OldVacationModel.query\
                    .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == OldVacationModel.document_employee_id)\
                    .add_columns(OldVacationModel.document_employee_id, OldVacationModel.id, OldVacationModel.rut, OldVacationModel.since, OldVacationModel.until, OldVacationModel.days, OldVacationModel.no_valid_days, OldVacationModel.added_date, OldVacationModel.updated_date, OldVacationModel.support, OldDocumentEmployeeModel.status_id).filter(OldVacationModel.order_id==order_id, OldDocumentEmployeeModel.rut==rut, OldDocumentEmployeeModel.document_type_id==6).order_by(db.desc(OldDocumentEmployeeModel.added_date))

        return old_vacations

    @staticmethod
    def restore(rut, order_id):
        old_vacations = Vacation.old_data_get(rut, order_id)

        data = []

        for old_vacation in old_vacations:
            data = [
                old_vacation.document_employee_id,
                old_vacation.rut,
                old_vacation.since,
                old_vacation.until,
                old_vacation.days,
                old_vacation.no_valid_days,
                old_vacation.support,
                old_vacation.added_date,
                old_vacation.updated_date
            ]

            Vacation.restore_store(data)

            Vacation.old_data_delete(old_vacation.id)

        return 1

    @staticmethod
    def restore_store(data):
        vacation = VacationModel()
        vacation.document_employee_id = data[0]
        vacation.rut = data[1]
        vacation.since = data[2]
        vacation.until = data[3]
        vacation.days = data[4]
        vacation.no_valid_days = data[5]
        vacation.support = data[6]
        vacation.added_date = data[7]
        vacation.updated_date = data[8]

        db.session.add(vacation)
        try:
            db.session.commit()

            return vacation
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def old_data_delete(id):
        old_vacation = OldVacationModel.query.filter_by(id=id).first()

        db.session.delete(old_vacation)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0