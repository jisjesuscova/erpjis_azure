from flask import request
from app.models.models import DocumentTypeModel
from app import db
from datetime import datetime

class DocumentType():
    @staticmethod
    def get(id = '', group_id = '', field = '', value = '', special_id = []):
        if id == '':
            document_type = DocumentTypeModel.query.filter_by(document_group_id = group_id).order_by('order').all()
        else:
            document_type = DocumentTypeModel.query.get(id)

        return document_type