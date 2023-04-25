from flask import request
from app import db
from datetime import datetime, timedelta
from app.models.models import MeshDatumModel
from app.employees_turns.employee_turn import EmployeeTurn
from app.turns.turn import Turn
from app.helpers.helper import Helper

class MeshDatum():
    @staticmethod
    def store(data):
        employee_turns = EmployeeTurn.get_all_by_rut(data['rut'])

        for employee_turn in employee_turns:
            current = datetime.strptime(str(employee_turn.start_date), '%Y-%m-%d')
            end = datetime.strptime(str(employee_turn.end_date), '%Y-%m-%d')
            
            while current <= end:
                current_date = Helper.split(current.strftime('%Y-%m-%d'), "-")
                week_day = Helper.week_day(int(current_date[0]), int(current_date[1]), int(current_date[2]))

                if employee_turn.turn_id == 0:
                    turn = Turn.get(employee_turn.turn_id)

                    mesh_datum = MeshDatumModel()
                    mesh_datum.turn_id = employee_turn.turn_id
                    mesh_datum.rut = employee_turn.rut
                    mesh_datum.date = current.strftime('%Y-%m-%d')
                    mesh_datum.total_hours = 0
                    mesh_datum.week_day = week_day
                    mesh_datum.start = '00:00:00'
                    mesh_datum.end = '00:00:00'
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
                    mesh_datum.week_day = week_day
                    mesh_datum.start = turn.start
                    mesh_datum.end = turn.end
                    mesh_datum.added_date = datetime.now()
                    mesh_datum.updated_date = datetime.now()

                    db.session.add(mesh_datum)
                    db.session.commit()

                current += timedelta(days=1)

        return 1
