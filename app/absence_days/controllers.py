from flask import Blueprint, render_template, request
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.years.year import Year
from app.helpers.helper import Helper
from app.months.month import Month

absence_day = Blueprint("absence_days", __name__)

@absence_day.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@absence_day.route("/management_payrolls/absence_days/<period>", methods=['GET'])
@absence_day.route("/management_payrolls/absence_days", methods=['GET'])
def index(period = ''):
   years = Year.get()
   months = Month.get()
   splited_period = Helper.split(period, '-')
   year = splited_period[1]
   month = splited_period[0]
   hr_employee_inputs = HrEmployeeInput.get('', period)

   return render_template('management_payrolls/absence_days/absence_days.html', hr_employee_inputs = hr_employee_inputs, years = years, months = months, period_month = month, period_year = year, period = period)

@absence_day.route("/management_payrolls/absence_days/search", methods=['POST'])
@absence_day.route("/management_payrolls/absence_days", methods=['POST'])
def search():
   years = Year.get()
   months = Month.get()
   period = request.form['month'] +"-"+  request.form['year']
   hr_employee_inputs = HrEmployeeInput.get('', period)

   return render_template('management_payrolls/absence_days/absence_days.html', hr_employee_inputs = hr_employee_inputs, years = years, months = months, period = period)