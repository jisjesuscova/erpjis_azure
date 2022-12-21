from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class SocialLaws():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        pention = HrEmployeeInput.get_with(rut, period, 35)
        health = HrEmployeeInput.get_with(rut, period, 39)
        employee_unemployment_insurance = HrEmployeeInput.get_with(rut, period, 43)

        total = pention + health + employee_unemployment_insurance

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 44, total)

        return 1