from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class ProportionalSalary():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        salary = HrEmployeeInput.get_with(rut, period, 1)

        days = HrEmployeeInput.get_with(rut, period, 31)

        total = round((int(salary)/30)*int(days))

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 40, total)

        return 1