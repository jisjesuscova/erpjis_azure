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

        # Obtener todas las fechas en el rango deseado
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
    def calculate(df_1, df_2):
        # Concatenar los dataframes df_1 y df_2
        concat = pd.concat([df_1, df_2], axis=1)

        # Extraer los valores del array en las columnas "start2" y "end2"
        concat.iloc[:, 8] = concat.iloc[:, 8].str[0]
        concat.iloc[:, 9] = concat.iloc[:, 9].str[0]

        # Convertir las columnas "start1" y "end1" a formato de fecha y hora
        concat.iloc[:, 2] = pd.to_datetime(concat.iloc[:, 2], format='%H:%M:%S', errors='coerce')
        concat.iloc[:, 3] = pd.to_datetime(concat.iloc[:, 3], format='%H:%M:%S', errors='coerce')

        # Convertir las columnas "start2" y "end2" a formato de fecha y hora
        concat.iloc[:, 8] = pd.to_datetime(concat.iloc[:, 8], format='%H:%M:%S', errors='coerce')
        concat.iloc[:, 9] = pd.to_datetime(concat.iloc[:, 9], format='%H:%M:%S', errors='coerce')

        # Calcular la diferencia condicional entre las columnas "end1" y "end2"
        concat['end_total'] = np.where(concat.iloc[:, 2] > concat.iloc[:, 8], 
                                        concat.iloc[:, 2] - concat.iloc[:, 8], 
                                        concat.iloc[:, 8] - concat.iloc[:, 2])

        # Calcular la diferencia condicional entre las columnas "start1" y "start2"
        concat['start_total'] = np.where(concat.iloc[:, 9] > concat.iloc[:, 3], 
                                        concat.iloc[:, 9] - concat.iloc[:, 3], 
                                        concat.iloc[:, 3] - concat.iloc[:, 9])

        # Convertir las diferencias a timedelta
        concat['end_total'] = pd.to_timedelta(concat['end_total'], unit='s')
        concat['start_total'] = pd.to_timedelta(concat['start_total'], unit='s')

        # Convertir los resultados a formato de tiempo (total de segundos)
        concat['end_total'] = concat['end_total'].dt.total_seconds().fillna(0).astype(int)
        concat['start_total'] = concat['start_total'].dt.total_seconds().fillna(0).astype(int)

        # Convertir los resultados a formato de tiempo (datetime)
        concat['end_total'] = pd.to_datetime(concat['end_total'], unit='s')
        concat['start_total'] = pd.to_datetime(concat['start_total'], unit='s')

        # Extraer solo la parte de tiempo (hora, minuto, segundo) de las columnas 'end_total' y 'start_total'
        concat['start_total'] = concat['start_total'].dt.time
        concat['end_total'] = concat['end_total'].dt.time

        # Convertir las cadenas de tiempo a objetos datetime
        concat['start_total'] = pd.to_datetime(concat['start_total'], format='%H:%M:%S')
        concat['end_total'] = pd.to_datetime(concat['end_total'], format='%H:%M:%S')

        # Calcular la resta entre las columnas 'start_total' y 'end_total'
        concat['resta_total'] = concat['end_total'] - concat['start_total']
        
        # Convertir la diferencia en segundos
        concat['resta_total'] = concat['resta_total'].dt.total_seconds()
        

        # Convertir los segundos de nuevo a tiempo (hora, minuto, segundo)
        concat['resta_total'] = pd.to_timedelta(concat['resta_total'], unit='s')
        # Convertir la columna 'resta_total' a tipo texto
        concat['resta_total'] = concat['resta_total'].astype(str)

        # Utilizar str.slice() para obtener los primeros cinco caracteres de la columna 'resta_total'
        concat['resta_total'] = concat['resta_total'].str.slice(6, 16)

        concat.rename(columns={'end_total': 'start_total', 'start_total': 'end_total'}, inplace=True)

        return concat
    
    @staticmethod
    def get_all_with_df_merged(df_1, df_2):
        merged_df = df_1.merge(df_2, on=['rut', 'date'], how='left')

        data_dict = merged_df.to_dict(orient='records')

        return data_dict
    
    @staticmethod
    def get_all_with_df_merged_total(df1, df2):
        grouped_df1 = df1.groupby('date')
        grouped_df2 = df2.groupby('date')
        agg_df1 = grouped_df1['start', 'end'].first()
        agg_df2 = grouped_df2['entrada', 'salida'].first()
        final_df = pd.concat([agg_df1, agg_df2], axis='columns')

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