from flask import request
from app.models.models import PrincipalModel
from app import db
from datetime import datetime

class Principal():
    @staticmethod
    def get(id = ''):
        if id == '':
            principal = PrincipalModel.query.all()

            return principal
        else:
            principal = PrincipalModel.query.get(id)

            return principal

    @staticmethod
    def store(data):
        principal = PrincipalModel()
        principal.principal = data['principal'] 
        principal.added_date = datetime.now()
        principal.updated_date = datetime.now()

        db.session.add(principal)
        db.session.commit()
        
        return principal

    @staticmethod
    def update(data, id):
        principal = PrincipalModel.query.get(id)
        principal.principal = data['principal']
        principal.updated_date = datetime.now()

        db.session.add(principal)
        db.session.commit()
        
        return principal

    @staticmethod
    def delete(id):
        principal = PrincipalModel.query.get(id)

        db.session.delete(principal)
        db.session.commit()
        
        return principal

