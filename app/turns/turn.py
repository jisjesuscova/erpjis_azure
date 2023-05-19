from app.models.models import TurnModel, PreEmployeeTurnModel
from app import db

class Turn():
    def get_by_employee_type_group(employee_type_id, group_id):
        turns = TurnModel.query.filter_by(employee_type_id=employee_type_id, group_id=group_id).all()

        return turns

    def get(id):
        turn = TurnModel.query.filter_by(id=id).first()

        return turn
    
    def get_special(id):
        turn = TurnModel.query.filter_by(id=id).all()

        return turn
        