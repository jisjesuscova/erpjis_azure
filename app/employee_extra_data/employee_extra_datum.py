from flask import request
from app.models.models import EmployeeExtraModel, OldEmployeeExtraModel
from app import db
from datetime import datetime, date
from app.helpers.helper import Helper
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum

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
    def empty_fields(rut):
        employee_extra_datum = EmployeeExtraModel.query.filter_by(rut = rut).first()

        count = 0

        if employee_extra_datum.extreme_zone_id == None or employee_extra_datum.extreme_zone_id == '':
            count = count + 1

        if employee_extra_datum.employee_type_id == None or employee_extra_datum.employee_type_id == '':
            count = count + 1

        if employee_extra_datum.young_job_status_id == None or employee_extra_datum.young_job_status_id == '':
            count = count + 1

        if employee_extra_datum.be_paid_id == None or employee_extra_datum.be_paid_id == '':
            count = count + 1

        if employee_extra_datum.suplemental_health_insurance_id == None or employee_extra_datum.suplemental_health_insurance_id == '':
            count = count + 1

        if employee_extra_datum.disability_id == None or employee_extra_datum.disability_id == '':
            count = count + 1

        if employee_extra_datum.pensioner_id == None or employee_extra_datum.pensioner_id == '':
            count = count + 1

        if employee_extra_datum.progressive_vacation_status_id == None or employee_extra_datum.progressive_vacation_status_id == '':
            count = count + 1

        if employee_extra_datum.progressive_vacation_date == None or employee_extra_datum.progressive_vacation_date == '':
            count = count + 1

        if  count > 4:
            return 0
        else:
            return 1

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
    def store(data):
        numeric_rut = Helper.numeric_rut(data['rut'])

        employee_extra_datum = EmployeeExtraModel()
        employee_extra_datum.rut = numeric_rut
        employee_extra_datum.visual_rut = data['rut']

        db.session.add(employee_extra_datum)

        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0
    
    @staticmethod
    def update_level(rut, level):
        employee_extra_datum = EmployeeExtraModel.query.filter_by(rut=rut).first()
        employee_extra_datum.progressive_vacation_level_id = level
        db.session.add(employee_extra_datum)
        db.session.commit()

        return 1

    @staticmethod
    def update(data, rut):
        employee_extra_datum = EmployeeExtraModel.query.filter_by(rut=rut).first()
        employee_extra_datum.extreme_zone_id = data['extreme_zone_id']
        employee_extra_datum.employee_type_id = data['employee_type_id']
        employee_extra_datum.young_job_status_id = data['young_job_status_id']
        employee_extra_datum.be_paid_id = data['be_paid_id']
        employee_extra_datum.disability_id = data['disability_id']
        employee_extra_datum.suplemental_health_insurance_id = data['suplemental_health_insurance_id']
        employee_extra_datum.progressive_vacation_status_id = data['progressive_vacation_status_id']
        employee_extra_datum.progressive_vacation_date = data['progressive_vacation_date']
        employee_extra_datum.pensioner_id = data['pensioner_id']

        if data['recognized_years'] == '':
            recognized_years = 0
        else:
            recognized_years = data['recognized_years']

        employee_extra_datum.recognized_years = recognized_years
        employee_extra_datum.progressive_vacation_level_id = 0

        db.session.add(employee_extra_datum)
        
        try:
            db.session.commit()

            employee_labor_datum = EmployeeLaborDatum.get(rut)

            how_many_months = Helper.months(employee_labor_datum.entrance_company, employee_extra_datum.progressive_vacation_date)
            years = Helper.months_to_years(how_many_months)
            
            total_years = int(years) + int(employee_extra_datum.recognized_years)

            level = Helper.progressive_vacation_level(total_years)

            employee_extra_datum = EmployeeExtraDatum.update_level(rut, level)
            
            return 1
        except Exception as e:
            return 0

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
                old_employee_extra_datum.extreme_zone_id,
                old_employee_extra_datum.employee_type_id,
                old_employee_extra_datum.young_job_status_id,
                old_employee_extra_datum.be_paid_id,
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
        employee_extra_datum.extreme_zone_id = data[2]
        employee_extra_datum.employee_type_id = data[3]
        employee_extra_datum.young_job_status_id = data[4]
        employee_extra_datum.be_paid_id = data[5]
        employee_extra_datum.suplemental_health_insurance_id = data[6]
        employee_extra_datum.pention_id = data[7]
        employee_extra_datum.entrance_pention = data[8]
        employee_extra_datum.disability_id = data[9]
        employee_extra_datum.progressive_vacation_status_id = data[10]
        employee_extra_datum.pensioner_id = data[11]
        employee_extra_datum.health_id = data[12]
        employee_extra_datum.entrance_health = data[13]
        employee_extra_datum.added_date = data[14]
        employee_extra_datum.updated_date = data[15]

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