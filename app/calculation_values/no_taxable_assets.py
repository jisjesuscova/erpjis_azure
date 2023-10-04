from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class NoTaxableAssets():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        total = HrEmployeeInput.get_with_sum(rut, period, 2)

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 38, total)

        return 1