from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser

class ClockAttendance():
    def store(data):
        print(data['rut'])
        clock_user = ClockUser.get(data['rut'])

        clock_attendance = ClockAttendanceModel()
        clock_attendance.uid = clock_user.uid
        clock_attendance.rut = data['rut']
        clock_attendance.punch = data['punch']
        clock_attendance.status = data['status']
        clock_attendance.mark_date = data['mark_date']
        clock_attendance.branch_office_id = data['branch_office_id']

        db.session.add(clock_attendance)
        db.session.commit()
        
        return str(clock_user.uid) + "_" + str(data['rut']) + "_" + str(data['punch']) + "_" + str(data['status']) + "_" + str(data['mark_date']) + "_" + str(data['branch_office_id'])