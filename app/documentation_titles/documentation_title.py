from flask import request
from app.models.models import DocumentationTitleModel, DocumentationSubTitleModel
from app import db
from datetime import datetime
import markdown
from app.helpers.helper import Helper
from bs4 import BeautifulSoup

class DocumentationTitle():
    @staticmethod
    def get(id = '', level_id = ''):
        if level_id == 1:
            documentation_title = DocumentationTitleModel.query.filter_by(documentation_id=id).all()

            return documentation_title
        else:
            documentation_title = DocumentationSubTitleModel.query.filter_by(documentation_id=id).all()

            return documentation_title