from app.models.models import SupervisorModel

class Supervisor:
    @staticmethod
    def get(branch_office_id):
        supervisors = SupervisorModel.query.filter_by(branch_office_id=branch_office_id).all()

        return supervisors