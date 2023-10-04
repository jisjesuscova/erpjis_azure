from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.hr_unemployment_insurances.hr_unemployment_insurance import HrUnemploymentInsurance
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum

class UnemploymentInsurance():
    @staticmethod
    def calculation(rut, period, branch_office_id):
        hr_unemployment_insurance = HrUnemploymentInsurance.get()
        employee_hr_unemployment_insurance_total = hr_unemployment_insurance.employee_value
        company_hr_unemployment_insurance_total = hr_unemployment_insurance.company_value

        employee_labor_datum = EmployeeLaborDatum.get(rut)

        taxable_assets = HrEmployeeInput.get_with(rut, period, 36)

        if employee_labor_datum.contract_type_id == 3:
            total = taxable_assets * employee_hr_unemployment_insurance_total
            HrEmployeeInput.calculation_store(rut, period, branch_office_id, 43, total)

            total = taxable_assets * company_hr_unemployment_insurance_total
            HrEmployeeInput.calculation_store(rut, period, branch_office_id, 42, total)
        else:
            total = taxable_assets * (employee_hr_unemployment_insurance_total + company_hr_unemployment_insurance_total)
            HrEmployeeInput.calculation_store(rut, period, branch_office_id, 42, total)
            total = 0
            HrEmployeeInput.calculation_store(rut, period, branch_office_id, 43, total)

        return 1