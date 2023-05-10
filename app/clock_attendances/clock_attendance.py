from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser

class ClockAttendance():
    def store(data):

        
        return str(1) + "_" + str(data['rut']) + "_" + str(data['punch']) + "_" + str(data['status']) + "_" + str(data['mark_date']) + "_" + str(data['branch_office_id'])