from app.models.models import ClockModel
from app import db
from datetime import datetime

class Clock():
    def store(data):
        clock = ClockModel()
        clock.branch_office_id = data['branch_office_id']
        clock.ip = data['ip']
        clock.sn = data['sn']
        clock.added_date = datetime.now()
        clock.updated_date = datetime.now()

        db.session.add(clock)
        db.session.commit()
        
        return str(data['branch_office_id']) + "_" + str(data['ip']) + "_" + str(data['sn'])
 