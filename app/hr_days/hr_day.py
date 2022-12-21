from app.models.models import HrEmployeeDayModel
from app.medical_licenses.medical_license import MedicalLicense
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.hr_final_day_months.hr_final_day_month import HrFinalDayMonth
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.hr_employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.helpers.helper import Helper
from app.models.models import EmployeeLaborDatumModel
from app import db
from flask import request

class HrDay():
    def update(period):
        value = request.form.getlist('value')
        rut = request.form.getlist('rut')

        for i in range(len(value)):
            hr_day = HrEmployeeDayModel.query.filter_by(rut=rut[i], period=period).first()
            hr_day.absence_days = value[i]
            days = hr_day.days
            hr_day.days = int(days) - int(value[i])

            db.session.add(hr_day)
            db.session.commit()

            HrEmployeeInput.update_employee_input_with_days(rut, period, 52, value)

    def store(period):
        employee_labor_data = EmployeeLaborDatumModel.query.all()

        for employee_labor_datum in employee_labor_data:
            license_days = MedicalLicense.days(employee_labor_datum.rut, period)
            entrance_days = EmployeeLaborDatum.entrance(employee_labor_datum.rut)
            exit_days = EmployeeLaborDatum.exit(employee_labor_datum.rut)
            splited_period = Helper.split(str(period), '-')
            adjustment_days = HrFinalDayMonth.get(splited_period[0])

            end_day = adjustment_days.end_day
            adjustment_days = adjustment_days.adjustment_day

            hr_day = HrEmployeeDayModel()
            hr_day.rut = employee_labor_datum.rut
            hr_day.period = period
            hr_day.current_days = end_day
            hr_day.entrance_days = entrance_days
            hr_day.exit_days = exit_days
            hr_day.license_days = license_days
            hr_day.absence_days = 0
            hr_day.adjustment_days = adjustment_days
            
            days = Helper.check_negative_days(int(end_day) - int(entrance_days) - int(exit_days) - int(license_days) + int(adjustment_days))
            hr_day.days = days

            db.session.add(hr_day)
            db.session.commit()

        
        