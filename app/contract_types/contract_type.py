from flask import request
from app.models.models import ContractTypeModel
from app import db
from datetime import datetime

class ContractType():
    @staticmethod
    def get(id = ''):
        if id == '':
            contract_types = ContractTypeModel.query.all()

            return contract_types
        else:
            contract_type = ContractTypeModel.query.get(id)

            return contract_type

    @staticmethod
    def store(data):
        contract_type = ContractTypeModel()
        contract_type.contract_type = data['contract_type']
        contract_type.added_date = datetime.now()
        contract_type.updated_date = datetime.now()

        db.session.add(contract_type)
        db.session.commit()
        
        return contract_type

    @staticmethod
    def update(data, id):
        contract_type = ContractTypeModel.query.get(id)
        contract_type.contract_type = data['contract_type']
        contract_type.updated_date = datetime.now()

        db.session.add(contract_type)
        db.session.commit()
        
        return contract_type

    @staticmethod
    def delete(id):
        contract_type = ContractTypeModel.query.get(id)

        db.session.delete(contract_type)
        db.session.commit()
        
        return contract_type

