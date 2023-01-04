from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.genders.gender import Gender
from app.nationalities.nationality import Nationality
from app.dropbox_data.dropbox import Dropbox
from app.users.user import User
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
   genders = Gender.get()
   nationalities = Nationality.get()
   user = User.get_by_rut(employee.rut)

   if user.rol_id == 1:
      return render_template('human_resources/personal_data/regular_personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities)
   else:
      return render_template('human_resources/personal_data/personal_data_update.html', employee = employee, rut = rut, genders = genders, nationalities = nationalities)

@personal_datum.route("/human_resources/personal_data/<int:rut>", methods=['POST'])
@personal_datum.route("/human_resources/personal_data", methods=['POST'])
def update(rut):
   Employee.update(request.form, rut)

   return redirect(url_for('personal_data.show', rut = rut))

@personal_datum.route("/human_resources/personal_datum/upload/<int:rut>", methods=['POST'])
@personal_datum.route("/human_resources/personal_datum/upload", methods=['POST'])
def upload(rut):
   Dropbox.upload(rut, "_foto", request.files, "/flask_user_photos/", "C:/Users/jesus/OneDrive/Desktop/erpjis_azure/")

   return redirect(url_for('personal_data.show', rut = rut))
