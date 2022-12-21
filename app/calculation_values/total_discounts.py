from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class TotalDiscount():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        social_laws = HrEmployeeInput.get_with(rut, period, 44)
        tax = HrEmployeeInput.get_with(rut, period, 48)
        total_discount = HrEmployeeInput.get_with(rut, period, 55)

        total = social_laws + tax + total_discount

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 67, total)

        return 1