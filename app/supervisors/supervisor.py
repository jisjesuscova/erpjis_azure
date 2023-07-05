from app.models.models import SupervisorModel

class Supervisor:
    @staticmethod
    def get(branch_office_id):
        supervisors = SupervisorModel.query.filter_by(branch_office_id=branch_office_id).all()

        return supervisors
    
    @staticmethod
    def get_by_rut(rut):
        supervisor = SupervisorModel.query.filter_by(rut=rut).first()

        return supervisor