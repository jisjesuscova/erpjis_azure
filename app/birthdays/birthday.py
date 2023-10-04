from app.models.models import BirthdayModel
from app import db
from datetime import datetime

class Birthday():
    @staticmethod
    def get(id):
        birthday = BirthdayModel.query.filter_by(id=id).first()

        return birthday
    
    @staticmethod
    def store(data):
        birthday = BirthdayModel()
        birthday.send_rut = data['send_rut']
        birthday.receive_rut = data['receive_rut']
        birthday.message = data['message']
        birthday.added_date = datetime.now()
        birthday.updated_date = datetime.now()

        db.session.add(birthday)
        try:
            db.session.commit()

            return birthday
        except Exception as e:
            return {'msg': 'Data could not be stored'}