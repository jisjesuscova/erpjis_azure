from flask import request
from app.models.models import DocumentEmployeeModel
from app import db
from datetime import datetime

class DocumentEmployee():
    @staticmethod
    def get(rut, page):
        documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut).paginate(page=page, per_page=20, error_out=False)
        
        return documents_employees

    @staticmethod
    def store(data):
        document_employee = DocumentEmployeeModel()
        document_employee.status_id = data['status_id']
        document_employee.rut = data['rut']
        document_employee.document_type_id = data['document_type_id']
        document_employee.added_date = datetime.now()
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        db.session.commit()
        
        return document_employee.id