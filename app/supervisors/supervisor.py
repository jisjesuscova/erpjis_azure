from app.models.models import SupervisorModel

class Supervisor:
    @staticmethod
    def get(branch_office_id):
        supervisors = SupervisorModel.query.filter_by(branch_office_id=branch_office_id).all()

        return supervisors
    
    @staticmethod
    def get_by_branch_office_id(branch_office_id):
        supervisor = SupervisorModel.query.filter_by(branch_office_id=branch_office_id).first()

        return supervisor