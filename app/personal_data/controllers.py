from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.genders.gender import Gender
from app.nationalities.nationality import Nationality
from app.dropbox_data.dropbox import Dropbox
from app.users.user import User
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from PIL import Image
import os

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
   employee_labor_datum = EmployeeLaborDatum.get(rut)
   genders = Gender.get()
   nationalities = Nationality.get()
   download_url = Dropbox.get('/flask_user_photos/', employee.picture)

   return render_template('human_resources/personal_data/personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum)

@personal_datum.route("/human_resources/personal_data/<int:rut>", methods=['POST'])
@personal_datum.route("/human_resources/personal_data", methods=['POST'])
def update(rut):
   if len(request.files) != 0:
      picture = Dropbox.upload(rut, "_photo", request.files, "/flask_user_photos/", "C:/Users/jesus/OneDrive/Desktop/erpjis_azure/", 1)
      Employee.upload(rut, picture)

   Employee.update(request.form, rut)

   return redirect(url_for('personal_data.show', rut = rut))

@personal_datum.route("/human_resources/personal_datum/delete_picture/<int:rut>", methods=['GET'])
@personal_datum.route("/human_resources/personal_datum/delete_picture", methods=['GET'])
def delete_picture(rut):
   employee = Employee.get(rut)
   Dropbox.delete("/flask_user_photos/", employee.picture)
   Employee.delete_picture(rut)
   
   return redirect(url_for('personal_data.show', rut = rut))
