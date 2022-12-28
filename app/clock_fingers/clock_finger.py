from app.models.models import ClockFingerModel
from app import db
from datetime import datetime

class ClockFinger():
    def store(data):
        clock_finger = ClockFingerModel()
        clock_finger.uid = data['uid']
        clock_finger.template = data['template']
        clock_finger.added_date = datetime.now()
        clock_finger.updated_date = datetime.now()

        db.session.add(clock_finger)
        db.session.commit()
        
        return str(data['uid']) + "_" + str(data['template'])
 