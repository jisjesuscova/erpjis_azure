from app.models.models import PreEmployeeTurnModel
from app import db
from sqlalchemy import inspect
from datetime import datetime
from app.helpers.helper import Helper
from app.turns.turn import Turn

class EmployeeTurn():
    def delete_old_ones(rut):
        employees_turns = PreEmployeeTurnModel.query.filter_by(rut = rut).all()

        for employee_turn in employees_turns:
            employee_turn_detail = PreEmployeeTurnModel.query.filter_by(id = employee_turn.id).first()

            db.session.delete(employee_turn_detail)
            db.session.commit()

    @staticmethod
    def pre_store(data):
        turn = Turn.get(data['turn_id'])

        end_day = Helper.get_last_date(data['start_date'], turn.group_day_id)
        print(end_day)
        turn = PreEmployeeTurnModel()
        turn.turn_id = data['turn_id']
        turn.rut = data['employee_id']
        turn.start_date = data['start_date']
        turn.end_day = end_day
        turn.added_date = datetime.now()
        turn.updated_date = datetime.now()
        inspection = inspect(turn)

        
        db.session.add(turn)
        status = inspection.pending
        db.session.commit()
        return status