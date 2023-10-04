from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.dropbox_data.dropbox import Dropbox
from app.vacations.vacation import Vacation
from app.documents_employees.document_employee import DocumentEmployee
from app.employees.employee import Employee
from app.helpers.helper import Helper
from app.old_vacations.old_vacation import OldVacation
from app.progressive_vacations.progressive_vacation import ProgressiveVacation

progressive_vacation = Blueprint("progressive_vacations", __name__)

@progressive_vacation.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@progressive_vacation.route("/human_resources/progressive_vacation/create/<int:rut>", methods=['GET'])
@progressive_vacation.route("/human_resources/progressive_vacation/create", methods=['GET'])
def create(rut):
   employees = Employee.get()

   return render_template('human_resource/human_resources/progressive_vacations/progressive_vacations_create.html', rut = rut, employees = employees)

@progressive_vacation.route("/human_resources/progressive_vacation/delete/<int:rut>/<int:id>", methods=['GET'])
@progressive_vacation.route("/human_resources/progressive_vacation/delete", methods=['GET'])
def delete(rut, id):
   document_employee = DocumentEmployee.get_by_id(id)
   DocumentEmployee.delete(id)
   ProgressiveVacation.delete(id)
   Dropbox.delete('/employee_documents/', document_employee.support)

   return redirect(url_for('vacations.index', rut = rut))

@progressive_vacation.route("/human_resources/progressive_vacation/store", methods=['POST'])
def store():
   document_employee_id = DocumentEmployee.store(request.form)
   ProgressiveVacation.store(request.form, document_employee_id)
   
   return redirect(url_for('vacations.index', rut = request.form['rut']))

@progressive_vacation.route("/human_resources/progressive_vacation/upload/<int:rut>/<int:id>", methods=['GET', 'POST'])
@progressive_vacation.route("/human_resources/progressive_vacation/upload", methods=['GET', 'POST'])
def upload(rut, id):
   if request.method == 'POST':
      support = Dropbox.upload(rut, '_vacaciones_progresivas', request.files, "/vacations/", "app/static/dist/files/vacation_data/")
      ProgressiveVacation.upload(id, support)

      if current_user.rol_id == 1:
         return redirect(url_for('documental_management_data.index', rut = rut))
      else:
         return redirect(url_for('progressive_vacations.index', rut = rut))
   else:
      if current_user.rol_id == 1:
         return render_template('collaborator/human_resources/progressive_vacation/progressive_vacations_upload.html', rut = rut, id = id)
      elif current_user.rol_id == 4:
         return render_template('human_resource/human_resources/progressive_vacation/progressive_vacations_upload.html', rut = rut, id = id)

@progressive_vacation.route("/human_resources/progressive_vacation/download/<int:id>", methods=['GET'])
def download(id):
      document_employee = DocumentEmployee.get_by_id(id)
      response = Dropbox.get('/employee_documents/', document_employee.support)

      return redirect(response)