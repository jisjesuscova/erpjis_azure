from app.models.models import ControlClockFingerModel
from app import db
import datetime

def ControlClockFinger():
    @staticmethod
    def store(data):
        control_clock_finger = ControlClockFingerModel()
        control_clock_finger.rut = data['rut']
        control_clock_finger.finger = data['finger']
        control_clock_finger.added_date = datetime.now()

        db.session.add(control_clock_finger)
        db.session.commit()
        
        return control_clock_finger