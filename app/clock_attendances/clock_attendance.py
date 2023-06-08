from app.models.models import ClockAttendanceModel
from app import db
from app.clock_users.clock_user import ClockUser
from sqlalchemy import func, extract, and_
from app.turns.turn import Turn
from datetime import datetime
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.mesh_data.mesh_datum import MeshDatum
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from app.helpers.helper import Helper
from dateutil.relativedelta import relativedelta

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
    def get_all_with_df(rut, period):
        clock_attendances = ClockAttendanceModel.query.filter(
            ClockAttendanceModel.rut == rut,
            func.date_format(ClockAttendanceModel.mark_date, '%m-%Y') == period
        ).all()

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
                'period': period,
                'hours': str(hours) +"_"+ str(attendance.status),
                'date': date,
                'week_id': attendance.week_id
            })
        
        df = pd.DataFrame(data)

        filtered_df_0 = df[(df['punch'].isin([0, 1]))]

        pivot_table_0 = filtered_df_0.pivot_table(index=['rut', 'date', 'week_id'], columns='punch', values='hours', aggfunc=lambda x: list(x))

        pivot_table_0 = pivot_table_0.rename(columns={0: 'start', 1: 'end'})

        new_df = pd.DataFrame(pivot_table_0.to_records())

        splitted_period = Helper.split(period, '-')

        start_period = str(splitted_period[1]) + "-" + str(splitted_period[0]) + "-01"

        end_period = Helper.get_last_day_of_month(start_period)

        start_period = pd.to_datetime(start_period)

        date_range = pd.date_range(start=start_period, end=end_period, freq='D')

        new_df2 = pd.MultiIndex.from_product([new_df['rut'].unique(), date_range], names=['rut', 'date']).to_frame(index=False)

        merged_df = pd.merge(new_df2, new_df, on=['rut', 'date'], how='left')

        merged_df['status_1'] = merged_df['start'].str[0].str.split('_').str[1]
        merged_df['status_2'] = merged_df['end'].str[0].str.split('_').str[1]

        merged_df['start'] = merged_df['start'].str[0].str.split('_').str[0]
        merged_df['end'] = merged_df['end'].str[0].str.split('_').str[0]

        merged_df['start'] = merged_df['start'].fillna(0)
        merged_df['end'] = merged_df['end'].fillna(0)
        merged_df['status_1'] = merged_df['status_1'].fillna(0)
        merged_df['status_2'] = merged_df['status_2'].fillna(0)
        merged_df['week_id'] = merged_df['week_id'].fillna(0)
        merged_df['week_id'] = merged_df['week_id'].astype(int)

        return merged_df
    
    @staticmethod
    def get_all_with_df_grouped_by_week(df):

        subset = df[['rut', 'week_id', 'total']]

        subset['total'] = pd.to_timedelta(subset['total'])

        # Realizar la suma por el grupo 'week_id'
        grouped_df = subset.groupby(subset.iloc[:, 2]).agg({'total': 'sum'})

        grouped_df['total_seconds'] = grouped_df['total'].dt.total_seconds()

        grouped_df.loc['Total'] = grouped_df['total_seconds'].sum()

        # Calcular los días, horas, minutos y segundos
        grouped_df['days'] = grouped_df['total_seconds'] // (24 * 60 * 60)
        grouped_df['hours'] = (grouped_df['total_seconds'] % (24 * 60 * 60)) // (60 * 60)
        grouped_df['minutes'] = (grouped_df['total_seconds'] % (60 * 60)) // 60
        grouped_df['seconds'] = grouped_df['total_seconds'] % 60

        # Crear el formato HH:MM:SS
        grouped_df['formatted'] = grouped_df.apply(lambda row: f"{int(row['days'] * 24 + row['hours']):02d}:{int(row['minutes']):02d}", axis=1)

        return grouped_df
    
    @staticmethod
    def calculate(df_1, df_2):

        concat = pd.concat([df_1, df_2], axis=1)

        concat.iloc[:, 2] = pd.to_datetime(concat.iloc[:, 2], format='%H:%M:%S', errors='coerce').dt.time
        concat.iloc[:, 3] = pd.to_datetime(concat.iloc[:, 3], format='%H:%M:%S', errors='coerce').dt.time

        concat.iloc[:, 9] = pd.to_datetime(concat.iloc[:, 9], format='%H:%M:%S', errors='coerce').dt.time
        concat.iloc[:, 10] = pd.to_datetime(concat.iloc[:, 10], format='%H:%M:%S', errors='coerce').dt.time

        concat.iloc[:, 9] = concat.iloc[:, 9].fillna(0)
        concat.iloc[:, 10] = concat.iloc[:, 10].fillna(0)

        concat.iloc[:, 2] = concat.iloc[:, 2].astype(str)
        concat[['hour', 'minute', 'second']] = concat.iloc[:, 2].str.split(':', expand=True)
        concat['hour1'] = concat['hour'].astype(int)
        concat['minute1'] = concat['minute'].astype(int)
        concat['second1'] = concat['second'].astype(int)

        concat['total_seconds1'] = concat['hour1'] * 3600 + concat['minute1'] * 60 + concat['second1']

        concat.iloc[:, 3] = concat.iloc[:, 3].astype(str)
        concat[['hour', 'minute', 'second']] = concat.iloc[:, 3].str.split(':', expand=True)
        concat['hour2'] = concat['hour'].astype(int)
        concat['minute2'] = concat['minute'].astype(int)
        concat['second2'] = concat['second'].astype(int)

        concat['total_seconds2'] = concat['hour2'] * 3600 + concat['minute2'] * 60 + concat['second2']

        concat.iloc[:, 9] = concat.iloc[:, 9].astype(str)
        concat[['hour', 'minute', 'second']] = concat.iloc[:, 9].str.split(':', expand=True)

        concat['hour3'] = concat['hour'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['minute3'] = concat['minute'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['second3'] = concat['second'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')

        concat['total_seconds3'] = concat['hour3'] * 3600 + concat['minute3'] * 60 + concat['second3']

        concat.iloc[:, 10] = concat.iloc[:, 10].astype(str)
        concat[['hour', 'minute', 'second']] = concat.iloc[:, 10].str.split(':', expand=True)
        concat['hour4'] = concat['hour'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['minute4'] = concat['minute'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['second4'] = concat['second'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')

        concat['total_seconds4'] = concat['hour4'] * 3600 + concat['minute4'] * 60 + concat['second4']

        concat['total_seconds1'] = concat['total_seconds1'].fillna(0)
        concat['total_seconds2'] = concat['total_seconds2'].fillna(0)
        concat['total_seconds3'] = concat['total_seconds3'].fillna(0)
        concat['total_seconds4'] = concat['total_seconds4'].fillna(0)

        mask = concat['total_seconds3'].ne(0)
        concat.loc[mask, 'subtotal1'] = concat.loc[mask, 'total_seconds1'] - concat.loc[mask, 'total_seconds3']

        mask = concat['total_seconds4'].ne(0)
        concat.loc[mask, 'subtotal2'] = concat.loc[mask, 'total_seconds2'] - concat.loc[mask, 'total_seconds4']

        concat['total'] = concat['subtotal1'] - concat['subtotal2']

        concat['total'] = pd.to_numeric(concat['total'], errors='coerce')

        concat['total'] = concat['total'] .fillna(0)

        concat['total'] = concat['total'].apply(lambda x: f"{x//3600:02d}:{(x%3600)//60:02d}:{(x%3600)//60:02d}")

        return concat
    
    @staticmethod
    def calculate_grouped_by_week(df_1, df_2):

        data = []

        i = 1

        for index, row in df_1.iterrows():
            if row['week'] != 'Total':
                data.append({
                    'week_1': i,
                    'hours_1': row['masked_total_hours']
                })

            i = i + 1

        df_1 = pd.DataFrame(data)

        data = []

        i = 1

        for index, row in df_2.iterrows():
            if i < 6:
                data.append({
                    'week_2': i,
                    'hours_2': row['formatted']
                })

            i = i + 1
        
        df_2 = pd.DataFrame(data)

        concat = pd.concat([df_1, df_2], axis=1)

        # Convertir las columnas a segundos
        concat['total_in_seconds_1'] = pd.to_timedelta(concat['hours_1'] + ":00").dt.total_seconds()
        concat['total_in_seconds_2'] = pd.to_timedelta(concat['hours_2'] + ":00").dt.total_seconds()

        concat['total'] = concat['total_in_seconds_1'] - concat['total_in_seconds_2']

        concat.loc[concat['total'] > concat['total_in_seconds_1'], 'total'] = concat['total_in_seconds_1']

        concat.loc['Total'] = concat['total'].sum()

        # Calcular los días, horas, minutos y segundos
        concat['days'] = concat['total'] // (24 * 60 * 60)
        concat['hours'] = (concat['total'] % (24 * 60 * 60)) // (60 * 60)
        concat['minutes'] = (concat['total'] % (60 * 60)) // 60
        concat['seconds'] = concat['total'] % 60

        # Crear el formato HH:MM:SS
        concat['formatted'] = concat.apply(lambda row: f"{int(row['days'] * 24 + row['hours']):02d}:{int(row['minutes']):02d}", axis=1)

        return concat
    
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