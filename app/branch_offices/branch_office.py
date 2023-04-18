from flask import request
from flask_login import login_required, current_user
from app.models.models import BranchOfficeModel, SupervisorModel, EmployeeLaborDatumModel
from app import db
from datetime import datetime

class BranchOffice():
    @staticmethod
    def get(id = ''):
        if id == '':
            if current_user.rol_id == 1:
                branch_offices = BranchOfficeModel.query\
                    .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.branch_office_id == BranchOfficeModel.id)\
                    .filter(EmployeeLaborDatumModel.rut == current_user.rut)\
                    .all()

                return branch_offices
            elif current_user.rol_id == 2:
                branch_offices = BranchOfficeModel.query\
                    .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.branch_office_id == BranchOfficeModel.id)\
                    .filter(EmployeeLaborDatumModel.rut == current_user.rut)\
                    .all()

                return branch_offices
            elif current_user.rol_id == 3:
                branch_offices = BranchOfficeModel.query\
                    .join(SupervisorModel, SupervisorModel.branch_office_id == BranchOfficeModel.id)\
                    .filter(SupervisorModel.rut == current_user.rut)\
                    .all()

                return branch_offices
            elif current_user.rol_id == 4:
                branch_offices = BranchOfficeModel.query.filter_by(visibility_id = '1').order_by('branch_office').all()

                return branch_offices
            elif current_user.rol_id == 5:
                branch_offices = BranchOfficeModel.query\
                    .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.branch_office_id == BranchOfficeModel.id)\
                    .filter(EmployeeLaborDatumModel.rut == current_user.rut)\
                    .all()

                return branch_offices
        else:
            branch_office = BranchOfficeModel.query.filter_by(id=id).first()

            return branch_office

        
