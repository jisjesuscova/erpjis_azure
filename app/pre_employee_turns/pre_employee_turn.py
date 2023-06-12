from app.models.models import PreEmployeeTurnModel
from app import db

class PreEmployeeTurn():
    def delete(id):
        pre_employee_turn = PreEmployeeTurnModel.query.filter_by(id = id).first()

        db.session.delete(pre_employee_turn)
        db.session.commit()

    def delete_by_rut(rut):
        pre_employee_turns = PreEmployeeTurnModel.query.filter_by(rut = rut).all()

        for pre_employee_turn in pre_employee_turns:
            detail_pre_employee_turn = PreEmployeeTurnModel.query.filter_by(id = pre_employee_turn.id).first()

            db.session.delete(detail_pre_employee_turn)
            db.session.commit()
