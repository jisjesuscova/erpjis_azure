from app.models.models import AttendanceModel
from app import db

class Attendance():
    @staticmethod
    def store(data):
        attendance = AttendanceModel()
        attendance.rut = data['rut']
        attendance.status = data['status']
        attendance.push = data['push']
        attendance.added_date = data['added_date']

        db.session.add(attendance)
        db.session.commit()
        
        return 1