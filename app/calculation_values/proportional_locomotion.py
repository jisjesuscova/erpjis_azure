from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class ProportionalLocomotion():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        locomotion = HrEmployeeInput.get_with(rut, period, 3)

        days = HrEmployeeInput.get_with(rut, period, 31)

        total = round((int(locomotion)/30)*int(days))

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 73, total)

        return 1