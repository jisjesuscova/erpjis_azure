from flask import request
from app.models.models import DocumentationSubTitleModel
from app import db

class DocumentationSubTitle():
    @staticmethod
    def delete(id = ''):
        delete_documentation_subtitle = DocumentationSubTitleModel.query.filter_by(documentation_id=id).first()

        db.session.delete(delete_documentation_subtitle)

        db.session.commit()