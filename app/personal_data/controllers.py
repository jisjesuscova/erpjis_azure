from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.genders.gender import Gender
from app.nationalities.nationality import Nationality
from app.dropbox_data.dropbox import Dropbox
from app.users.user import User
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from PIL import Image
from app.banks.bank import Bank
import os
from app.old_employees.old_employee import OldEmployee
from app.old_employee_labor_data.old_employee_labor_datum import OldEmployeeLaborDatum
from app.helpers.helper import Helper
from app.employee_bank_accounts.employee_bank_account import EmployeeBankAccount
from app.documentation_titles.documentation_title import DocumentationTitle

personal_datum = Blueprint("personal_data", __name__)

@personal_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@personal_datum.route("/human_resources/personal_data/<int:rut>", methods=['GET'])
@personal_datum.route("/human_resources/personal_data", methods=['GET'])
def show(rut):
   status_id = Helper.is_active(rut)

   documentation_titles_menu = DocumentationTitle.get()

   if status_id == 1:
      employee = Employee.get(rut)
      employee_labor_datum = EmployeeLaborDatum.get(rut)
      genders = Gender.get()
      nationalities = Nationality.get()
      employee_bank_account = EmployeeBankAccount.get(rut)
      requested_employee_bank_account = EmployeeBankAccount.get_change_requested(rut)

      empty_field_status_id = Employee.empty_fields(rut)

      if employee.picture != '' and employee.picture != None:
         download_url = Dropbox.get('/pictures/', employee.picture)
      else:
         download_url = url_for("static", filename="dist/img/logo.png")
      
      if employee.signature != '' and employee.signature != None:
         signature_exist = Dropbox.exist('/signature/', employee.signature)

         if signature_exist == 1:
            signature = Dropbox.get('/signature/', employee.signature)
         else:
            signature = ''
      else:
         signature_exist = 0
         signature = ''

      is_active = 1
   else:
      employee = OldEmployee.get(rut)
      employee_labor_datum = OldEmployeeLaborDatum.get(rut)
      genders = Gender.get()
      nationalities = Nationality.get()
      employee_bank_account = EmployeeBankAccount.get(rut)
      requested_employee_bank_account = EmployeeBankAccount.get_change_requested(rut)

      empty_field_status_id = 1

      if employee.picture != '' and employee.picture != None:
         download_url = Dropbox.get('/pictures/', employee.picture)
      else:
         download_url = url_for("static", filename="dist/img/logo.png")
      
      if employee.signature != '' and employee.signature != None:
         signature_exist = Dropbox.exist('/signatures/', employee.signature)

         if signature_exist == 1:
            signature = Dropbox.get('/signatures/', employee.signature)
         else:
            signature = ''
      else:
         signature_exist = 0
         signature = ''

      is_active = 0

   banks = Bank.get()

   status_change_bank_account_id = EmployeeBankAccount.get_status(rut)

   personal_datum_button_status_id = 1

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/personal_data/personal_data_update.html', documentation_titles_menu = documentation_titles_menu, banks = banks, employee_bank_account = employee_bank_account, personal_datum_button_status_id = personal_datum_button_status_id, employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature, is_active = is_active)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/personal_data/personal_data_update.html', documentation_titles_menu = documentation_titles_menu, banks = banks, employee_bank_account = employee_bank_account, personal_datum_button_status_id = personal_datum_button_status_id, employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature, is_active = is_active)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/personal_data/personal_data_update.html', documentation_titles_menu = documentation_titles_menu, banks = banks, employee_bank_account = employee_bank_account, personal_datum_button_status_id = personal_datum_button_status_id, employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature, is_active = is_active)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/personal_data/personal_data_update.html', documentation_titles_menu = documentation_titles_menu, requested_employee_bank_account = requested_employee_bank_account, status_change_bank_account_id = status_change_bank_account_id, banks = banks, employee_bank_account = employee_bank_account, empty_field_status_id = empty_field_status_id, personal_datum_button_status_id = personal_datum_button_status_id, employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature, is_active = is_active)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/personal_data/personal_data_update.html', documentation_titles_menu = documentation_titles_menu, requested_employee_bank_account = requested_employee_bank_account, status_change_bank_account_id = status_change_bank_account_id, banks = banks, employee_bank_account = employee_bank_account, empty_field_status_id = empty_field_status_id, personal_datum_button_status_id = personal_datum_button_status_id, employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature, is_active = is_active)
   elif current_user.rol_id == 6:
      return render_template('management/human_resources/personal_data/personal_data_update.html', documentation_titles_menu = documentation_titles_menu, requested_employee_bank_account = requested_employee_bank_account, status_change_bank_account_id = status_change_bank_account_id, banks = banks, employee_bank_account = employee_bank_account, empty_field_status_id = empty_field_status_id, personal_datum_button_status_id = personal_datum_button_status_id, employee = employee, rut = rut, genders = genders, nationalities = nationalities, download_url = download_url, employee_labor_datum = employee_labor_datum, signature_exist = signature_exist, signature = signature, is_active = is_active)

@personal_datum.route("/human_resources/personal_data/<int:rut>", methods=['POST'])
@personal_datum.route("/human_resources/personal_data", methods=['POST'])
def update(rut):
   
   if 'file' in request.files:
      if request.files['file'].filename != '':
         picture = Dropbox.upload(rut, "_photo", request.files, "/pictures/", "app/static/dist/files/picture_data/", 1)
         Employee.upload(rut, picture)

   status_id = Employee.update(request.form, rut)

   flash('Se ha actualizado con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'

@personal_datum.route("/human_resources/personal_datum/delete_picture/<int:rut>", methods=['GET'])
@personal_datum.route("/human_resources/personal_datum/delete_picture", methods=['GET'])
def delete_picture(rut):
   employee = Employee.get(rut)

   if employee.picture != None:
      Dropbox.delete("/pictures/", employee.picture)
      Employee.delete_picture(rut)
   
   return redirect(url_for('personal_data.show', rut = rut))
