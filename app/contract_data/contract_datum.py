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
    def store(data):
        numeric_rut = Helper.numeric_rut(data['rut'])

        employee_labor_data = EmployeeLaborDatumModel()
        employee_labor_data.rut = numeric_rut
        employee_labor_data.visual_rut = data['rut']
        employee_labor_data.entrance_company = data['entrance_company']
        employee_labor_data.added_date = datetime.now()

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
        employee_labor_data.commune_id = 0
        employee_labor_data.civil_state_id = data['civil_state_id']
        employee_labor_data.health_id = data['health_id']
        employee_labor_data.pention_id = data['pention_id']
        employee_labor_data.job_position_id = data['job_position_id']
        employee_labor_data.employee_type_id = data['employee_type_id']
        employee_labor_data.address = data['address']
        employee_labor_data.entrance_company = data['entrance_company']
        employee_labor_data.salary = data['salary']
        employee_labor_data.collation = data['collation']
        employee_labor_data.locomotion = data['locomotion']
        employee_labor_data.updated_date = datetime.now()

        db.session.add(employee_labor_data)
        db.session.commit()
        
        return employee_labor_data
