from flask import request
from app import db
from datetime import datetime, timedelta
from app.models.models import MeshDatumModel, TotalMeshDatumModel, UserModel
from app.employees_turns.employee_turn import EmployeeTurn
from app.turns.turn import Turn
from app.helpers.helper import Helper
from app.pre_employee_turns.pre_employee_turn import PreEmployeeTurn
from sqlalchemy import func

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
    def get_per_day(rut, period):
        mesh_data = MeshDatumModel.query\
                            .join(UserModel, UserModel.rut == MeshDatumModel.rut)\
                            .add_columns(UserModel.visual_rut, MeshDatumModel.turn_id, MeshDatumModel.rut, MeshDatumModel.date, MeshDatumModel.total_hours, MeshDatumModel.start, MeshDatumModel.end, MeshDatumModel.week, MeshDatumModel.period).all()

        return mesh_data
    
    @staticmethod
    def get_week(rut, date):
        mesh_datum = MeshDatumModel.query.filter_by(rut=rut,date=date).first()

        return mesh_datum.week
    
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
                    turn = Turn.get(employee_turn.turn_id)

                    mesh_datum = MeshDatumModel()
                    mesh_datum.turn_id = employee_turn.turn_id
                    mesh_datum.rut = employee_turn.rut
                    mesh_datum.date = current.strftime('%Y-%m-%d')
                    mesh_datum.total_hours = '00:00:00'
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

                    mesh_datum = MeshDatumModel()
                    mesh_datum.turn_id = employee_turn.turn_id
                    mesh_datum.rut = employee_turn.rut
                    mesh_datum.date = current.strftime('%Y-%m-%d')
                    mesh_datum.total_hours = turn.working
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

        n = last_week

        for i in range(1, n+1):
            mesh_datum = MeshDatum.get_data_per_week(i)

            total_sundays = MeshDatum.get_sundays(i)

            turn = Turn.get(mesh_datum.turn_id)

            total_mesh_datum = TotalMeshDatumModel()
            total_mesh_datum.document_employee_id = id
            total_mesh_datum.rut = mesh_datum.rut
            total_mesh_datum.total_hours = turn.total_week_hours
            total_mesh_datum.week = i
            total_mesh_datum.total_sundays = total_sundays
            total_mesh_datum.total_free_days = turn.free_day_group_id
            total_mesh_datum.period = mesh_datum.period
            db.session.add(total_mesh_datum)
            db.session.commit()
            
        return 1

    @staticmethod
    def delete(rut, period):
        mesh_data = MeshDatumModel.query.filter_by(rut=rut, period = period).all()

        for mesh_datum in mesh_data:
            mesh_datum = MeshDatumModel.query.filter_by(id=mesh_datum.id).first()

            db.session.delete(mesh_datum)
            db.session.commit()
        
