from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.hr_days.hr_day import HrDay
from app.months.month import Month
from app.years.year import Year
from app.audits.audit import Audit

hr_employee = Blueprint("hr_employees", __name__)

@hr_employee.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@hr_employee.route("/management_payrolls/employees", methods=['GET'])
def index():
   months = Month.get()
   years = Year.get()

   return render_template('management_payrolls/hr_employees/employees.html', months = months, years = years)

@hr_employee.route("/management_payrolls/employees", methods=['POST'])
def open():
   HrEmployeeInput.open(request.form)

   period = request.form['month'] +'-'+ request.form['year']
   HrDay.store(period)

   return redirect(url_for('absence_days.index', period = period))
