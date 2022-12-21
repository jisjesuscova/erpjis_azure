from app.models.models import HrEmployeeInputModel
from app.calculation_values.proportional_salary import ProportionalSalary
from app.calculation_values.proportional_collation import ProportionalCollation
from app.calculation_values.proportional_locomotion import ProportionalLocomotion
from app.calculation_values.taxable_assets import TaxableAssets
from app.calculation_values.no_taxable_assets import NoTaxableAssets
from app.calculation_values.gratification import Gratification
from app.calculation_values.pention import PentionCalculation
from app.calculation_values.health import HealthCalculation
from app.calculation_values.unemployment_insurance import UnemploymentInsurance
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.calculation_values.social_laws import SocialLaws
from app.calculation_values.total_assets import TotalAssets
from app.calculation_values.taxable_taxable_calculation import TaxableTaxableCalculation
from app.calculation_values.single_tax import SingleTaxCalculation
from app.calculation_values.other_discount import OtherDiscount
from app.calculation_values.total_discounts import TotalDiscount
from app.calculation_values.net_salary import NetSalary

class CalculationValue():
    def store(period):
        hr_employee_input_data = HrEmployeeInputModel.query.filter_by(period=period).group_by('rut').all()

        for hr_employee_input_datum in hr_employee_input_data:
            hr_employeelabor_data = EmployeeLaborDatum.get(hr_employee_input_datum.rut)
            #ProportionalSalary.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #ProportionalCollation.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #ProportionalLocomotion.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #Gratification.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #TaxableAssets.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #NoTaxableAssets.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #PentionCalculation.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id, hr_employeelabor_data.pention_id)
            #HealthCalculation.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #UnemploymentInsurance.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #SocialLaws.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #TotalAssets.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #TaxableTaxableCalculation.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #SingleTaxCalculation.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #OtherDiscount.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #TotalDiscount.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
            #NetSalary.calculation(hr_employee_input_datum.rut, period, hr_employeelabor_data.branch_office_id)
        
        return 1