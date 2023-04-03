from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.models.models import EmployeeModel
from app.document_types.document_type import DocumentType
from app.branch_offices.branch_office import BranchOffice
from app.documents_employees.document_employee import DocumentEmployee
from app.vacations.vacation import Vacation
from app.employees.employee import Employee
from app.dropbox_data.dropbox import Dropbox
from datetime import datetime
from app.helpers.helper import Helper
from app.old_documents_employees.old_document_employee import OldDocumentEmployee
from app.old_vacations.old_vacation import OldVacation

documental_management_datum = Blueprint("documental_management_data", __name__)

@documental_management_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@documental_management_datum.route("/human_resources/documental_management_datum/create", methods=['GET'])
def create():
   if current_user.rol_id == 1:
      document_type_values = [2, 4]

      document_types = DocumentType.get('', 2, '', '', document_type_values)
   else:
      document_types = DocumentType.get('', 2, '', '', '')
   
   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)

@documental_management_datum.route("/human_resources/documental_management_data", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/<int:page>", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/<int:rut>", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/<int:rut>/<int:page>", methods=['GET'])
def index(rut = '', page=1):
   status_id = Helper.is_active(rut)

   if status_id == 1:
      kardex_data = DocumentEmployee.get(rut, '', page, 1)
      settlement_data = DocumentEmployee.get(rut, 5, page, '')
      certificates = DocumentEmployee.get_by_type(rut, 4, page, [], 2)
      vacations = Vacation.get(rut, '', '')
   else:
      kardex_data = OldDocumentEmployee.get(rut, '', page, 1)
      settlement_data = OldDocumentEmployee.get(rut, 5, page, '')
      certificates = OldDocumentEmployee.get_by_type(rut, 4, page, [], 2)
      vacations = OldVacation.get(rut, '', '')

   employee = Employee.get(rut)

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)

@documental_management_datum.route("/human_resources/documental_management_data/review/<int:page>", methods=['GET'])
def review(page=1):
   branch_offices = BranchOffice.get()

   if current_user.rol_id == 3:
      documents_employees = DocumentEmployee.get_by_supervisor(current_user.rut, page)

      return render_template('supervisor/human_resources/documental_management_data/review_documental_management_data.html', documents_employees = documents_employees, branch_offices = branch_offices)
   elif current_user.rol_id == 4:
      documents_employees = DocumentEmployee.get_by_administrator(current_user.rut, page)

      return render_template('administrator/human_resources/documental_management_data/review_documental_management_data.html', documents_employees = documents_employees, branch_offices = branch_offices)

@documental_management_datum.route("/human_resources/documental_management_data/search/<int:page>", methods=['POST'])
def search(page=1):
   branch_offices = BranchOffice.get()

   if current_user.rol_id == 3:
      documents_employees = DocumentEmployee.get_by_supervisor(current_user.rut, page, request.form)

      return render_template('supervisor/human_resources/documental_management_data/review_documental_management_data.html', documents_employees = documents_employees, branch_offices = branch_offices)
   elif current_user.rol_id == 4:
      documents_employees = DocumentEmployee.get_by_administrator(current_user.rut, page, request.form)

      return render_template('administrator/human_resources/documental_management_data/review_documental_management_data.html', documents_employees = documents_employees, branch_offices = branch_offices)

@documental_management_datum.route("/human_resources/documental_management_data/show/<int:id>", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/show", methods=['GET'])
def show(id, page=1):

   document_employee = DocumentEmployee.get_by_id(id)
   document_type_id = document_employee.document_type_id
   employee = Employee.get(document_employee.rut)

   if document_type_id == 6:
      vacation = Vacation.get_by_document(document_employee.id)
   else:
      vacation = ''

   if current_user.rol_id == 3:
      return render_template('supervisor/human_resources/document_requests/document_requests_review.html', document_employee = document_employee, document_type_id = document_type_id, vacation = vacation, employee = employee)
   else:
      return render_template('administrator/human_resources/document_requests/document_requests_review.html', document_employee = document_employee, document_type_id = document_type_id, vacation = vacation, employee = employee)

@documental_management_datum.route("/human_resources/documental_management_data/signed/<int:rut>/<int:id>", methods=['GET'])
def signed(rut, id):
   print(current_user.rol_id )
   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/documental_management_data/upload_signed_document.html', id = id, rut = rut)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/documental_management_data/upload_signed_document.html', id = id, rut = rut)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/documental_management_data/upload_signed_document.html', id = id, rut = rut)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/documental_management_data/upload_signed_document.html', id = id, rut = rut)

@documental_management_datum.route("/human_resources/documental_management_data/signed_vacation/<int:rut>/<int:id>", methods=['GET'])
def signed_vacation(rut, id):
   print(current_user.rol_id )
   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)


@documental_management_datum.route("/human_resources/documental_management_data/upload", methods=['POST'])
def upload():
   document_employee = DocumentEmployee.get_by_id(request.form['id'])
   document_type = DocumentType.get(document_employee.document_type_id)

   file_name = "_" + document_type.document_type + "_" + str(datetime.now())

   if request.files['file'].filename != '':
      support = Dropbox.upload(request.form['rut'], 'papeleta_vacaciones', request.files, "/employee_documents/", "app/static/dist/files/document_data/", 0)
      DocumentEmployee.sign(request.form['id'], request.form['rut'], support)

   flash('El documento ha sido subido con éxito', 'success')

   if current_user.rol_id == 1:
      return redirect(url_for('documental_management_data.index', rut=request.form['rut']))
   if current_user.rol_id == 2:
      return redirect(url_for('documental_management_data.index', rut=request.form['rut']))
   if current_user.rol_id == 3:
      return redirect(url_for('documental_management_data.index', rut=request.form['rut']))
   elif current_user.rol_id == 4:
      if document_type.id == 6 or document_type.id == 36:
         return redirect(url_for('vacations.index', rut=document_employee.rut))
      else:
         return redirect(url_for('documental_management_data.review', page=1))

@documental_management_datum.route("/human_resources/documental_management_data/upload_vacation", methods=['POST'])
def upload_vacation():
   document_employee = DocumentEmployee.get_by_id(request.form['id'])
   document_type = DocumentType.get(document_employee.document_type_id)

   file_name = "_" + document_type.document_type + "_" + str(datetime.now())

   support = Dropbox.upload(request.form['rut'], 'papeleta_vacaciones', request.files, "/employee_documents/", "app/static/dist/files/vacation_data/", 0)
   status_id = DocumentEmployee.sign_vacation(request.form['id'], request.form['rut'], support)
   
   flash('El documento ha sido subido con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'
      
@documental_management_datum.route("/human_resources/documental_management_data/download/<int:id>", methods=['GET'])
def download(id):
   document_employee = DocumentEmployee.get_by_id(id)

   response = Dropbox.get('/employee_documents/', document_employee.support)

   return redirect(response)

@documental_management_datum.route("/human_resources/documental_management_data/delete/<int:id>", methods=['GET'])
def delete(id):
   document_employee = DocumentEmployee.get_by_id(id)
   DocumentEmployee.delete(id)

   if document_employee.support != None:
      Dropbox.delete('/employee_documents/', document_employee.support)

   if document_employee.document_type_id == 6 or document_employee.document_type_id == 36:
      Vacation.delete(id)
      return redirect(url_for('vacations.index', rut = document_employee.rut))

   