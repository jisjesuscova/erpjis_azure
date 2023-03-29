from app.models.models import HonoraryReasonModel

class HonoraryReason():
    @staticmethod
    def get():
        honoraries = HonoraryReasonModel.query.all()
        
        return honoraries
