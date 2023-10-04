from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.hr_healths.hr_health import HrHealth

class HealthCalculation():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        health = HrHealth.get()
        health = health.value

        taxable_assets = HrEmployeeInput.get_with(rut, period, 36)

        total = round(int(taxable_assets) * float(health))

        HrEmployeeInput.calculation_store(rut, period, branch_office_id, 39, total)

        return 1