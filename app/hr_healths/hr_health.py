from app.models.models import HrHealthModel

class HrHealth():
    def get():
        hr_health = HrHealthModel.query.filter_by(id=1).first()

        return hr_health