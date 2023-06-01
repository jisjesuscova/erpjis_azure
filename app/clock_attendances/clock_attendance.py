from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser
from sqlalchemy import func, extract
from app.turns.turn import Turn
from datetime import datetime
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.mesh_data.mesh_datum import MeshDatum
import pandas as pd


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

        week = MeshDatum.get_week(format_mark_date)

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
    def get_all_with_df_marked(rut, period):
        clock_attendances = ClockAttendanceModel.query.filter_by(rut=rut).all()

        data = []
        for attendance in clock_attendances:
            year = attendance.mark_date.year
            month = attendance.mark_date.month
            period = f"{month:02d}-{year}"

            hours = attendance.mark_date.strftime('%H:%M:%S')

            date = attendance.mark_date.strftime('%Y-%m-%d')
            # Convertir la fecha a tipo datetime
            date = pd.to_datetime(date)

            data.append({
                'rut': attendance.rut,
                'mark_date': attendance.mark_date,
                'punch': attendance.punch,
                'status': attendance.status,
                'period': period,
                'hours': hours,
                'date': date
            })

        df = pd.DataFrame(data)

        # Filtrar por punch igual a 0 o 1
        filtered_df = df[(df['punch'].isin([0, 1])) & (df['status'].isin([0, 1]))]
        filtered_df = filtered_df.assign(status=1)

        # Crear el pivot table
        pivot_table = filtered_df.pivot_table(index=['date', 'rut', 'status'], columns='punch', values='hours', aggfunc='first')

        # Reemplazar NaN por 0
        pivot_table = pivot_table.fillna(0)

        return pivot_table
    
    @staticmethod
    def get_all_with_df_inserted(rut, period):
        clock_attendances = ClockAttendanceModel.query.filter_by(rut=rut).all()

        data = []
        for attendance in clock_attendances:
            year = attendance.mark_date.year
            month = attendance.mark_date.month
            period = f"{month:02d}-{year}"

            hours = attendance.mark_date.strftime('%H:%M:%S')

            date = attendance.mark_date.strftime('%Y-%m-%d')
            # Convertir la fecha a tipo datetime
            date = pd.to_datetime(date)

            data.append({
                'rut': attendance.rut,
                'mark_date': attendance.mark_date,
                'punch': attendance.punch,
                'status': attendance.status,
                'period': period,
                'hours': hours,
                'date': date
            })

        df = pd.DataFrame(data)

        # Filtrar por punch igual a 0 o 1
        filtered_df = df[(df['punch'].isin([0, 1])) & (df['status'].isin([2]))]
        filtered_df = filtered_df.assign(status=2)

        # Crear el pivot table
        pivot_table = filtered_df.pivot_table(index=['date', 'rut', 'status'], columns='punch', values='hours', aggfunc='first')

        # Reemplazar NaN por 0
        pivot_table = pivot_table.fillna(0)

        return pivot_table
    
    @staticmethod
    def get_all_with_df_merged(df_1, df_2):
        merged_df = df_1.merge(df_2, on=['rut', 'date', 'status'], how='outer')
        merged_df['entrada'] = merged_df['0_x'].combine_first(merged_df['0_y'])
        merged_df['salida'] = merged_df['1_x'].combine_first(merged_df['1_y'])
        merged_df = merged_df.drop(['0_x', '0_y', '1_x', '1_y'], axis=1)

        return merged_df
    
    @staticmethod
    def get_all_with_df_merged_total(df1, df2):
        grouped_df1 = df1.groupby('date')
        grouped_df2 = df2.groupby('date')
        agg_df1 = grouped_df1['start', 'end'].first()
        agg_df2 = grouped_df2['entrada', 'salida'].first()
        final_df = pd.concat([agg_df1, agg_df2], axis='columns')
        print(final_df)
        exit()
        return final_df
    
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