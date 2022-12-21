from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
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
   vacations = Vacation.get(rut)
   legal = Vacation.legal(rut)
   taken_days = Vacation.taken_days(rut)
   balance = Vacation.balance(legal, taken_days)

   return render_template('human_resources/vacations/vacations.html', vacations = vacations, rut = rut, legal = legal, balance = balance, taken_days = taken_days)


@vacation.route("/human_resources/vacation/create/<int:rut>", methods=['GET'])
@vacation.route("/human_resources/vacation/create", methods=['GET'])
def create(rut):
   return render_template('human_resources/vacations/vacations_create.html', rut = rut)

@vacation.route("/human_resources/vacation/delete/<int:rut>/<int:id>", methods=['GET'])
@vacation.route("/human_resources/vacation/delete", methods=['GET'])
def delete(rut, id):
   Vacation.delete(id)
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
      support = Dropbox.upload(request.files, "/vacations/", "C:/Users/jesus/OneDrive/Desktop/erp_jis_v1/erp_jis_v1/erp_jis/")
      Vacation.upload(id, support)
      return redirect(url_for('vacations.index', rut = rut))
   else:
      return render_template('human_resources/vacations/vacations_upload.html', rut = rut, id = id)

@vacation.route("/human_resources/vacation/download/<int:rut>/<int:id>", methods=['GET', 'POST'])
@vacation.route("/human_resources/vacation/download", methods=['GET', 'POST'])
def download(rut, id):
   pass