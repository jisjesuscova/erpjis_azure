from flask import request
from app import db
from datetime import datetime
from app.models.models import MeshDatumModel
from app.employees_turns.employee_turn import EmployeeTurn
from app.turns.turn import Turn
from app.helpers.helper import Helper

class MeshDatum():
    @staticmethod
    def store(data):
        turn = Turn.get(data['turn_id'])

        employee_turns = EmployeeTurn.get_all_by_rut(data['rut'])

        total_hours = Helper.calculate_total_hours(turn.start_time, turn.end_time)

        # Obtener fecha y hora actuales
        current_date = datetime.datetime.now()

        # Obtener el mes y el año actuales
        current_month = current_date.month
        current_year = current_date.year

        weeks_in_month = Helper.weeks_in_month(current_year, current_month)

        weeks = 1

        for employee_turn in employee_turns:
            if weeks == 1:
                mesh_datum = MeshDatumModel()
                mesh_datum.turn_id = employee_turn.turn_id
                mesh_datum.rut = employee_turn.rut
                mesh_datum.start_date = employee_turn.start_date
                mesh_datum.end_date = employee_turn.end_date
                mesh_datum.total_hours = total_hours
                mesh_datum.added_date = datetime.now()
                mesh_datum.updated_date = datetime.now()

                db.session.add(mesh_datum)
                db.session.commit()
            elif weeks == weeks_in_month:
                mesh_datum = MeshDatumModel()
                mesh_datum.turn_id = employee_turn.turn_id
                mesh_datum.rut = employee_turn.rut
                mesh_datum.start_date = employee_turn.start_date
                mesh_datum.end_date = employee_turn.end_date
                mesh_datum.total_hours = total_hours
                mesh_datum.added_date = datetime.now()
                mesh_datum.updated_date = datetime.now()

                db.session.add(mesh_datum)
                db.session.commit()
            else:
                mesh_datum = MeshDatumModel()
                mesh_datum.turn_id = employee_turn.turn_id
                mesh_datum.rut = employee_turn.rut
                mesh_datum.start_date = employee_turn.start_date
                mesh_datum.end_date = employee_turn.end_date
                mesh_datum.total_hours = total_hours
                mesh_datum.added_date = datetime.now()
                mesh_datum.updated_date = datetime.now()

                db.session.add(mesh_datum)
                db.session.commit()

            weeks += 1
