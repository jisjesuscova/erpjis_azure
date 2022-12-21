from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

class ProportionalCollation():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        collation = HrEmployeeInput.get_with(rut, period, 2)

        days = HrEmployeeInput.get_with(rut, period, 31)

        total = round((int(collation)/30)*int(days))

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 72, total)

        return 1