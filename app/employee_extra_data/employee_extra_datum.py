from flask import request
from app.models.models import EmployeeExtraModel

class EmployeeExtraDatum():
    @staticmethod
    def get(rut = ''):
        employee_extra_data = EmployeeExtraModel.query.filter_by(rut=rut).first()

        return employee_extra_data

    @staticmethod
    def update(data, rut):
        employee_extra_data = EmployeeExtraModel.query.filter_by(rut=rut).first()
        employee_extra_data.contract_schedule_id = data['contract_schedule_id']
        employee_extra_data.extreme_zone_id = data['extreme_zone_id']
        employee_extra_data.employee_type_id = data['employee_type_id']
        employee_extra_data.health_payment_id = data['health_payment_id']
        employee_extra_data.young_job_status_id = data['young_job_status_id']
        employee_extra_data.be_paid_id = data['be_paid_id']
        employee_extra_data.regime_id = data['regime_id']
        employee_extra_data.pention_id = data['pention_id']
        employee_extra_data.entrance_pention = data['entrance_pention']
        employee_extra_data.disability_id = data['disability_id']
        employee_extra_data.progressive_vacation_status_id = data['progressive_vacation_status_id']
        employee_extra_data.pensioner_id = data['pensioner_id']
        employee_extra_data.health_id = data['health_id']
        employee_extra_data.entrance_health = data['entrance_health']
        
        return employee_extra_data