from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser

class ClockAttendance():
    def store(data):
        print(data['rut'])
        
        return str(data)