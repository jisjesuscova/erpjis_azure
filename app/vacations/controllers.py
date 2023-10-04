from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.dropbox_data.dropbox import Dropbox
from app.vacations.vacation import Vacation
from app.documents_employees.document_employee import DocumentEmployee
from app.employees.employee import Employee
from app.helpers.helper import Helper
from app.old_vacations.old_vacation import OldVacation
from app.progressive_vacations.progressive_vacation import ProgressiveVacation
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app.old_employees.old_employee import OldEmployee

vacation = Blueprint("vacations", __name__)

@vacation.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@vacation.route("/human_resources/vacations/<int:rut>", methods=['GET'])
@vacation.route("/human_resources/vacations", methods=['GET'])
def index(rut):
   status_id = Helper.is_active(rut)

   if status_id == 1:
      vacations = Vacation.get(rut, '', [3, 4])
      legal = Vacation.legal(rut)
      taken_days = Vacation.taken_days(rut)
      balance = Vacation.balance(legal, taken_days)
      progressive_vacations = ProgressiveVacation.get(rut, '', [3, 4])
      progressive_vacation_legal = ProgressiveVacation.legal(rut)
      progressive_vacation_taken_days = ProgressiveVacation.taken_days(rut)
      progressive_vacation_balance = ProgressiveVacation.balance(progressive_vacation_legal, progressive_vacation_taken_days)
      employee_extra_datum = EmployeeExtraDatum.get(rut)
      employee  = Employee.get(rut)
   else:
      vacations = OldVacation.get(rut, '', [3, 4])
      legal = OldVacation.legal(rut)
      taken_days = OldVacation.taken_days(rut)
      balance = OldVacation.balance(legal, taken_days)
      progressive_vacation_legal = 0
      progressive_vacation_taken_days = 0
      progressive_vacation_balance = 0
      progressive_vacations = []
      employee_extra_datum = []
      employee  = OldEmployee.get(rut)

   vacation_button_status_id = 1

   title = employee.visual_rut + ' - ' + employee.names + ' ' + employee.father_lastname + ' ' + employee.mother_lastname
   module_name = 'Recursos Humanos'

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/vacations/vacations.html', vacation_button_status_id = vacation_button_status_id, vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days, status_id = status_id, progressive_vacation_legal = progressive_vacation_legal, progressive_vacation_taken_days = progressive_vacation_taken_days, progressive_vacation_balance = progressive_vacation_balance, progressive_vacations = progressive_vacations, employee_extra_datum = employee_extra_datum)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/vacations/vacations.html', vacation_button_status_id = vacation_button_status_id, vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days, status_id = status_id, progressive_vacation_legal = progressive_vacation_legal, progressive_vacation_taken_days = progressive_vacation_taken_days, progressive_vacation_balance = progressive_vacation_balance, progressive_vacations = progressive_vacations, employee_extra_datum = employee_extra_datum)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/vacations/vacations.html', vacation_button_status_id = vacation_button_status_id, vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days, status_id = status_id, progressive_vacation_legal = progressive_vacation_legal, progressive_vacation_taken_days = progressive_vacation_taken_days, progressive_vacation_balance = progressive_vacation_balance, progressive_vacations = progressive_vacations, employee_extra_datum = employee_extra_datum)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/vacations/vacations.html', title = title, module_name = module_name, vacation_button_status_id = vacation_button_status_id, vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days, status_id = status_id, progressive_vacation_legal = progressive_vacation_legal, progressive_vacation_taken_days = progressive_vacation_taken_days, progressive_vacation_balance = progressive_vacation_balance, progressive_vacations = progressive_vacations, employee_extra_datum = employee_extra_datum)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/vacations/vacations.html', title = title, module_name = module_name, vacation_button_status_id = vacation_button_status_id, vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days, status_id = status_id, progressive_vacation_legal = progressive_vacation_legal, progressive_vacation_taken_days = progressive_vacation_taken_days, progressive_vacation_balance = progressive_vacation_balance, progressive_vacations = progressive_vacations, employee_extra_datum = employee_extra_datum)
   elif current_user.rol_id == 6:
      return render_template('management/human_resources/vacations/vacations.html', title = title, module_name = module_name, vacation_button_status_id = vacation_button_status_id, vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days, status_id = status_id, progressive_vacation_legal = progressive_vacation_legal, progressive_vacation_taken_days = progressive_vacation_taken_days, progressive_vacation_balance = progressive_vacation_balance, progressive_vacations = progressive_vacations, employee_extra_datum = employee_extra_datum)

@vacation.route("/human_resources/vacation/create/<int:rut>", methods=['GET'])
@vacation.route("/human_resources/vacation/create", methods=['GET'])
def create(rut):
   employees = Employee.get()

   return render_template('human_resource/human_resources/vacations/vacations_create.html', rut = rut, employees = employees)

@vacation.route("/human_resources/vacation/delete/<int:rut>/<int:id>", methods=['GET'])
@vacation.route("/human_resources/vacation/delete", methods=['GET'])
def delete(rut, id):
   document_employee = DocumentEmployee.get_by_id(id)
   DocumentEmployee.delete(id)
   Vacation.delete(id)
   Dropbox.delete('/employee_documents/', document_employee.support)

   flash('La vacación ha sido borrada con éxito', 'success')

   return redirect(url_for('vacations.index', rut = rut))

@vacation.route("/human_resources/vacation/store", methods=['POST'])
def store():
   document_employee_id = DocumentEmployee.store(request.form)
   status_id = Vacation.store(request.form, document_employee_id)

   flash('La vacación ha sido registrada con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'

@vacation.route("/human_resources/vacation/upload/<int:rut>/<int:id>", methods=['GET', 'POST'])
@vacation.route("/human_resources/vacation/upload", methods=['GET', 'POST'])
def upload(rut, id):
   if request.method == 'POST':
      support = Dropbox.upload(rut, '_vacation', request.files, "/employee_documents/", "app/static/dist/files/vacation_data/")
      Vacation.upload(id, support)

      if current_user.rol_id == 1:
         return redirect(url_for('documental_management_data.index', rut = rut))
      else:
         return redirect(url_for('vacations.index', rut = rut))
   else:
      if current_user.rol_id == 1:
         return render_template('collaborator/human_resources/vacations/vacations_upload.html', rut = rut, id = id)
      elif current_user.rol_id == 4:
         return render_template('human_resource/human_resources/vacations/vacations_upload.html', rut = rut, id = id)

@vacation.route("/human_resources/vacation/download/<int:id>", methods=['GET'])
def download(id):
      document_employee = DocumentEmployee.get_by_id(id)
      response = Dropbox.get('/employee_documents/', document_employee.support)

      return redirect(response)