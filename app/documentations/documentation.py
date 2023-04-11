from flask import request
from app.models.models import DocumentationModel
from app import db
from datetime import datetime

class Documentation():
    @staticmethod
    def get(page):
        documentations = DocumentationModel.query.order_by(DocumentationModel.added_date.asc()).paginate(page=page, per_page=20, error_out=False)

        return documentations