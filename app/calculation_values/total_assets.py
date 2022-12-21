from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class TotalAssets():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        taxable_assets = HrEmployeeInput.get_with(rut, period, 36)
        no_taxable_assets  = HrEmployeeInput.get_with(rut, period, 38)

        total = taxable_assets + no_taxable_assets

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 66, total)

        return 1