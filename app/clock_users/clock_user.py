from app.models.models import ClockUserModel
from app import db
from datetime import datetime

class ClockUser():
    def store(data):
        clock_user = ClockUserModel()
        clock_user.uid = data['uid']
        clock_user.rut = data['rut']
        clock_user.full_name = data['full_name']
        clock_user.privilege = data['privilege']
        clock_user.added_date = datetime.now()
        clock_user.updated_date = datetime.now()

        db.session.add(clock_user)
        db.session.commit()
        
        return str(data['uid']) + "_" + str(data['rut']) + "_" + str(data['full_name']) + "_" + str(data['privilege'])
 