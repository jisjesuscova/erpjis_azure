from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.kardex_data.kardex_datum import KardexDatum
from app.document_types.document_type import DocumentType
from app.dropbox_data.dropbox import Dropbox
from datetime import datetime
from app.documents_employees.document_employee import DocumentEmployee
from app.old_documents_employees.old_document_employee import OldDocumentEmployee
from app.helpers.helper import Helper

kardex_datum = Blueprint("kardex_data", __name__)

@kardex_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@kardex_datum.route("/human_resources/kardex_data/<int:rut>/<int:page>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/<int:rut>", methods=['GET'])
def index(rut, page = 1):
   status_id = Helper.is_active(rut)

   if status_id == 1:
      kardex_data = DocumentEmployee.get(rut, '', page, 1)

      is_active = 1
   else:
      kardex_data = OldDocumentEmployee.get(rut, '', page, 1)

      is_active = 0

   return render_template('administrator/human_resources/kardex_data/kardex_data.html', kardex_data = kardex_data, rut = rut, is_active = is_active)

@kardex_datum.route("/human_resources/kardex_data/create/<int:rut>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/create", methods=['GET'])
def create(rut):
   document_types = DocumentType.get('', 1, '', '')

   return render_template('administrator/human_resources/kardex_data/kardex_data_create.html', rut = rut, document_types = document_types)

@kardex_datum.route("/human_resources/kardex_data/edit/<int:rut>/<int:id>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/edit", methods=['GET'])
def edit(rut, id):
   KardexDatum.get(id, '')

   return render_template('human_resources/kardex_data/kardex_data_edit.html', rut = rut)

@kardex_datum.route("/human_resources/kardex_data/update/<int:rut>/<int:id>", methods=['POST'])
@kardex_datum.route("/human_resources/kardex_data/update", methods=['POST'])
def update(rut, id):
   KardexDatum.update(id, request.form)

   return redirect(url_for('kardex_data.index', rut = rut))

@kardex_datum.route("/human_resources/kardex_data/delete/<int:rut>/<int:id>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/delete", methods=['GET'])
def delete(rut, id):
   document_employee = DocumentEmployee.get_by_id(id)
   
   DocumentEmployee.delete(id)

   Dropbox.delete('/employee_documents/', document_employee.support)

   return redirect(url_for('kardex_data.index', rut = rut))

@kardex_datum.route("/human_resources/kardex_data/download/<int:id>/<int:rut>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/download", methods=['GET'])
def download(id, rut):
   status_id = Helper.is_active(rut)

   if status_id == 1:
      document_employee = DocumentEmployee.get_by_id(id)
   else:
      document_employee = OldDocumentEmployee.get_by_id(id)

   response = Dropbox.get('/employee_documents/', document_employee.support)

   return redirect(response)

@kardex_datum.route("/human_resources/kardex_datum/store", methods=['POST'])
def store():
   document_type = DocumentType.get(request.form['document_type_id'])

   file_name = "_" + document_type.document_type + "_kardex"

   support = Dropbox.upload(request.form['rut'], file_name, request.files, "/employee_documents/", "C:/Users/jesus/OneDrive/Desktop/erpjis_azure/")
   if support != 0:
      KardexDatum.store(request.form, support)

   return redirect(url_for('kardex_data.index', rut = request.form['rut']))