from flask import request
from app.models.models import OldEmployeeLaborDatumModel
from app.helpers.helper import Helper
from app import db
from datetime import datetime

class OldContractDatum():
    @staticmethod
    def get(rut):
        employee_labor_data = OldEmployeeLaborDatumModel.query.filter_by(rut = rut).first()

        return employee_labor_data
