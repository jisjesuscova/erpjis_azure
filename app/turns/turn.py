from app.models.models import TurnModel
from app import db
from sqlalchemy import or_, and_

class Turn():
    def get_by_employee_type_group(employee_type_id, group_id):
        if employee_type_id == 1:
            turns = TurnModel.query.filter_by(employee_type_id=employee_type_id, group_id=group_id, visibility_id = 0).all()
        else:
            turns = TurnModel.query.filter(TurnModel.employee_type_id == 2,
                               TurnModel.group_id == group_id, TurnModel.visibility_id == 0).all()

        return turns

    def get(id):
        turn = TurnModel.query.filter_by(id=id).first()

        return turn
    
    def existence(id):
        turn_qty = TurnModel.query.filter_by(id=id).count()

        if turn_qty > 0:
            return 1
        else:
            return 0
    
    def get_special(id):
        turn = TurnModel.query.filter_by(id=id).all()

        return turn