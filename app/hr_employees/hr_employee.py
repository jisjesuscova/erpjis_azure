from flask import request
from app.models.models import HrEmployeeModel, EmployeeLaborDataModel, HrInputDescriptionModel
from app.helpers.helper import Helper

from app import db
from datetime import datetime

class HrEmployee():
    @staticmethod
    def get(period):
        hr_employees = HrEmployeeModel.query.filter_by(period=period).group_by('rut').all()

        return hr_employees

    @staticmethod
    def open(data):
        HrEmployee.value(1, data)
            
    def value(hr_input_type_id, data):
        hr_input_descriptions = HrInputDescriptionModel.query.filter_by(hr_input_type_id = id).all()

        for hr_input_description in hr_input_descriptions:
            employee_labor_data = EmployeeLaborDataModel.query.all()

            for employee_labor_datum in employee_labor_data:
                period = Helper.period(data['month'], data['year'])

                hr_employee = HrEmployeeModel()
                hr_employee.rut = employee_labor_datum.rut
                hr_employee.period = period
                hr_employee.branch_office_id = employee_labor_datum.branch_office_id
                hr_employee.value = employee_labor_datum.salary
                hr_employee.hr_input_description_id = hr_input_description.hr_input_description_id
                hr_employee.added_date = datetime.now()
                hr_employee.updated_date = datetime.now()

                db.session.add(hr_employee)
                try:
                    db.session.commit()

                    return hr_employee
                except Exception as e:
                    return {'msg': 'Data could not be stored'}