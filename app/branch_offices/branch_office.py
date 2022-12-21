from flask import request
from app.models.models import BranchOfficeModel
from app import db
from datetime import datetime

class BranchOffice():
    @staticmethod
    def get(id = ''):
        if id == '':
            branch_offices = BranchOfficeModel.query.filter_by(visibility_id = '1').order_by('branch_office').all()

            return branch_offices
        else:
            branch_office = BranchOfficeModel.query.get(id)

            return branch_office

        
