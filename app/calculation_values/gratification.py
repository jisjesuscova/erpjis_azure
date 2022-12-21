from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class Gratification():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        taxable_assets = HrEmployeeInput.get_with(rut, period, 36)
        
        total = int(taxable_assets) * 0.25

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 37, total)

        return 1