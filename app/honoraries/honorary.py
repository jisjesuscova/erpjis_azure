from app.models.models import HonoraryModel, BankModel, BranchOfficeModel, RegionModel, CommunesModel, EmployeeModel, HonoraryReasonModel
from app.helpers.helper import Helper
from flask_login import current_user
from app import db
from datetime import datetime, date
from sqlalchemy import func

class Honorary():
    @staticmethod
    def get(id, page):
        if id != '':
            honorary = HonoraryModel.query.filter_by(id = id).first()
        
            return honorary
        else:
            honoraries = HonoraryModel.query\
                    .join(BankModel, BankModel.id == HonoraryModel.bank_id)\
                    .join(BranchOfficeModel, BranchOfficeModel.id == HonoraryModel.branch_office_id)\
                    .join(RegionModel, RegionModel.id == HonoraryModel.region_id)\
                    .join(CommunesModel, CommunesModel.id == HonoraryModel.commune_id)\
                    .join(EmployeeModel, EmployeeModel.rut == HonoraryModel.requested_by)\
                    .join(HonoraryReasonModel, HonoraryReasonModel.id == HonoraryModel.reason_id)\
                    .add_columns(HonoraryModel.id, HonoraryModel.rut, HonoraryModel.full_name, EmployeeModel.nickname, HonoraryReasonModel.reason, HonoraryModel.added_date).paginate(page=page, per_page=10, error_out=False)
        
            return honoraries

        
    @staticmethod
    def store(data):
        honorary = HonoraryModel()
        honorary.reason_id = data['reason_id']
        honorary.branch_office_id = data['branch_office_id']
        honorary.foreigner_id = data['foreigner_id']
        honorary.bank_id = data['bank_id']
        honorary.schedule_id = data['schedule_id']
        honorary.region_id = data['region_id']
        honorary.commune_id = data['commune_id']
        honorary.requested_by = current_user.rut
        honorary.employee_to_replace = data['employee_to_replace']
        honorary.rut = data['rut']
        honorary.full_name = data['full_name']
        honorary.email = data['email']
        honorary.address = data['address']
        honorary.account_number = data['account_number']
        honorary.start_date = data['start_date']
        honorary.end_date = data['end_date']
        honorary.account_number = data['account_number']
        honorary.added_date = datetime.now()
        honorary.updated_date = datetime.now()

        db.session.add(honorary)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def update(id = '', document_employee_id = '', data = []):

        days = Helper.days(data['since'], data['until'], data['no_valid_days'])
        
        vacation = VacationModel.query.filter_by(document_employee_id=document_employee_id).first()
        vacation.since = data['since']
        vacation.until = data['until']
        vacation.days = days
        vacation.no_valid_days = data['no_valid_days']
        vacation.updated_date = datetime.now()

        db.session.add(vacation)
        try:
            db.session.commit()

            return vacation
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def delete(id):
        honorary = HonoraryModel.query.filter_by(id=id).first()

        db.session.delete(honorary)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0