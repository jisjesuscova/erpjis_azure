from flask import request
from app.models.models import DocumentEmployeeModel, DocumentTypeModel, DocumentGroupModel
from app.helpers.helper import Helper
from flask_sqlalchemy import get_debug_queries
from app import db
from datetime import datetime

class KardexDatum():
    @staticmethod
    def get(rut):
        documents_employees = DocumentEmployeeModel.query\
        .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
        .join(DocumentGroupModel, DocumentGroupModel.id == DocumentTypeModel.document_group_id)\
        .add_columns(DocumentEmployeeModel.id, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date)\
        .filter(DocumentEmployeeModel.rut==rut)\
        .filter(DocumentGroupModel.id==1)\
        .order_by(DocumentTypeModel.order.asc())\
        .all()

        return documents_employees

    @staticmethod
    def store(data, support = ''):
        document_employee_data = DocumentEmployeeModel()
        document_employee_data.status_id = 0
        document_employee_data.rut = data['rut']
        document_employee_data.document_type_id = data['document_type_id']
        document_employee_data.support = support
        document_employee_data.added_date = datetime.now()

        db.session.add(document_employee_data)
        
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0