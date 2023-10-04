from flask import request
from app.models.models import EmployeeBankAccountModel
from app import db
from datetime import datetime, date

class EmployeeBankAccount():
    @staticmethod
    def get(rut):
        employee_bank_account = EmployeeBankAccountModel.query.filter_by(rut=rut, status_id=1).order_by(EmployeeBankAccountModel.id.desc()).first()

        return employee_bank_account
    
    @staticmethod
    def get_change_requested(rut):
        employee_bank_account = EmployeeBankAccountModel.query.filter_by(rut=rut, status_id=0).order_by(EmployeeBankAccountModel.id.desc()).first()

        return employee_bank_account
    
    @staticmethod
    def get_by_id(id):
        employee_bank_account = EmployeeBankAccountModel.query.filter_by(id=id, status_id=0).order_by(EmployeeBankAccountModel.id.desc()).first()

        return employee_bank_account
    
    @staticmethod
    def get_status(rut):
        quantity = EmployeeBankAccountModel.query.filter_by(rut=rut, status_id=0).order_by(EmployeeBankAccountModel.id.desc()).count()

        if quantity > 0:
            return 1
        else:
            return 0

    @staticmethod
    def store(data, status_id):
        employee_bank_account = EmployeeBankAccountModel()
        employee_bank_account.rut = data['rut']
        employee_bank_account.bank_id = data['bank_id']
        employee_bank_account.status_id = status_id
        employee_bank_account.account_type_id = data['account_type_id']
        employee_bank_account.account_number = data['account_number']
        employee_bank_account.added_date = datetime.now()
        employee_bank_account.updated_date = datetime.now()

        db.session.add(employee_bank_account)
        
        try:
            db.session.commit()
            
            return employee_bank_account.id
        except Exception as e:
            return 0
        
    @staticmethod
    def accept(id):
        employee_bank_account = EmployeeBankAccountModel.query.filter_by(id=id).order_by(EmployeeBankAccountModel.id.desc()).first()
        employee_bank_account.status_id = 1
        employee_bank_account.updated_date = datetime.now()

        db.session.add(employee_bank_account)
        
        try:
            db.session.commit()
            
            return 1
        except Exception as e:
            return 0
        
    
    @staticmethod
    def delete(id):
        employee_bank_account = EmployeeBankAccountModel.query.filter_by(id=id).order_by(EmployeeBankAccountModel.id.desc()).first()
        db.session.delete(employee_bank_account)
        
        try:
            db.session.commit()
            
            return 1
        except Exception as e:
            return 0