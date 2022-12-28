from app.models.models import ClockAttendanceModel
from app import db

class ClockAttendance():
    def store(data):
        clock_attendance = ClockAttendanceModel()
        clock_attendance.uid = data['uid']
        clock_attendance.rut = data['rut']
        clock_attendance.punch = data['punch']
        clock_attendance.status = data['status']
        clock_attendance.mark_date = data['mark_date']

        db.session.add(clock_attendance)
        db.session.commit()
        
        return clock_attendance
