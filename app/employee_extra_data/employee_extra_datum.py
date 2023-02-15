from flask import request
from app.models.models import EmployeeExtraModel, OldEmployeeExtraModel
from app import db

class EmployeeExtraDatum():
    @staticmethod
    def get(rut = ''):
        employee_extra_data = EmployeeExtraModel.query.filter_by(rut=rut).first()

        return employee_extra_data

    @staticmethod
    def get_by_rut(rut = ''):
        employee_extra_data = EmployeeExtraModel.query.filter_by(rut=rut).all()

        return employee_extra_data

    @staticmethod
    def delete(id):
        employee_extra_datum = EmployeeExtraModel.query.filter_by(id=id).first()

        db.session.delete(employee_extra_datum)
        try:
            db.session.commit()

            return employee_extra_datum
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def update(data, rut):
        employee_extra_datum = EmployeeExtraModel.query.filter_by(rut=rut).first()
        employee_extra_datum.contract_schedule_id = data['contract_schedule_id']
        employee_extra_datum.extreme_zone_id = data['extreme_zone_id']
        employee_extra_datum.employee_type_id = data['employee_type_id']
        employee_extra_datum.health_payment_id = data['health_payment_id']
        employee_extra_datum.young_job_status_id = data['young_job_status_id']
        employee_extra_datum.be_paid_id = data['be_paid_id']
        employee_extra_datum.disability_id = data['disability_id']
        employee_extra_datum.progressive_vacation_status_id = data['progressive_vacation_status_id']
        employee_extra_datum.progressive_vacation_date = data['progressive_vacation_date']
        employee_extra_datum.pensioner_id = data['pensioner_id']
        employee_extra_datum.extra_health_amount = data['extra_health_amount']

        db.session.add(employee_extra_datum)
        db.session.commit()
        
        return employee_extra_datum

    @staticmethod
    def old_data_get_by_rut(rut = '', order_id = ''):
        old_employee_extra_data = OldEmployeeExtraModel.query.filter_by(rut=rut, order_id=order_id).all()

        return old_employee_extra_data

    @staticmethod
    def restore(rut, order_id):
        old_employee_extra_data = EmployeeExtraDatum.old_data_get_by_rut(rut, order_id)

        data = []

        for old_employee_extra_datum in old_employee_extra_data:
            data = [
                old_employee_extra_datum.rut,
                old_employee_extra_datum.visual_rut,
                old_employee_extra_datum.contract_schedule_id,
                old_employee_extra_datum.extreme_zone_id,
                old_employee_extra_datum.employee_type_id,
                old_employee_extra_datum.health_payment_type_id,
                old_employee_extra_datum.young_job_status_id,
                old_employee_extra_datum.be_paid_id,
                old_employee_extra_datum.regime_id,
                old_employee_extra_datum.suplemental_health_insurance_id,
                old_employee_extra_datum.pention_id,
                old_employee_extra_datum.entrance_pention,
                old_employee_extra_datum.disability_id,
                old_employee_extra_datum.progressive_vacation_status_id,
                old_employee_extra_datum.pensioner_id,
                old_employee_extra_datum.health_id,
                old_employee_extra_datum.entrance_health,
                old_employee_extra_datum.added_date,
                old_employee_extra_datum.updated_date
            ]

            EmployeeExtraDatum.restore_store(data)

            EmployeeExtraDatum.old_data_delete(old_employee_extra_datum.id)

        return 1

    @staticmethod
    def restore_store(data):
        employee_extra_datum = EmployeeExtraModel()
        employee_extra_datum.rut = data[0]
        employee_extra_datum.visual_rut = data[1]
        employee_extra_datum.contract_schedule_id = data[2]
        employee_extra_datum.extreme_zone_id = data[3]
        employee_extra_datum.employee_type_id = data[4]
        employee_extra_datum.health_payment_type_id = data[5]
        employee_extra_datum.young_job_status_id = data[6]
        employee_extra_datum.be_paid_id = data[7]
        employee_extra_datum.regime_id = data[8]
        employee_extra_datum.suplemental_health_insurance_id = data[9]
        employee_extra_datum.pention_id = data[10]
        employee_extra_datum.entrance_pention = data[11]
        employee_extra_datum.disability_id = data[12]
        employee_extra_datum.progressive_vacation_status_id = data[13]
        employee_extra_datum.pensioner_id = data[14]
        employee_extra_datum.health_id = data[15]
        employee_extra_datum.entrance_health = data[16]
        employee_extra_datum.added_date = data[17]
        employee_extra_datum.updated_date = data[18]

        db.session.add(employee_extra_datum)
        db.session.commit()
        
        return employee_extra_datum.id

    @staticmethod
    def old_data_delete(id):
        old_employee_extra_datum = OldEmployeeExtraModel.query.filter_by(id=id).first()

        db.session.delete(old_employee_extra_datum)
        try:
            db.session.commit()

            return old_employee_extra_datum
        except Exception as e:
            return {'msg': 'Data could not be stored'}