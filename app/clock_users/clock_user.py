from app.models.models import ClockUserModel
from app import db
from datetime import datetime
from flask import json
from app.helpers.helper import Helper

class ClockUser():
    @staticmethod
    def to_json(data):
        res = []

        for row in data:
            res.append({
                'uid': row.uid,
                'rut': row.rut,
                'full_name': row.full_name,
                'privilege': row.privilege
            })

        return res

    @staticmethod
    def get(rut = ''):
        if rut != '':
            clock_user = ClockUserModel.query.filter_by(rut=rut).first()

            return clock_user
        else:
            clock_users = ClockUserModel.query.all()

            return clock_users

    @staticmethod
    def verifiy(rut = ''):
        clock_user_qty = ClockUserModel.query.filter_by(rut=rut).count()

        if clock_user_qty > 0:
            return 1
        else:
            return 0
        
    @staticmethod
    def get_last_uid():
        clock_user = ClockUserModel.query.filter(ClockUserModel.rut != '15538007').order_by(ClockUserModel.uid.desc()).first()
        result = clock_user.uid + 1

        return result

    @staticmethod
    def check(data):
        quantity = ClockUserModel.query.filter_by(rut=data['rut']).count()

        return quantity

    def store(data):
        rut = Helper.numeric_rut(data['rut'])

        status_id = ClockUser.verifiy(rut)

        if status_id == 0:
            clock_user = ClockUserModel()
            clock_user.uid = data['uid']
            
            clock_user.rut = rut
            upper_string = data['names'] + " " + data['father_lastname']
            upper_string = Helper.upper_string(upper_string)
            clock_user.full_name = upper_string
            clock_user.privilege = data['privilege']
            clock_user.added_date = datetime.now()
            clock_user.updated_date = datetime.now()

            db.session.add(clock_user)
            try:
                db.session.commit()

                return str(data['uid']) + "_" + str(data['rut']) + "_" + upper_string + "_" + str(data['privilege'])
            except Exception as e:
                return 0
        else:
            upper_string = data['names'] + " " + data['father_lastname'] + " " + data['mother_lastname']
            upper_string = Helper.upper_string(upper_string)

            return str(data['uid']) + "_" + str(data['rut']) + "_" + upper_string + "_" + str(data['privilege'])
        
        
 
    @staticmethod
    def update(data):
        clock_user = ClockUserModel.query.filter_by(rut = data['rut']).first()
        clock_user.uid = data['uid']
        clock_user.rut = data['rut']
        clock_user.full_name = data['full_name']
        clock_user.privilege = data['privilege']
        clock_user.updated_date = datetime.now()

        db.session.add(clock_user)
        db.session.commit()

        return str(data['uid']) + "_" + str(data['rut']) + "_" + str(data['full_name']) + "_" + str(data['privilege'])