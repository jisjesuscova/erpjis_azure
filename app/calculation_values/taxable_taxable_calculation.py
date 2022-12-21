from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class TaxableTaxableCalculation():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        taxable_assets = HrEmployeeInput.get_with(rut, period, 36)
        social_laws = HrEmployeeInput.get_with(rut, period, 44)

        total = taxable_assets - social_laws

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 47, total)

        return 1