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

    @staticmethod
    def special_update(rut, password):
        user = UserModel.query.filter_by(rut=rut).first()
        user.password = generate_password_hash(str(password))
        user.updated_date = datetime.now()

        db.session.add(user)
        db.session.commit()

        if db.session.commit():
            return user
        else:
            return {'msg': 'Data could not be stored'}

    
