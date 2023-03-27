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

    def get(data):
        pre_employee_turn = PreEmployeeTurnModel.query.filter_by(turn_id = data['turn_id'], rut = data['employee_id'], start_date = data['start_date']).all()

        return pre_employee_turn

    def get_all_by_rut(rut):
        pre_employee_turns = PreEmployeeTurnModel.query.filter_by(rut = rut).all()

        return pre_employee_turns
    
    @staticmethod
    def update(data):
        turn = Turn.get(data['turn_id'])

        end_date = Helper.get_last_date(data['start_date'], turn.group_day_id)
            
        turn = PreEmployeeTurnModel.query.filter_by(id=data['id']).first()
        turn.turn_id = data['turn_id']
        turn.rut = data['employee_id']
        turn.start_date = data['start_date']
        turn.end_date = end_date
        turn.updated_date = datetime.now()
        inspection = inspect(turn)

        db.session.add(turn)
        status = inspection.pending
        db.session.commit()
        return status
        
    @staticmethod
    def pre_store(data):
        if data['turn_id'] == '0':
            turn = PreEmployeeTurnModel()
            turn.turn_id = 0
            turn.rut = data['employee_id']
            turn.start_date = data['start_date']
            turn.end_date = data['start_date']
            turn.added_date = datetime.now()
            turn.updated_date = datetime.now()
            inspection = inspect(turn)

            db.session.add(turn)
            status = inspection.pending
            db.session.commit()
            return status
        else:
            turn = Turn.get(data['turn_id'])

            end_date = Helper.get_last_date(data['start_date'], turn.group_day_id)

            turn = PreEmployeeTurnModel()
            turn.turn_id = data['turn_id']
            turn.rut = data['employee_id']
            turn.start_date = data['start_date']
            turn.end_date = end_date
            turn.added_date = datetime.now()
            turn.updated_date = datetime.now()
            inspection = inspect(turn)

            
            db.session.add(turn)
            status = inspection.pending
            db.session.commit()
            return status