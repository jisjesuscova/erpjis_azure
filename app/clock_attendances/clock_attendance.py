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
                'status': attendance.status,
                'period': period,
                'hours': hours,
                'date': date
            })

        df = pd.DataFrame(data)

        filtered_df_0 = df[(df['punch'].isin([0, 1])) & (df['status'].isin([0]))]

        pivot_table_0 = filtered_df_0.pivot_table(index=['rut', 'date', 'status'], columns='punch', values='hours', aggfunc='first')

        pivot_table_0 = pivot_table_0.rename(columns={0: 'start', 1: 'end'})

        new_df_0 = pd.DataFrame(pivot_table_0.to_records())

        filtered_df_1 = df[(df['punch'].isin([0, 1])) & (df['status'].isin([1]))]

        pivot_table_1 = filtered_df_1.pivot_table(index=['rut', 'date', 'status'], columns='punch', values='hours', aggfunc='first')

        pivot_table_1 = pivot_table_1.rename(columns={0: 'start', 1: 'end'})

        new_df_1 = pd.DataFrame(pivot_table_1.to_records())

        filtered_df_2 = df[(df['punch'].isin([0, 1])) & (df['status'].isin([2]))]

        pivot_table_2 = filtered_df_2.pivot_table(index=['rut', 'date', 'status'], columns='punch', values='hours', aggfunc='first')

        pivot_table_2 = pivot_table_2.rename(columns={0: 'start', 1: 'end'})

        new_df_2 = pd.DataFrame(pivot_table_2.to_records())
        
        concat = pd.concat([new_df_0, new_df_1, new_df_2], axis=0)
        concat['start'] = concat['start'].fillna(0)
        concat['end'] = concat['end'].fillna(0)

        grouped_df = concat.groupby(['rut', 'date']).agg(list).reset_index()

        # Obtener todas las fechas en el rango deseado. ACA HAY QUE CAMBIAR EL RANGO DE FECHAS QUE VENGA POR PERIOD
        date_range = pd.date_range(start='2023-05-01', end='2023-05-31', freq='D')

        # Crear un nuevo DataFrame con todas las combinaciones de 'rut' y 'date'
        new_df = pd.MultiIndex.from_product([grouped_df['rut'].unique(), date_range], names=['rut', 'date']).to_frame(index=False)

        # Realizar un merge entre el nuevo DataFrame y grouped_df para llenar los valores faltantes
        merged_df = pd.merge(new_df, grouped_df, on=['rut', 'date'], how='left')

        # Rellenar los valores NaN con 0 en las columnas 'start' y 'end'
        merged_df['status'] = merged_df['status'].fillna(0)
        merged_df['start'] = merged_df['start'].fillna(0)
        merged_df['end'] = merged_df['end'].fillna(0)

        # Ordenar el DataFrame por 'rut' y 'date'
        merged_df = merged_df.sort_values(['rut', 'date']).reset_index(drop=True)

        return merged_df
    
    @staticmethod
    def get_all_with_df_grouped_by_week(rut, period):
        clock_attendances = ClockAttendanceModel.query.filter(
            ClockAttendanceModel.rut == rut,
            func.date_format(ClockAttendanceModel.mark_date, '%m-%Y') == period,
            ClockAttendanceModel.punch.in_([0, 1])
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
                'status': attendance.status,
                'punch': attendance.punch,
                'period': period,
                'hours': hours,
                'date': date,
                'week': attendance.week_id
            })

        df = pd.DataFrame(data)
        

        filtered_df_0 = df[(df['punch'].isin([0, 1])) & (df['status'].isin([0]))]

        pivot_table_0 = filtered_df_0.pivot_table(index=['rut', 'mark_date', 'week'], columns='punch', values='hours', aggfunc=lambda x: list(x))

        pivot_table_0 = pivot_table_0.rename(columns={0: 'start', 1: 'end'})

        new_df_0 = pd.DataFrame(pivot_table_0.to_records())

        
        filtered_df_1 = df[(df['punch'].isin([0, 1])) & (df['status'].isin([1]))]

        pivot_table_1 = filtered_df_1.pivot_table(index=['rut', 'mark_date', 'week'], columns='punch', values='hours', aggfunc=lambda x: list(x))

        pivot_table_1 = pivot_table_1.rename(columns={0: 'start', 1: 'end'})

        new_df_1 = pd.DataFrame(pivot_table_1.to_records())


        filtered_df_2 = df[(df['punch'].isin([0, 1])) & (df['status'].isin([2]))]

        pivot_table_2 = filtered_df_2.pivot_table(index=['rut', 'mark_date', 'week'], columns='punch', values='hours', aggfunc=lambda x: list(x))

        pivot_table_2 = pivot_table_2.rename(columns={0: 'start', 1: 'end'})

        new_df_2 = pd.DataFrame(pivot_table_2.to_records())

        
        concat = pd.concat([new_df_0, new_df_1, new_df_2], axis=0)

        concat['start'] = concat['start'].fillna(0)
        concat['end'] = concat['end'].fillna(0)
        concat['mark_date'] = pd.to_datetime(concat['mark_date'])

        concat['mark_date'] = pd.to_datetime(concat['mark_date'])

        concat['mark_date'] = concat['mark_date'].dt.strftime('%Y-%m-%d')
        grouped = concat.groupby(['rut', 'mark_date', 'week']).agg({'start': list, 'end': list}).reset_index()
        counted = grouped.groupby(['week']).count()

        df = pd.DataFrame(grouped)

        df['start'] = df['start'].apply(lambda x: x[0][0] if isinstance(x, list) and len(x) > 0 and len(x[0]) > 0 else 0)
        df['end'] = df['end'].apply(lambda x: x[1][0] if isinstance(x, list) and len(x) > 1 and len(x[1]) > 0 else 0)

        df.iloc[:, 3] = pd.to_datetime(df.iloc[:, 3], format='%H:%M:%S', errors='coerce')
        df.iloc[:, 4] = pd.to_datetime(df.iloc[:, 4], format='%H:%M:%S', errors='coerce')

        df['total'] = np.where(df.iloc[:, 3] > df.iloc[:, 4], 
                                        df.iloc[:, 3] - df.iloc[:, 4], 
                                        df.iloc[:, 4] - df.iloc[:, 3])

        df['numeric_total'] = np.where(df.iloc[:, 3] > df.iloc[:, 4], 
                                        df.iloc[:, 3] - df.iloc[:, 4], 
                                        df.iloc[:, 4] - df.iloc[:, 3])
        
        df['start'] = df['start'].fillna(pd.Timedelta(seconds=0))
        df['end'] = df['end'].fillna(pd.Timedelta(seconds=0))
        df['total'] = df['total'].fillna(pd.Timedelta(seconds=0))

        grouped = df.groupby(['rut', 'week']).agg({'total': 'sum'}).reset_index()

        merged_df = pd.merge(grouped, counted, on=['week'], how='left')

        df = pd.DataFrame(merged_df)

        # Obtener todos los valores únicos de la columna "week"
        unique_weeks = df['week'].unique()

        # Crear un rango de valores del 1 al 5
        all_weeks = range(1, 6)

        # Obtener los valores faltantes en la columna "week"
        missing_weeks = set(all_weeks) - set(unique_weeks)

        # Crear filas con los valores faltantes en la columna "week"
        missing_rows = pd.DataFrame({'week': list(missing_weeks)})
        missing_rows['rut'] = np.nan
        missing_rows['total'] = pd.Timedelta(seconds=0)

        # Concatenar el DataFrame original con las filas faltantes
        df = pd.concat([df, missing_rows])

        # Ordenar el DataFrame por la columna "week"
        df = df.sort_values('week')

        # Restablecer el índice del DataFrame
        df = df.reset_index(drop=True)

        df['mark_date'] = df['mark_date'].fillna(0)

        df['mark_date'] = df['mark_date'].astype(str)

        df['mark_date'] = df['mark_date'].str.slice(0, 1)

        df['mark_date'] = pd.to_numeric(df['mark_date'], errors='coerce')

        df['total'] = pd.to_timedelta(df['total'])

        df.loc['Total'] = df[['total', 'mark_date']].sum()

        df['week'] = df['week'].fillna('Total')

        df['total'] = df['total'].astype(str)

        df['total'] = df['total'].str.slice(6, 12)

        return df
    
    @staticmethod
    def calculate(df_1, df_2):
        concat = pd.concat([df_1, df_2], axis=1)

        concat.iloc[:, 8] = concat.iloc[:, 8].str[0]
        concat.iloc[:, 9] = concat.iloc[:, 9].str[0]

        concat.iloc[:, 2] = pd.to_datetime(concat.iloc[:, 2], format='%H:%M:%S', errors='coerce').dt.time
        concat.iloc[:, 3] = pd.to_datetime(concat.iloc[:, 3], format='%H:%M:%S', errors='coerce').dt.time

        concat.iloc[:, 8] = pd.to_datetime(concat.iloc[:, 8], format='%H:%M:%S', errors='coerce').dt.time
        concat.iloc[:, 9] = pd.to_datetime(concat.iloc[:, 9], format='%H:%M:%S', errors='coerce').dt.time

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

        print(concat)
        exit()

        concat['end_total'] = pd.to_timedelta(concat['end_total'], unit='s')
        concat['start_total'] = pd.to_timedelta(concat['start_total'], unit='s')

        concat['end_total'] = concat['end_total'].dt.total_seconds().fillna(0).astype(int)
        concat['start_total'] = concat['start_total'].dt.total_seconds().fillna(0).astype(int)

        concat['end_total'] = pd.to_datetime(concat['end_total'], unit='s')
        concat['start_total'] = pd.to_datetime(concat['start_total'], unit='s')

        concat['start_total'] = concat['start_total'].dt.time
        concat['end_total'] = concat['end_total'].dt.time

        concat['start_total'] = pd.to_datetime(concat['start_total'], format='%H:%M:%S')
        concat['end_total'] = pd.to_datetime(concat['end_total'], format='%H:%M:%S')

        concat['resta_total'] = concat['end_total'] - concat['start_total']
        
        concat['resta_total'] = concat['resta_total'].dt.total_seconds()
        
        concat['resta_total'] = pd.to_timedelta(concat['resta_total'], unit='s')

        concat['resta_total'] = concat['resta_total'].astype(str)

        concat['resta_total'] = concat['resta_total'].str.slice(6, 16)

        concat.rename(columns={'end_total': 'start_total', 'start_total': 'end_total'}, inplace=True)

        return concat
    
    @staticmethod
    def calculate_grouped_by_week(df_1, df_2):
        data = []

        for index, row in df_1.iterrows():
            data.append({
                'rut': row['rut'],
                'date': row['date'],
                'start_1': row['start'],
                'end_1': row['end'],
                'week_id': row['week_id']
            })

        df_1 = pd.DataFrame(data)
    
        data = []

        for index, row in df_2.iterrows():
            if isinstance(row['start'], list):
                for item in row['start']:
                    if item != 0:
                        start_value = item
            else:
                start_value = row['start']

            
            if isinstance(row['end'], list):
                for item in row['end']:
                    if item != 0:
                        end_value = item
            else:
                end_value = row['end']
            
            data.append({
                'rut': row['rut'],
                'date': row['date'],
                'start_2': start_value,
                'end_2': end_value
            })

        df_2 = pd.DataFrame(data)

        df_2['start_2'] = df_2['start_2'].fillna(0)
        df_2['end_2'] = df_2['end_2'].fillna(0)
 
        concat = pd.concat([df_1, df_2], axis=1)

        concat.iloc[:, 2] = pd.to_datetime(concat.iloc[:, 2], format='%H:%M:%S', errors='coerce').dt.time
        concat.iloc[:, 3] = pd.to_datetime(concat.iloc[:, 3], format='%H:%M:%S', errors='coerce').dt.time

        concat.iloc[:, 7] = pd.to_datetime(concat.iloc[:, 7], format='%H:%M:%S', errors='coerce').dt.time
        concat.iloc[:, 8] = pd.to_datetime(concat.iloc[:, 8], format='%H:%M:%S', errors='coerce').dt.time

        concat.iloc[:, 7] = concat.iloc[:, 7].fillna(0)
        concat.iloc[:, 8] = concat.iloc[:, 8].fillna(0)

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

        concat.iloc[:, 7] = concat.iloc[:, 7].astype(str)
        concat[['hour', 'minute', 'second']] = concat.iloc[:, 7].str.split(':', expand=True)

        concat['hour3'] = concat['hour'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['minute3'] = concat['minute'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['second3'] = concat['second'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')

        concat['total_seconds3'] = concat['hour3'] * 3600 + concat['minute3'] * 60 + concat['second3']

        concat.iloc[:, 8] = concat.iloc[:, 8].astype(str)
        concat[['hour', 'minute', 'second']] = concat.iloc[:, 8].str.split(':', expand=True)
        concat['hour4'] = concat['hour'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['minute4'] = concat['minute'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')
        concat['second4'] = concat['second'].apply(lambda x: int(x) if pd.notnull(x) else np.nan).astype('Int64')

        concat['total_seconds4'] = concat['hour4'] * 3600 + concat['minute4'] * 60 + concat['second4']

        concat['total_seconds1'] = concat['total_seconds1'] .fillna(0)
        concat['total_seconds2'] = concat['total_seconds2'] .fillna(0)
        concat['total_seconds3'] = concat['total_seconds3'] .fillna(0)
        concat['total_seconds4'] = concat['total_seconds4'] .fillna(0)
        
        mask = concat['total_seconds3'].ne(0)
        concat.loc[mask, 'subtotal1'] = concat.loc[mask, 'total_seconds1'] - concat.loc[mask, 'total_seconds3']

        mask = concat['total_seconds4'].ne(0)
        concat.loc[mask, 'subtotal2'] = concat.loc[mask, 'total_seconds2'] - concat.loc[mask, 'total_seconds4']
        
        concat['total'] = concat['subtotal1'] - concat['subtotal2']

        concat['total'] = pd.to_numeric(concat['total'], errors='coerce')

        concat['total'] = concat['total'] .fillna(0)
        
        grouped_df = concat.groupby(['week_id']).agg(list).reset_index()
        grouped_df.loc['Total'] = grouped_df[['total']].sum()
        grouped_df['total_sum'] = grouped_df['total'].apply(sum)

        grouped_df['total_sum'] = pd.to_numeric(grouped_df['total_sum'], errors='coerce')
        grouped_df['total_sum'] = grouped_df['total_sum'] .fillna(0)

        grouped_df['total_sum'] = grouped_df['total_sum'].apply(lambda x: f"{x//3600:02d}:{(x%3600)//60:02d}")
        
        subset = grouped_df[['rut', 'date', 'week_id', 'total_sum']]

        return subset
    
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