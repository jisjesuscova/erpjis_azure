from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need, db
from app.employees.employee import Employee
from app.genders.gender import Gender
from app.nationalities.nationality import Nationality
from app.models.models import EmployeeModel
from datetime import datetime

personal_datum = Blueprint("personal_data", __name__)

@personal_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@personal_datum.route("/human_resources/personal_data/<int:rut>", methods=['GET'])
@personal_datum.route("/human_resources/personal_data", methods=['GET'])
def show(rut):
   employee = Employee.get(rut)
   genders = Gender.get()
   nationalities = Nationality.get()

   return render_template('human_resources/personal_data/personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities)

@personal_datum.route("/human_resources/personal_data/<int:rut>", methods=['POST'])
@personal_datum.route("/human_resources/personal_data", methods=['POST'])
def update(rut):
   Employee.update(request.form, rut)

   return redirect(url_for('personal_data.show', rut = rut))