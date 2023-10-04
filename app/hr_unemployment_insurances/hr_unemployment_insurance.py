from app.models.models import HrUnemploymentInsuranceModel

class HrUnemploymentInsurance():
    def get():
        hr_unemployment_insurance = HrUnemploymentInsuranceModel.query.filter_by(id=1).first()

        return hr_unemployment_insurance