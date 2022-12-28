from app.models.models import ControlClockUserModel
from app import db
import datetime

def ControlClockUser():
    @staticmethod
    def store(data):
        control_clock_user = ControlClockUserModel()
        control_clock_user.rut = data['rut']
        control_clock_user.added_date = datetime.now()

        db.session.add(control_clock_user)
        db.session.commit()
        
        return control_clock_user