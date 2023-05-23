from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser
from sqlalchemy import func
from app.turns.turn import Turn
from datetime import datetime
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.mesh_data.mesh_datum import MeshDatum

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
    def get_by_mark_date(rut, date):
        clock_attendance = ClockAttendanceModel.query.filter_by(rut=rut)\
        .filter(ClockAttendanceModel.mark_date == date).first()

        return clock_attendance
    
    @staticmethod
    def validate(turn_id, current_hour, punch):
        if punch == 0:
            turn = Turn.get(turn_id)

            if current_hour > turn.end_entry_time_threshold:
                return 0
            else:
                return 1
        else:
            turn = Turn.get(turn_id)

            if current_hour > turn.end_exit_time_threshold:
                return 0
            else:
                return 1

    @staticmethod
    def checked_attedance(rut, current_date, punch):
        clock_attendance = ClockAttendanceModel.query.filter_by(rut=rut,punch=punch)\
        .filter(func.DATE(ClockAttendanceModel.mark_date) == current_date).count()
        
        if clock_attendance > 0:
            ClockAttendance.update(rut, current_date, punch)

            return 0
        else:
            return 1
        

    @staticmethod
    def store(data):
        mark_date_str = data['mark_date']
        mark_date = datetime.strptime(mark_date_str, '%Y-%m-%d %H:%M:%S')
        format_mark_date = mark_date.strftime("%Y-%m-%d")

        week = MeshDatum.get_week(data['rut'], format_mark_date)

        clock_user = ClockUser.get(data['rut'])
        uid = clock_user.uid

        clock_user = ClockUser.get(data['rut'])

        clock_attendance = ClockAttendanceModel()
        clock_attendance.uid = uid
        clock_attendance.rut = data['rut']
        clock_attendance.punch = data['punch']
        clock_attendance.week_id = week
        clock_attendance.status = data['status']
        clock_attendance.mark_date = data['mark_date']
        clock_attendance.branch_office_id = data['branch_office_id']
        clock_attendance.checked_attendance_id = 0
        db.session.add(clock_attendance)
        db.session.commit()

        return str(data)
    
    @staticmethod
    def special_store(data, mark_date):
        mark_date_str = mark_date
        mark_date = datetime.strptime(mark_date_str, '%Y-%m-%d %H:%M:%S')
        format_mark_date = mark_date.strftime("%Y-%m-%d")

        week = MeshDatum.get_week(data['rut'], format_mark_date)

        clock_user = ClockUser.get(data['rut'])
        uid = clock_user.uid

        employee_labor_datum = EmployeeLaborDatum.get_detail_by_rut(data['rut'])

        clock_attendance = ClockAttendanceModel()
        clock_attendance.uid = uid
        clock_attendance.rut = data['rut']
        clock_attendance.punch = data['punch']
        clock_attendance.week_id = week
        clock_attendance.status = 3
        clock_attendance.checked_attendance_id = 1
        clock_attendance.mark_date = mark_date
        clock_attendance.branch_office_id = employee_labor_datum.branch_office_id
        db.session.add(clock_attendance)
        db.session.commit()

        return str(data)
    
    @staticmethod
    def update(rut, current_date, punch):
        clock_attendances = ClockAttendanceModel.query.filter_by(rut=rut,punch=punch)\
        .filter(func.DATE(ClockAttendanceModel.mark_date) == current_date).all()

        for clock_attendance in clock_attendances:
            update_clock_attendance = ClockAttendanceModel.query.filter_by(id=clock_attendance.id).first()
            update_clock_attendance.checked_attendance_id = 1
            db.session.add(update_clock_attendance)
            db.session.commit()

        return str(1)
    
    @staticmethod
    def delete(id):
        control_clock_no_mark = ClockAttendanceModel.query.filter_by(id=id).first()

        db.session.delete(control_clock_no_mark)
        try:
            db.session.commit()

            return control_clock_no_mark
        except Exception as e:
            return {'msg': 'Data could not be stored'}