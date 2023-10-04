from flask import Blueprint, render_template, redirect, request, url_for, flash
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
from app.helpers.file import File
from app.employees.employee import Employee
from app.old_employees.old_employee import OldEmployee
from app.documentation_titles.documentation_title import DocumentationTitle

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
   documentation_titles_menu = DocumentationTitle.get()

   if status_id == 1:
      kardex_data = DocumentEmployee.get(rut, '', page, 1)
      employee  = Employee.get(rut)

      is_active = 1
   else:
      kardex_data = OldDocumentEmployee.get(rut, '', page, 1)
      employee  = OldEmployee.get(rut)

      is_active = 0

   kardex_button_status_id = 1

   title = employee.visual_rut + ' - ' + employee.names + ' ' + employee.father_lastname + ' ' + employee.mother_lastname
   module_name = 'Recursos Humanos'

   return render_template('human_resource/human_resources/kardex_data/kardex_data.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, kardex_button_status_id = kardex_button_status_id, kardex_data = kardex_data, rut = rut, is_active = is_active)

@kardex_datum.route("/human_resources/kardex_data/create/<int:rut>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/create", methods=['GET'])
def create(rut):
   documentation_titles_menu = DocumentationTitle.get()
   document_types = DocumentType.get('', 1, '', '')

   return render_template('human_resource/human_resources/kardex_data/kardex_data_create.html', documentation_titles_menu = documentation_titles_menu, rut = rut, document_types = document_types)

@kardex_datum.route("/human_resources/kardex_data/edit/<int:rut>/<int:id>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/edit", methods=['GET'])
def edit(rut, id):
   documentation_titles_menu = DocumentationTitle.get()
   KardexDatum.get(id, '')

   return render_template('human_resources/kardex_data/kardex_data_edit.html', rut = rut, documentation_titles_menu = documentation_titles_menu)

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
   File.delete("app/static/dist/files/kardex_data/", document_employee.support)

   flash('El registro ha sido borrado con éxito', 'success')

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

   support = Dropbox.upload(request.form['rut'], file_name, request.files, "/employee_documents/", "app/static/dist/files/kardex_data/", 0)
   
   if support != 0:
      status_id = KardexDatum.store(request.form, support)

   flash('El documento se ha guardado con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'