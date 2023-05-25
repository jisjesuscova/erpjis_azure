from flask import Blueprint, render_template, request, redirect, url_for, flash, make_response
from flask_login import login_required, current_user
from app import regular_employee_rol_need
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
from app.total_mesh_data.total_mesh_datum import TotalMeshDatum
import dropbox
from app.settings.setting import Setting
import tempfile
from app.mesh_data.mesh_datum import MeshDatum
from app.users.user import User
from app.helpers.pdf import Pdf

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
      return render_template('human_resource/human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)
   elif current_user.rol_id == 6:
      return render_template('management/human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)

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
      total_mesh_data = TotalMeshDatum.get_by_rut(rut)
   else:
      kardex_data = OldDocumentEmployee.get(rut, '', page, 1)
      settlement_data = OldDocumentEmployee.get(rut, 5, page, '')
      certificates = OldDocumentEmployee.get_by_type(rut, 4, page, [], 2)
      vacations = OldVacation.get(rut, '', '')
      total_mesh_data = TotalMeshDatum.get_by_rut(rut)

   employee = Employee.get(rut)

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee, total_mesh_data = total_mesh_data)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)
   elif current_user.rol_id == 6:
      return render_template('management/human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), kardex_data = kardex_data, certificates = certificates, settlement_data = settlement_data, vacations = vacations, status_id = status_id, employee = employee)

@documental_management_datum.route("/human_resources/documental_management_data/review/<int:page>", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/review", methods=['GET'])
def review(page=1):
   branch_offices = BranchOffice.get()

   values = ['', '', '', '', '']

   if current_user.rol_id == 3:
      documents_employees = DocumentEmployee.get_by_supervisor(current_user.rut, page)

      return render_template('supervisor/human_resources/documental_management_data/review_documental_management_data.html', documents_employees = documents_employees, branch_offices = branch_offices)
   elif current_user.rol_id == 4:
      documents_employees = DocumentEmployee.get_by_human_resource(page, '')

      return render_template('human_resource/human_resources/documental_management_data/review_documental_management_data.html', values = values, documents_employees = documents_employees, branch_offices = branch_offices)

@documental_management_datum.route("/human_resources/documental_management_data/search/<int:page>", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/search", methods=['GET'])
def search(page=1):
   branch_offices = BranchOffice.get()

   if current_user.rol_id == 3:
      documents_employees = DocumentEmployee.get_by_supervisor(current_user.rut, page, request.form)

      return render_template('supervisor/human_resources/documental_management_data/review_documental_management_data.html', documents_employees = documents_employees, branch_offices = branch_offices)
   elif current_user.rol_id == 4:
      rut = request.args.get('rut')
      names = request.args.get('names')
      father_lastname = request.args.get('father_lastname')
      mother_lastname = request.args.get('mother_lastname')
      status_id = request.args.get('status_id')
      branch_office_id = request.args.get('branch_office_id')

      # Crear un arreglo para almacenar los valores
      values = []

      # Agregar los valores obtenidos al arreglo
      values.append(rut)
      values.append(names)
      values.append(father_lastname)
      values.append(mother_lastname)
      values.append(status_id)
      if branch_office_id == '':
         values.append(branch_office_id)
      else:
         values.append(int(branch_office_id))

      documents_employees = DocumentEmployee.get_by_human_resource(page, values)

      return render_template('human_resource/human_resources/documental_management_data/review_documental_management_data_search.html', values = values, documents_employees = documents_employees, branch_offices = branch_offices)

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
      return render_template('human_resource/human_resources/document_requests/document_requests_review.html', document_employee = document_employee, document_type_id = document_type_id, vacation = vacation, employee = employee)

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
      return render_template('human_resource/human_resources/documental_management_data/upload_signed_document.html', id = id, rut = rut)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/documental_management_data/upload_signed_document.html', id = id, rut = rut)
   elif current_user.rol_id == 6:
      return render_template('management/human_resources/documental_management_data/upload_signed_document.html', id = id, rut = rut)

@documental_management_datum.route("/human_resources/documental_management_data/signed_vacation/<int:rut>/<int:id>", methods=['GET'])
def signed_vacation(rut, id):

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)
   elif current_user.rol_id == 6:
      return render_template('management/human_resources/documental_management_data/upload_signed_vacation_document.html', id = id, rut = rut)


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
   if current_user.rol_id == 4:
      if document_type.id == 6 or document_type.id == 36:
         return redirect(url_for('vacations.index', rut=document_employee.rut))
      else:
         return redirect(url_for('documental_management_data.review', page=1))
   if current_user.rol_id == 5:
      return redirect(url_for('documental_management_data.index', rut=request.form['rut']))
   if current_user.rol_id == 6:
      return redirect(url_for('documental_management_data.index', rut=request.form['rut']))
   
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

@documental_management_datum.route("/human_resources/documental_management_data/sign/<rut>/<period>/<int:document_type_id>", methods=['GET'])
def sign(rut, period, document_type_id):
   settings = Setting.get()
   employee = Employee.get(rut)
   user = User.get_by_int_rut(rut)
   total_mesh_datum = TotalMeshDatum.get_one(rut, period)
   id = total_mesh_datum.document_employee_id
   signature_exist = Dropbox.exist('/signature/', employee.signature)
   mesh_data = MeshDatum.get_per_day(rut, period)
   total_mesh_data = TotalMeshDatum.get(rut, period)

   if signature_exist == 1:
   
      signature = Dropbox.get('/signature/', employee.signature)
   
      data = ['', user.visual_rut, '', signature]
   else:
      signature = ''

      data = ['', user.visual_rut, '', signature]

   pdf = Pdf.create_business_hours_pdf('business_hours', data, mesh_data, total_mesh_data)

   with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_file:
      temp_file.write(pdf)

      if document_type_id == 23:
         file_name = 'Horario_Laboral_' + rut + "_" + period + '.pdf'

      file_path = '/business_hours/' + file_name
      dbx = dropbox.Dropbox(settings.dropbox_token)
      with open(temp_file.name, 'rb') as file:
         dbx.files_upload(file.read(), file_path, mode=dropbox.files.WriteMode.overwrite)

   DocumentEmployee.update_file(id, file_name)

   response = make_response(pdf)
   response.headers['Content-Type'] = 'application/pdf'
   response.headers['Content-Disposition'] = 'attachment; filename='+file_name

   return response

@documental_management_datum.route("/human_resources/documental_management_data/delete/<int:id>", methods=['GET'])
def delete(id):
   document_employee = DocumentEmployee.get_by_id(id)
   DocumentEmployee.delete(id)

   if document_employee.support != None:
      Dropbox.delete('/employee_documents/', document_employee.support)

   if document_employee.document_type_id == 6 or document_employee.document_type_id == 36:
      Vacation.delete(id)
      return redirect(url_for('vacations.index', rut = document_employee.rut))

   