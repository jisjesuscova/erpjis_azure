from app.models.models import HrSingleTaxModel
class HrSingleTax():
    def calculation(value):
        hr_single_tax = HrSingleTaxModel.query.filter(HrSingleTaxModel.since<value).filter(HrSingleTaxModel.until>value).first()

        return (hr_single_tax.factor*value)-hr_single_tax.amount

    def tax(value):
        hr_single_tax = HrSingleTaxModel.query.filter(HrSingleTaxModel.since<value).filter(HrSingleTaxModel.until>value).first()

        return hr_single_tax.amount

    def factor(value):
        hr_single_tax = HrSingleTaxModel.query.filter(HrSingleTaxModel.since<value).filter(HrSingleTaxModel.until>value).first()

        return hr_single_tax.factor

        
