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
        documentation_titles = DocumentationTitleModel.query.outerjoin(DocumentationTitleModel.sub_titles).all()

        return documentation_titles