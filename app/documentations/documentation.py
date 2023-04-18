from flask import request
from app.models.models import DocumentationModel, PreDocumentationModel
from app import db
from datetime import datetime
import markdown

class Documentation():
    @staticmethod
    def get(page):
        documentations = DocumentationModel.query.order_by(DocumentationModel.added_date.asc()).paginate(page=page, per_page=20, error_out=False)

        return documentations

    @staticmethod
    def pre_store(data):
        pre_documentation = PreDocumentationModel()
        pre_documentation.title = '123'
        pre_documentation.description = markdown.markdown(data['description'])
        pre_documentation.added_date = datetime.now()
        pre_documentation.updated_date = datetime.now()

        db.session.add(pre_documentation)

        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0