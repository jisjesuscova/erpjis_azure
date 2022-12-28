from app.models.models import ClockAttendanceModel
from app import db

class ClockAttendance():
    def store(data):
        return str(data['uid']) + "_" + str(data['rut']) + "_" + str(data['punch']) + "_" + str(data['status']) + "_" + str(data['mark_date'])
