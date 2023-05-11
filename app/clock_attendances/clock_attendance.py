from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser

class ClockAttendance():
    def store(data):
        clock_user = ClockUser.get(data['rut'])
        uid = clock_user.uid

        clock_attendance = ClockAttendanceModel()
        clock_attendance.uid = uid
        clock_attendance.rut = data['rut']
        clock_attendance.punch = data['punch']
        clock_attendance.status = data['status']
        clock_attendance.mark_date = data['mark_date']
        clock_attendance.branch_office_id = data['branch_office_id']
        db.session.add(clock_attendance)
        db.session.commit()

        return str(data)