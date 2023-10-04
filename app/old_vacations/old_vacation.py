from app.models.models import OldVacationModel, VacationModel, OldEmployeeLaborDatumModel, OldDocumentEmployeeModel
from app.vacations.vacation import Vacation
from app import db
from app.helpers.helper import Helper
from datetime import datetime, date

class OldVacation():
    @staticmethod
    def get(rut = '', id = '', status_id = ''):
        if rut != '':
            if status_id != '':
                vacations = OldVacationModel.query\
                    .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == OldVacationModel.document_employee_id)\
                    .add_columns(OldVacationModel.document_employee_id, OldVacationModel.id, OldVacationModel.rut, OldVacationModel.since, OldVacationModel.until, OldVacationModel.days, OldVacationModel.no_valid_days, OldDocumentEmployeeModel.status_id, OldVacationModel.document_employee_id).filter(OldDocumentEmployeeModel.rut==rut, OldDocumentEmployeeModel.document_type_id==6, OldDocumentEmployeeModel.status_id.in_(status_id)).order_by(db.desc(OldDocumentEmployeeModel.added_date))
            else:
                 vacations = OldVacationModel.query\
                    .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == OldVacationModel.document_employee_id)\
                    .add_columns(OldVacationModel.document_employee_id, OldVacationModel.id, OldVacationModel.rut, OldVacationModel.since, OldVacationModel.until, OldVacationModel.days, OldVacationModel.no_valid_days, OldVacationModel.added_date, OldVacationModel.updated_date, OldVacationModel.support, OldDocumentEmployeeModel.status_id).filter(OldDocumentEmployeeModel.rut==rut, OldDocumentEmployeeModel.document_type_id==6).order_by(db.desc(OldDocumentEmployeeModel.added_date))

            return vacations
        else:
            vacation = OldVacationModel.query.filter_by(id=id).first()

            return vacation

    @staticmethod
    def get_last_order(rut):
        vacation = OldVacationModel.query.filter_by(rut=rut).order_by(OldVacationModel.order_id.desc()).first()

        vacation_qty = OldVacationModel.query.filter_by(rut=rut).order_by(OldVacationModel.order_id.desc()).count()
        
        if vacation_qty > 0:
            return int(vacation.order_id) + 1
        else:
            return 1

    @staticmethod
    def finish(rut, order_id):
        vacations = Vacation.get(rut)
     
        data = []

        for vacation in vacations:
            data = [
                vacation.document_employee_id,
                order_id,
                vacation.rut,
                vacation.since,
                vacation.until,
                vacation.days,
                vacation.no_valid_days,
                vacation.support,
                vacation.added_date,
                vacation.updated_date
            ]

            OldVacation.store(data)

            Vacation.delete(vacation.document_employee_id)

        return 1

    @staticmethod
    def store(data):
        old_vacation = OldVacationModel()
        old_vacation.document_employee_id = data[0]
        old_vacation.order_id = data[1]
        old_vacation.rut = data[2]
        old_vacation.since = data[3]
        old_vacation.until = data[4]
        old_vacation.days = data[5]
        old_vacation.no_valid_days = data[6]
        old_vacation.support = data[7]
        old_vacation.added_date = data[8]
        old_vacation.updated_date = data[9]

        db.session.add(old_vacation)
        try:
            db.session.commit()

            return old_vacation
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    
    @staticmethod
    def legal(rut):
        employee_labor_data = OldEmployeeLaborDatumModel.query.filter_by(rut=rut).first()
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
    def update(old_id, new_id):
        old_vacation_qty = OldVacationModel.query.filter_by(document_employee_id=old_id).count()

        if old_vacation_qty > 0:
            old_vacation = OldVacationModel.query.filter_by(document_employee_id=old_id).first()
            old_vacation.document_employee_id = new_id

            db.session.add(old_vacation)
            db.session.commit()
            
            return old_vacation.id