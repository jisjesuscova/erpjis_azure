from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
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

   if employee.picture != None:
      download_url = Dropbox.get('/flask_user_photos/', employee.picture)
   else:
      download_url = url_for("static", filename="dist/img/logo.png")
   
   if employee.signature != None:
      signature_exist = Dropbox.exist('/signature/', employee.signature)

      if signature_exist == 1:
         signature = Dropbox.get('/signature/', employee.signature)
      else:
         signature = ''
   else:
      signature_exist = 0
      signature = ''

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/personal_data/personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/personal_data/personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/personal_data/personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/personal_data/personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature)

@personal_datum.route("/human_resources/personal_data/<int:rut>", methods=['POST'])
@personal_datum.route("/human_resources/personal_data", methods=['POST'])
def update(rut):
   
   if request.files['file'].filename != '':
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
