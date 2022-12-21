from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.hr_single_taxes.hr_single_tax import HrSingleTax
class SingleTaxCalculation():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        taxable_taxable = HrEmployeeInput.get_with(rut, period, 47)
        total = HrSingleTax.calculation(taxable_taxable)

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 48, total)

        total = HrSingleTax.tax(taxable_taxable)

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 49, total)

        return 1