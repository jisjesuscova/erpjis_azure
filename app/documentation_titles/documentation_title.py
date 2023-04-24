from flask import request
from app.models.models import DocumentationTitleModel, DocumentationSubTitleModel
from app import db
from datetime import datetime
import markdown
from app.helpers.helper import Helper
from bs4 import BeautifulSoup

class DocumentationTitle():
    @staticmethod
    def get(id = ''):
        if id == '':
            documentation_titles = DocumentationTitleModel.query.all()
        else:
            documentation_titles = DocumentationTitleModel.query.filter_by(documentation_id = id).all() 

        return documentation_titles
    
    @staticmethod
    def delete(id = ''):
        delete_documentation_title = DocumentationTitleModel.query.filter_by(documentation_id=id).first()

        db.session.delete(delete_documentation_title)

        db.session.commit()