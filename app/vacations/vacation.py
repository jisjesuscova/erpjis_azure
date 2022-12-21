from app.models.models import VacationModel, EmployeeLaborDatumModel
from app.helpers.helper import Helper
from app import db
from datetime import datetime, date

class Vacation():
    @staticmethod
    def get(rut):
        vacations = VacationModel.query.filter_by(rut=rut).all()
        
        return vacations

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