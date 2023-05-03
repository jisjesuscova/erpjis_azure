from flask import request
from app.models.models import UserModel
from app.helpers.helper import Helper
from app import db, mail
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_mail import Message

class User():
    @staticmethod
    def get(id = ''):
        if id == '':
            users = UserModel.query.all()

            return users
        else:
            user = UserModel.query.get(id)

            return user

    def get_by_id(id):
        user = UserModel.query.filter_by(id=id).first()

        return user
    
    @staticmethod
    def check_rut(rut):
        user_qty = UserModel.query.filter_by(rut=rut).count()

        if(user_qty > 0):
            return 1
        else:
            return 0

    def get_by_rut(rut):
        user = UserModel.query.filter_by(visual_rut=rut).first()

        return user

    def get_by_int_rut(rut):
        user = UserModel.query.filter_by(rut=rut).first()

        return user

    def get_by_rol_id(rol_id):
        users = UserModel.query.filter_by(rol_id=rol_id).all()

        return users
    
    def check_user_exists_by_token(token):
        quantity = UserModel.query.filter_by(api_token=token).count()
        
        return quantity

    def check_user_exists(rut):
        quantity = UserModel.query.filter_by(visual_rut=rut).count()

        return quantity

    def send_email(email):
        try:
            msg = Message(subject='Hello',
                    sender='jesuscova@jisparking.com',
                    recipients=['jesuscova@jisparking.com'],
                    body='This is a test email')
            mail.send(msg)
            return 'Email enviado'
        except Exception as e:
            return 'Error al enviar el correo: {}'.format(e)

    @staticmethod
    def store(data):
        numeric_rut = Helper.numeric_rut(data['rut'])
        nickname = Helper.nickname(data['names'], data['father_lastname'])

        user = UserModel()
        user.rol_id = 1
        user.clock_rol_id = data['privilege']
        user.rut = numeric_rut
        user.visual_rut = data['rut']
        user.email = data['personal_email']
        user.nickname = nickname
        user.password = generate_password_hash(data['rut'])
        user.api_token = generate_password_hash(data['rut'])
        user.added_date = datetime.now()
        user.updated_date = datetime.now()

        db.session.add(user)

        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def special_update(rut, password):
        user = UserModel.query.filter_by(rut=rut).first()
        user.password = generate_password_hash(str(password))
        user.status_id = 1
        user.updated_date = datetime.now()

        db.session.add(user)
        db.session.commit()

        if db.session.commit():
            return user
        else:
            return {'msg': 'Data could not be stored'}


    @staticmethod
    def update_status(rut, status_id):
        user = UserModel.query.filter_by(rut=rut).first()
        user.status_id = status_id
        user.updated_date = datetime.now()

        db.session.add(user)
        db.session.commit()

        if db.session.commit():
            return user
        else:
            return {'msg': 'Data could not be stored'}
    
