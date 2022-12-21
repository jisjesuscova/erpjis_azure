from app.models.models import HrPentionModel

class HrPention():
    @staticmethod
    def get(id = ''):
        hr_pention = HrPentionModel.query.get(id)

        return hr_pention