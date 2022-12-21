from flask import request
from app.models.models import AuditModel
from app import db
from datetime import datetime

class Audit():
    @staticmethod
    def store(data, model):
        audit = AuditModel()
        audit.rut = '123456'
        audit.model = model
        audit.affected_rut = data['rut']
        audit.added_date = datetime.now()

        db.session.add(audit)
        db.session.commit()
        
        return audit