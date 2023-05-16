from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser
from sqlalchemy import func
from app.turns.turn import Turn
from datetime import datetime

class ClockAttendance():
    @staticmethod
    def get(rut, date, punch):
        if punch == 0:
            clock_attendance = ClockAttendanceModel.query.filter_by(rut=rut, punch=punch)\
            .order_by(ClockAttendanceModel.mark_date.asc())\
            .filter(func.DATE(ClockAttendanceModel.mark_date) == date).first()
        else:
            clock_attendance = ClockAttendanceModel.query.filter_by(rut=rut, punch=punch)\
            .order_by(ClockAttendanceModel.mark_date.desc())\
            .filter(func.DATE(ClockAttendanceModel.mark_date) == date).first()

        return clock_attendance
    
    @staticmethod
    def validate(turn_id, mark_date, punch):
        if punch == 0:
            mark_time = datetime.strptime(str(mark_date), '%Y-%m-%d %H:%M:%S').time()

            turn = Turn.get(turn_id)

            end_time = datetime.strptime(turn.end_entry_time_threshold, '%H:%M:%S').time()

            if mark_time <= end_time:
                return 1
            else:
                return 0
        else:
            mark_time = datetime.strptime(str(mark_date), '%Y-%m-%d %H:%M:%S').time()

            turn = Turn.get(turn_id)

            end_time = datetime.strptime(turn.end_entry_time_threshold, '%H:%M:%S').time()

            if mark_time >= end_time:
                return 1
            else:
                return 0
        
    
    @staticmethod
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
    

    @staticmethod
    def update(id):
        clock_attendance = ClockAttendanceModel.query.filter_by(id=id).first()
        clock_attendance.check_status_id = 1
        db.session.update(clock_attendance)
        db.session.commit()

        return str(1)