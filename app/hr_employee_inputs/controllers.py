from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.hr_input_descriptions.hr_input_description import HrInputDescription
from app.files.file import File
from app.months.month import Month
from app.years.year import Year
from app.helpers.helper import Helper

hr_employee_input = Blueprint("hr_employee_inputs", __name__)

@hr_employee_input.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@hr_employee_input.route("/management_payrolls/hr_employee_inputs/<period>", methods=['GET'])
@hr_employee_input.route("/management_payrolls/hr_employee_inputs", methods=['GET'])
def index(period = '00-0000'):
   years = Year.get()
   months = Month.get()
   splited_period = Helper.split(period, '-')
   year = splited_period[1]
   month = splited_period[0]
   hr_employee_inputs = HrEmployeeInput.get('', period)
   hr_input_descriptions = HrInputDescription.get('', 3)

   return render_template('management_payrolls/hr_employee_inputs/hr_employee_inputs.html', hr_employee_inputs = hr_employee_inputs, years = years, months = months, period_month = month, period_year = year, period = period, hr_input_descriptions = hr_input_descriptions, hr_input_description_id = 0)

@hr_employee_input.route("/management_payrolls/hr_employee_inputs/<period>", methods=['POST'])
@hr_employee_input.route("/management_payrolls/hr_employee_inputs", methods=['GET'])
def store(period = ''):
   if period == '':
      HrEmployeeInput.store(request.form, period)
   else:
      period = request.form['month'] +'-'+ request.form['year'] 
      HrEmployeeInput.store(request.form, period)

   return redirect(url_for('hr_employee_inputs.index', period = period))


@hr_employee_input.route("/management_payrolls/hr_employee_inputs/days/<period>", methods=['GET'])
@hr_employee_input.route("/management_payrolls/hr_employee_inputs/days", methods=['GET'])
def day(period = ''):
   HrEmployeeInput.store_input_days(period)

   return redirect(url_for('hr_employee_inputs.index', period = period))


@hr_employee_input.route("/management_payrolls/hr_employee_inputs/add/<period>", methods=['POST'])
@hr_employee_input.route("/management_payrolls/hr_employee_inputs/add", methods=['POST'])
def add(period = ''):
   years = Year.get()
   months = Month.get()
   splited_period = Helper.split(period, '-')
   year = int(splited_period[1])
   month = int(splited_period[0])
   hr_employee_inputs = HrEmployeeInput.get('', period)
   hr_input_descriptions = HrInputDescription.get('', 3)
   general_value = request.form['general_value']

   return render_template('management_payrolls/hr_employee_inputs/hr_employee_inputs.html', hr_employee_inputs = hr_employee_inputs, years = years, months = months, period = period, period_month = month, period_year = year, hr_input_descriptions = hr_input_descriptions, general_value = general_value, hr_input_description_id = int(request.form['hr_input_description_id']))


@hr_employee_input.route("/management_payrolls/hr_employee_inputs/search", methods=['POST'])
@hr_employee_input.route("/management_payrolls/hr_employee_inputs", methods=['POST'])
def search():
   years = Year.get()
   months = Month.get()
   period = request.form['month'] +"-"+  request.form['year']
   splited_period = Helper.split(period, '-')
   year = int(splited_period[1])
   month = int(splited_period[0])
   hr_employee_inputs = HrEmployeeInput.get('', period)
   hr_input_descriptions = HrInputDescription.get('', 3)

   return render_template('management_payrolls/hr_employee_inputs/hr_employee_inputs.html', hr_employee_inputs = hr_employee_inputs, years = years, months = months, period = period, period_month = month, period_year = year, hr_input_descriptions = hr_input_descriptions, hr_input_description_id = int(request.form['hr_input_description_id']))


@hr_employee_input.route("/management_payrolls/hr_employee_inputs/create", methods=['GET'])
def create():
   years = Year.get()
   months = Month.get()
   hr_input_descriptions = HrInputDescription.get('', 3)

   return render_template('management_payrolls/hr_employee_inputs/hr_employee_inputs_create.html', years = years, months = months, hr_input_descriptions = hr_input_descriptions)


@hr_employee_input.route("/management_payrolls/hr_employee_inputs/upload", methods=['POST'])
def upload():
   period = request.form['month'] +'-'+ request.form['year'] 
   HrEmployeeInput.false_store(request.form, period)
   File.upload_csv(request.files, "C:/Users/jesus/OneDrive/Desktop/erp_jis_v1/erp_jis_v1/erp_jis/", period, request.form['hr_input_description_id'])
   
   return redirect(url_for('hr_employee_inputs.index', period = period))