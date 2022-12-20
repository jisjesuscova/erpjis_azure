from flask import request
from app.models.models import UserModel
from app.helpers.helper import Helper
from app import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class User():
    @staticmethod
    def get(id = ''):
        if id == '':
            users = UserModel.query.all()

            return users
        else:
            user = UserModel.query.get(id)

            return user

    @staticmethod
    def store(data):
        numeric_rut = Helper.numeric_rut(data['rut'])
        nickname = Helper.nickname(data['names'], data['father_lastname'])

        user = UserModel()
        user.rol_id = 1
        user.rut = numeric_rut
        user.visual_rut = data['rut']
        user.email = data['email']
        user.nickname = nickname
        user.password = generate_password_hash(data['rut'])
        user.added_date = datetime.now()
        user.updated_date = datetime.now()

        db.session.add(user)
        db.session.commit()

        if db.session.commit():
            return user
        else:
            return {'msg': 'Data could not be stored'}

    
