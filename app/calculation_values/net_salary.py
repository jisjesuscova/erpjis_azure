from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class NetSalary():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        total_asset = HrEmployeeInput.get_with(rut, period, 66)
        total_discount = HrEmployeeInput.get_with(rut, period, 67)

        total = total_asset + total_discount

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 51, total)

        return 1