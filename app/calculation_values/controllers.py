from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.calculation_values.calculation_value import CalculationValue
from app.years.year import Year
from app.months.month import Month

calculation_value = Blueprint("calculation_values", __name__)

@calculation_value.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@calculation_value.route("/management_payrolls/calculation_values", methods=['GET'])
def index():
   years = Year.get()
   months = Month.get()

   return render_template('management_payrolls/calculation_values/calculation_values.html', years = years, months = months)

@calculation_value.route("/management_payrolls/calculation_values/store", methods=['POST'])
@calculation_value.route("/management_payrolls/calculation_values", methods=['POST'])
def store():
   period = request.form['month'] +'-'+ request.form['year']
   CalculationValue.store(period)

   return redirect(url_for('settlement_data.store', period = period))