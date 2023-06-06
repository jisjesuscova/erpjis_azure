from flask import request
from app import db
from datetime import datetime, timedelta
from app.models.models import MeshDatumModel, UserModel, TurnModel
from app.employees_turns.employee_turn import EmployeeTurn
from app.turns.turn import Turn
from app.helpers.helper import Helper
from app.pre_employee_turns.pre_employee_turn import PreEmployeeTurn
import pandas as pd
import calendar
import locale
from unidecode import unidecode
from sqlalchemy import literal, func

class MeshDatum():
    @staticmethod
    def get(week = ''):
        if week != '':
            mesh_data = MeshDatumModel.query.filter_by(week=week).all()
        else:
            now = datetime.now()
            current_date = now.strftime('%Y-%m-%d')

            mesh_data = MeshDatumModel.query.filter_by(date=current_date).all()

        return mesh_data
    
    @staticmethod
    def get_all_with_df(rut, period):
        mesh_data = MeshDatumModel.query \
            .filter(MeshDatumModel.rut == rut, MeshDatumModel.period == period) \
            .add_columns(MeshDatumModel.rut, MeshDatumModel.week, MeshDatumModel.date, MeshDatumModel.start, MeshDatumModel.end, MeshDatumModel.period, literal(4).label('status')) \
            .all()

        # Configurar el idioma en español
        locale.setlocale(locale.LC_TIME, 'es_ES.utf-8')

        data = []
        for datum in mesh_data:
            # Convertir la fecha a tipo datetime
            date = pd.to_datetime(datum.date)

            # Obtener el nombre del día de la semana en español y capitalizar la primera letra
            day_of_week = pd.to_datetime(datum.date).strftime('%A').capitalize()

            day_of_week = unidecode(day_of_week)

            if day_of_week == "Mia(c)rcoles":
                day_of_week = "Miércoles"
            elif day_of_week == "Sa!bado":
                day_of_week = "Sábado"
            else:
                day_of_week = day_of_week

            data.append({
                'rut': datum.rut,
                'date': date,
                'start': datum.start,
                'end': datum.end,
                'day_of_week': day_of_week,
                'week_id': datum.week
            })

        df = pd.DataFrame(data)

        return df

    @staticmethod
    def get_all_with_df_grouped_by_week(rut, period):
        mesh_data = MeshDatumModel.query \
            .join(TurnModel, MeshDatumModel.turn_id == TurnModel.id) \
            .with_entities(
                MeshDatumModel.rut,
                MeshDatumModel.week,
                MeshDatumModel.period,
                func.sum(MeshDatumModel.total_hours).label('total_hours'),
                TurnModel.group_day_id.label('group_day_id'),
                TurnModel.free_day_group_id.label('free_day_group_id')
            ) \
            .filter(MeshDatumModel.rut == rut, MeshDatumModel.period == period) \
            .group_by(
                MeshDatumModel.rut,
                MeshDatumModel.week,
                MeshDatumModel.period,
                TurnModel.group_day_id,
                TurnModel.free_day_group_id
            ) \
            .having(func.count(MeshDatumModel.id) > 1) \
            .all()

        # Configurar el idioma en español
        locale.setlocale(locale.LC_TIME, 'es_ES.utf-8')

        data = []
        for datum in mesh_data:
            data.append({
                'rut': datum.rut,
                'week': datum.week,
                'period': datum.period,
                'total_hours': datum.total_hours,
                'working_days': datum.group_day_id,
                'free_days': datum.free_day_group_id
            })

        df = pd.DataFrame(data)

        df.loc['Total'] = df[['total_hours', 'working_days', 'free_days']].sum()

        df['masked_total_hours'] = df['total_hours'].apply(lambda x: '{:02d}:{:02d}'.format(int(x), int((x % 1) * 60)))

        df['week'] = df['week'].fillna('Total')

        return df
    
    @staticmethod
    def get_all_with_df_group_by(period):
        mesh_data = MeshDatumModel.query\
            .join(UserModel, UserModel.rut == MeshDatumModel.rut)\
            .filter(MeshDatumModel.period == period)\
            .add_columns(MeshDatumModel.id, MeshDatumModel.turn_id, MeshDatumModel.document_employee_id, MeshDatumModel.rut, MeshDatumModel.date, MeshDatumModel.total_hours, MeshDatumModel.start, MeshDatumModel.end, MeshDatumModel.week, MeshDatumModel.week_day, MeshDatumModel.period, UserModel.nickname, UserModel.visual_rut)\
            .all()

        data = []
        for datum in mesh_data:
            data.append({
                'id': datum.id,
                'turn_id': datum.turn_id,
                'document_employee_id': datum.document_employee_id,
                'rut': datum.rut,
                'date': datum.date,
                'total_hours': datum.total_hours,
                'start': datum.start,
                'end': datum.end,
                'week': datum.week,
                'week_day': datum.week_day,
                'period': datum.period,
                'nickname': datum.nickname,
                'visual_rut': datum.visual_rut
            })

        df = pd.DataFrame(data)
        grouped_df = df.groupby(['rut', 'period']).agg({
            'id': 'first',
            'turn_id': 'first',
            'document_employee_id': 'first',
            'date': 'first',
            'total_hours': 'sum',
            'start': 'first',
            'end': 'first',
            'week': 'first',
            'week_day': 'first',
            'nickname': 'first',
            'visual_rut': 'first'
        }).reset_index()

        grouped_data = grouped_df.to_dict(orient='records')
  
        return grouped_data
    
    @staticmethod
    def get_per_day(rut, period):
        mesh_data = MeshDatumModel.query\
                            .join(UserModel, UserModel.rut == MeshDatumModel.rut)\
                            .add_columns(UserModel.visual_rut, MeshDatumModel.turn_id, MeshDatumModel.rut, MeshDatumModel.date, MeshDatumModel.total_hours, MeshDatumModel.start, MeshDatumModel.end, MeshDatumModel.week, MeshDatumModel.period).all()

        return mesh_data
    
    @staticmethod
    def get_week(date):
        date = datetime.strptime(date, "%Y-%m-%d").date()
        week = (date.day - 1) // 7 + 1
        return week
    
    @staticmethod
    def get_by_date(date):
        mesh_data = MeshDatumModel.query.filter_by(date=date).all()

        return mesh_data

    @staticmethod
    def get_data_per_week(week):
        mesh_datum = MeshDatumModel.query.filter_by(week=week).filter(MeshDatumModel.turn_id != 0).first()

        return mesh_datum

    @staticmethod
    def get_sundays(week):
        mesh_data = MeshDatum.get(week)

        total_sundays = 0

        for mesh_datum in mesh_data:
            if mesh_datum.week_day == 7:
                total_sundays = total_sundays + 1

        return total_sundays
        
    @staticmethod
    def store(id, data):
        employee_turns = EmployeeTurn.get_all_by_rut(data['rut'])

        for employee_turn in employee_turns:
            current = datetime.strptime(str(employee_turn.start_date), '%Y-%m-%d')
            end = datetime.strptime(str(employee_turn.end_date), '%Y-%m-%d')
            
            while current <= end:
                current_date = Helper.split(current.strftime('%Y-%m-%d'), "-")
                week_day = Helper.week_day(int(current_date[0]), int(current_date[1]), int(current_date[2]))
                week = Helper.which_week(int(current_date[0]), int(current_date[1]), int(current_date[2]))
                
                if employee_turn.turn_id == 0:
                    mesh_datum = MeshDatumModel()
                    mesh_datum.turn_id = employee_turn.turn_id
                    mesh_datum.document_employee_id = id
                    mesh_datum.rut = employee_turn.rut
                    mesh_datum.date = current.strftime('%Y-%m-%d')
                    mesh_datum.total_hours = '0'
                    mesh_datum.week = week
                    mesh_datum.week_day = week_day
                    mesh_datum.start = '00:00:00'
                    mesh_datum.end = '00:00:00'
                    mesh_datum.period = employee_turn.period
                    mesh_datum.added_date = datetime.now()
                    mesh_datum.updated_date = datetime.now()

                    db.session.add(mesh_datum)
                    db.session.commit()
                else:
                    turn = Turn.get(employee_turn.turn_id)
                    time = Helper.split(turn.working, ':')
                    hours = int(time[0])
                    minutes = int(time[1])
                    minutes = minutes / 60.0
                    duration = hours + minutes

                    mesh_datum = MeshDatumModel()
                    mesh_datum.turn_id = employee_turn.turn_id
                    mesh_datum.document_employee_id = id
                    mesh_datum.rut = employee_turn.rut
                    mesh_datum.date = current.strftime('%Y-%m-%d')
                    mesh_datum.total_hours = duration
                    mesh_datum.week = week
                    mesh_datum.week_day = week_day
                    mesh_datum.start = turn.start
                    mesh_datum.end = turn.end
                    mesh_datum.period = employee_turn.period
                    mesh_datum.added_date = datetime.now()
                    mesh_datum.updated_date = datetime.now()

                    db.session.add(mesh_datum)
                    db.session.commit()

                last_week = week

                current += timedelta(days=1)

            PreEmployeeTurn.delete(employee_turn.id)

        return 1

    @staticmethod
    def delete(rut, period):
        mesh_data = MeshDatumModel.query.filter_by(rut=rut, period = period).all()

        for mesh_datum in mesh_data:
            mesh_datum = MeshDatumModel.query.filter_by(id=mesh_datum.id).first()

            db.session.delete(mesh_datum)
            db.session.commit()
        
