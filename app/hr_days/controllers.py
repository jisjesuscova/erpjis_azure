from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.hr_employee_days.hr_employee_day import HrEmployeeDay
from app.years.year import Year
from app.hr_days.hr_day import HrDay
from app.months.month import Month
from app.audits.audit import Audit

hr_day = Blueprint("hr_days", __name__)

@hr_day.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@hr_day.route("/management_payrolls/days/<period>", methods=['GET'])
@hr_day.route("/management_payrolls/days", methods=['GET'])
def index(period = ''):
   years = Year.get()
   months = Month.get()
   hr_employee_days = HrEmployeeDay.get(period)
   
   return render_template('management_payrolls/hr_days/days.html', hr_employee_days = hr_employee_days, years = years, months = months, period = period)


@hr_day.route("/management_payrolls/absences/<period>", methods=['POST'])
@hr_day.route("/management_payrolls/absences", methods=['POST'])
def absence(period = ''):
   HrDay.update(period)

   return redirect(url_for('hr_days.index', period = period))
