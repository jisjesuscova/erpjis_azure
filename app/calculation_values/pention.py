from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.hr_pentions.hr_pention import HrPention

class PentionCalculation():
    @staticmethod
    def calculation(rut, period, branch_office_id, pention_id):
        pention = HrPention.get(pention_id)
        pention = pention.afp_value

        taxable_assets = HrEmployeeInput.get_with(rut, period, 36)
        total = round(int(taxable_assets) * float(pention)/100)

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 35, total)

        return 1