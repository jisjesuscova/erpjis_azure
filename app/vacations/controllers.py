from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.dropbox_data.dropbox import Dropbox
from app.vacations.vacation import Vacation
from app.documents_employees.document_employee import DocumentEmployee
from datetime import datetime

vacation = Blueprint("vacations", __name__)

@vacation.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@vacation.route("/human_resources/vacations/<int:rut>", methods=['GET'])
@vacation.route("/human_resources/vacations", methods=['GET'])
def index(rut):
   vacations = Vacation.get(rut, '', 4)
   legal = Vacation.legal(rut)
   taken_days = Vacation.taken_days(rut)
   balance = Vacation.balance(legal, taken_days)

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/vacations/vacations.html', vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/vacations/vacations.html', vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/vacations/vacations.html', vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/vacations/vacations.html', vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days)

@vacation.route("/human_resources/vacation/create/<int:rut>", methods=['GET'])
@vacation.route("/human_resources/vacation/create", methods=['GET'])
def create(rut):
   return render_template('human_resources/vacations/vacations_create.html', rut = rut)

@vacation.route("/human_resources/vacation/delete/<int:rut>/<int:id>", methods=['GET'])
@vacation.route("/human_resources/vacation/delete", methods=['GET'])
def delete(rut, id):
   document_employee = DocumentEmployee.get_by_id(id)
   DocumentEmployee.delete(id)
   Vacation.delete(id)
   Dropbox.delete('/employee_documents/', document_employee.support)

   return redirect(url_for('vacations.index', rut = rut))

@vacation.route("/human_resources/vacation/store/<int:rut>", methods=['POST'])
@vacation.route("/human_resources/vacation/store", methods=['POST'])
def store(rut):
   document_employee_id = DocumentEmployee.store(request.form)
   Vacation.store(request.form, document_employee_id)

   return redirect(url_for('vacations.index', rut = rut))

@vacation.route("/human_resources/vacation/upload/<int:rut>/<int:id>", methods=['GET', 'POST'])
@vacation.route("/human_resources/vacation/upload", methods=['GET', 'POST'])
def upload(rut, id):
   if request.method == 'POST':
      support = Dropbox.upload(rut, '_vacation', request.files, "/vacations/", "C:/Users/jesus/OneDrive/Desktop/erp_azure/")
      Vacation.upload(id, support)
      return redirect(url_for('vacations.index', rut = rut))
   else:
      return render_template('human_resources/vacations/vacations_upload.html', rut = rut, id = id)

@vacation.route("/human_resources/vacation/download/<int:id>", methods=['GET'])
def download(id):
      document_employee = DocumentEmployee.get_by_id(id)
      response = Dropbox.get('/employee_documents/', document_employee.support)

      return redirect(response)