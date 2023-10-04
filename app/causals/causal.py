from app.models.models import CausalModel

class Causal():
    @staticmethod
    def get(id):
        print(id)
        causal = CausalModel.query.filter_by(id=id).first()

        return causal
