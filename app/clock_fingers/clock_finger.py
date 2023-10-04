from app.models.models import ClockFingerModel, ClockUserModel
from app import db
from datetime import datetime

class ClockFinger():
    @staticmethod
    def to_json(data):
        res = []

        for row in data:
            res.append({
                'uid': row.uid,
                'template': row.template
            })

        return res

    @staticmethod
    def get():
        clock_fingers = db.session.query(ClockFingerModel).join(ClockUserModel, ClockFingerModel.uid == ClockUserModel.uid).all()

        return clock_fingers

    @staticmethod
    def check(data):
        quantity = ClockFingerModel.query.filter_by(uid=data['uid']).count()

        return quantity

    def store(data):
        clock_finger = ClockFingerModel()
        clock_finger.uid = data['uid']
        clock_finger.template = data['template']
        clock_finger.added_date = datetime.now()
        clock_finger.updated_date = datetime.now()

        db.session.add(clock_finger)
        db.session.commit()
        
        return str(data['uid']) + "_" + str(data['template'])
    
    @staticmethod
    def update(data):
        clock_finger = ClockFingerModel.query.filter_by(uid = data['uid']).first()
        clock_finger.uid = data['uid']
        clock_finger.template = data['template']
        clock_finger.updated_date = datetime.now()

        db.session.add(clock_finger)
        db.session.commit()

        return str(data['uid']) + "_" + str(data['template'])