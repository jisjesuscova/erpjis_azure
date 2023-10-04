from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class OtherDiscount():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        total = HrEmployeeInput.get_with_sum(rut, period, 3)
        
        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 55, total)

        return 1