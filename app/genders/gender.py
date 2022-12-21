from flask import request
from app.models.models import GenderModel
from app import db

class Gender():
    @staticmethod
    def get(id = ''):
        if id == '':
            gender = GenderModel.query.all()
        else:
            gender = GenderModel.query.get(id)

        return gender
