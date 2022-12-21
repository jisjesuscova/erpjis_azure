from app.models.models import EmployeeLaborDatumModel
from app.helpers.helper import Helper
from app.hr_final_day_months.hr_final_day_month import HrFinalDayMonth
from datetime import datetime

class EmployeeLaborDatum():
    def get(rut):
        employee_labor_datum = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()

        return employee_labor_datum

    def entrance(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()

        data = Helper.split(str(employee_labor_data.entrance_company), '-')
        start_month = str(data[0]) + '-' + data[1] +'-01'
        end_month = employee_labor_data.entrance_company

        d1 = datetime.strptime(str(start_month), "%Y-%m-%d")
        d2 = datetime.strptime(str(end_month), "%Y-%m-%d")
        days = abs((d2 - d1 ).days)

        return days
    
    def exit(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()
        
        if employee_labor_data.exit_company is None:
            return 0
        else:
            data = Helper.split(employee_labor_data.exit_company, '-')

            final_day_month = HrFinalDayMonth.get(data[1])
            final_day_month = final_day_month.end_day
        
            start_month = employee_labor_data.exit_company
        
            end_month = str(data[0]) + '-' + data[1] +'-' + str(final_day_month)

            d1 = datetime.strptime(start_month, "%Y-%m-%d")
            d2 = datetime.strptime(end_month, "%Y-%m-%d")
            days = abs((d2 - d1 ).days)

            return days
