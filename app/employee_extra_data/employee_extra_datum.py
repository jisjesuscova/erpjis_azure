from flask import request
from app.models.models import EmployeeExtraModel

class EmployeeExtraDatum():
    @staticmethod
    def get(rut = ''):
            employee_extra_data = EmployeeExtraModel.query.filter_by(rut=rut).first()

            return employee_extra_data