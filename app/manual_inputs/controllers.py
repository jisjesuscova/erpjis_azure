from flask import Blueprint, render_template, request
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.years.year import Year
from app.helpers.helper import Helper
from app.months.month import Month

manual_input = Blueprint("manual_inputs", __name__)

@manual_input.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@manual_input.route("/management_payrolls/manual_inputs/<period>", methods=['GET'])
@manual_input.route("/management_payrolls/manual_inputs", methods=['GET'])
def index(period = ''):
   years = Year.get()
   months = Month.get()
   splited_period = Helper.split(period, '-')
   year = splited_period[1]
   month = splited_period[0]
   hr_employee_inputs = HrEmployeeInput.get('', period)

   return render_template('management_payrolls/manual_inputs/manual_inputs.html', hr_employee_inputs = hr_employee_inputs, years = years, months = months, period_month = month, period_year = year, period = period)

@manual_input.route("/management_payrolls/manual_inputs/search", methods=['POST'])
@manual_input.route("/management_payrolls/manual_inputs", methods=['POST'])
def search():
   years = Year.get()
   months = Month.get()
   period = request.form['month'] +"-"+  request.form['year']
   hr_employee_inputs = HrEmployeeInput.get('', period)

   return render_template('management_payrolls/manual_inputs/manual_inputs.html', hr_employee_inputs = hr_employee_inputs, years = years, months = months, period = period)