from app.models.models import PreEmployeeTurnModel
from app import db

class PreEmployeeTurn():
    def delete(id):
        pre_employee_turn = PreEmployeeTurnModel.query.filter_by(id = id).first()

        db.session.delete(pre_employee_turn)
        db.session.commit()
