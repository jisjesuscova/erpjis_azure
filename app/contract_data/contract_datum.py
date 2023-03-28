from flask import request
from app.models.models import EmployeeLaborDatumModel
from app.helpers.helper import Helper
from app import db
from datetime import datetime

class ContractDatum():
    @staticmethod
    def get(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut = rut).first()

        return employee_labor_data

    @staticmethod
    def empty_fields(rut):
        employee_labor_datum = EmployeeLaborDatumModel.query.filter_by(rut = rut).first()

        count = 0

        if employee_labor_datum.contract_type_id == None or employee_labor_datum.contract_type_id == '':
            count = count + 1

        if employee_labor_datum.branch_office_id == None or employee_labor_datum.branch_office_id == '':
            count = count + 1

        if employee_labor_datum.region_id == None or employee_labor_datum.region_id == '':
            count = count + 1

        if employee_labor_datum.commune_id == None or employee_labor_datum.commune_id == '':
            count = count + 1

        if employee_labor_datum.address == None or employee_labor_datum.address == '':
            count = count + 1

        if employee_labor_datum.civil_state_id == None or employee_labor_datum.civil_state_id == '':
            count = count + 1

        if employee_labor_datum.entrance_health == None or employee_labor_datum.entrance_health == '':
            count = count + 1

        if employee_labor_datum.job_position_id == None or employee_labor_datum.job_position_id == '':
            count = count + 1

        if employee_labor_datum.entrance_company == None or employee_labor_datum.entrance_company == '':
            count = count + 1

        if employee_labor_datum.salary == None or employee_labor_datum.salary == '':
            count = count + 1

        if employee_labor_datum.collation == None or employee_labor_datum.collation == '':
            count = count + 1

        if employee_labor_datum.regime_id == None or employee_labor_datum.regime_id == '':
            count = count + 1

        if employee_labor_datum.health_id == None or employee_labor_datum.health_id == '':
            count = count + 1

        if employee_labor_datum.pention_id == None or employee_labor_datum.pention_id == '':
            count = count + 1

        if employee_labor_datum.entrance_pention == None or employee_labor_datum.entrance_pention == '':
            count = count + 1

        if employee_labor_datum.health_payment_id == None or employee_labor_datum.health_payment_id == '':
            count = count + 1

        if employee_labor_datum.extra_health_amount == None or employee_labor_datum.extra_health_amount == '':
            count = count + 1

        if  count > 4:
            return 0
        else:
            return 1
        
    @staticmethod
    def store(data):
        numeric_rut = Helper.numeric_rut(data['rut'])

        employee_labor_data = EmployeeLaborDatumModel()
        employee_labor_data.rut = numeric_rut
        employee_labor_data.visual_rut = data['rut']
        employee_labor_data.entrance_company = data['entrance_company']
        employee_labor_data.added_date = datetime.now()
        
        db.session.add(employee_labor_data)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def restore(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut = rut).first()
        employee_labor_data.status_id = 1
        employee_labor_data.exit_company = None
        employee_labor_data.updated_date = datetime.now()

        db.session.add(employee_labor_data)
        db.session.commit()
        
        return employee_labor_data

    @staticmethod
    def update(data, rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut = rut).first()
        employee_labor_data.contract_type_id = data['contract_type_id']
        employee_labor_data.branch_office_id = data['branch_office_id']
        employee_labor_data.address = data['address']
        employee_labor_data.region_id = data['region_id']
        employee_labor_data.commune_id = data['commune_id']
        employee_labor_data.civil_state_id = data['civil_state_id']
        employee_labor_data.health_id = data['health_id']
        employee_labor_data.pention_id = data['pention_id']
        employee_labor_data.job_position_id = data['job_position_id']
        employee_labor_data.employee_type_id = data['employee_type_id']
        employee_labor_data.regime_id = data['regime_id']
        employee_labor_data.address = data['address']
        entrance_pention = Helper.fix_entrance_date(data['entrance_pention'])
        employee_labor_data.entrance_pention = entrance_pention
        employee_labor_data.entrance_company = data['entrance_company']
        employee_labor_data.entrance_health = data['entrance_health']
        employee_labor_data.salary = Helper.remove_from_string('.', data['salary'])
        employee_labor_data.collation = Helper.remove_from_string('.', data['collation'])
        employee_labor_data.locomotion = Helper.remove_from_string('.', data['locomotion'])
        employee_labor_data.health_payment_id = data['health_payment_id']
        employee_labor_data.extra_health_amount = data['extra_health_amount']
        employee_labor_data.apv_payment_type_id = data['apv_payment_type_id']
        employee_labor_data.apv_amount = data['apv_amount']
        employee_labor_data.updated_date = datetime.now()

        db.session.add(employee_labor_data)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0
