from app.models.models import CivilStateModel

class CivilState():
    @staticmethod
    def get(id = ''):
        if id == '':
            civil_states = CivilStateModel.query.order_by('civil_state').all()

            return civil_states
        else:
            civil_state = CivilStateModel.query.filter_by(id=id).first()

            return civil_state