from flask import request
from app.models.models import PatologyTypeModel
from app import db

class PatologyType():
    @staticmethod
    def get():
        patology_types = PatologyTypeModel.query.all()

        return patology_types
