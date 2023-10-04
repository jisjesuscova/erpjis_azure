from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class TaxableAssets():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        total = HrEmployeeInput.get_with_sum(rut, period, 1)
        
        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 36, total)

        return 1