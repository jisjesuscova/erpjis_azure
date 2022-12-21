from flask import request
from app.models.models import NationalityModel
from app import db

class Nationality():
    @staticmethod
    def get(id = ''):
        if id == '':
            gender = NationalityModel.query.all()
        else:
            gender = NationalityModel.query.get(id)

        return gender
