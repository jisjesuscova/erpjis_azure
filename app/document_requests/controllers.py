from flask import Blueprint, render_template, redirect, request, url_for, flash, send_file, make_response
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.document_types.document_type import DocumentType
from app.branch_offices.branch_office import BranchOffice
from app.job_positions.job_position import JobPosition
from app.document_requests.document_request import DocumentRequest
from app.documents_employees.document_employee import DocumentEmployee
from app.employees.employee import Employee
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.helpers.pdf import Pdf
from app.information_letters.information_letter import InformationLetter
from app.vacations.vacation import Vacation
from app.dropbox_data.dropbox import Dropbox
from app.helpers.whatsapp import Whatsapp
from app.progressive_vacations.progressive_vacation import ProgressiveVacation
import pdfkit
from datetime import datetime
from app.helpers.helper import Helper
from app.job_positions.job_position import JobPosition
from app.employee_types.employee_type import EmployeeType
from app.mesh_data.mesh_datum import MeshDatum
from app.users.user import User
import tempfile
import dropbox
from app.settings.setting import Setting

document_request = Blueprint("document_requests", __name__)

@document_request.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@document_request.route("/human_resources/document_requests/<int:id>", methods=['GET'])
@document_request.route("/human_resources/document_requests", methods=['GET'])
def show(id):
   document_type = DocumentType.get(id, 2)
   branch_offices = BranchOffice.get()
   job_positions = JobPosition.get()
   employees = Employee.get()

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/document_requests/document_requests_create.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employees = employees, id = id)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/document_requests/document_requests_create.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employees = employees, id = id)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/document_requests/document_requests_create.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employees = employees, id = id)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/document_requests/document_requests_create.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employees = employees, id = id)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/document_requests/document_requests_create.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employees = employees, id = id)
   elif current_user.rol_id == 6:
      return render_template('management/human_resources/document_requests/document_requests_create.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employees = employees, id = id)


@document_request.route("/human_resources/document_requests/store", methods=['POST'])
def store():
   document_id = DocumentRequest.store(request.form)

   document_employee = DocumentEmployee.get_by_id(document_id)

   if document_employee.document_type_id == 6:
      Vacation.store(request.form, document_id)

   if current_user.rol_id == 1 or current_user.rol_id == 2:
      Whatsapp.send(document_id, request.form['answer'], 1, 13)
   else:
      Whatsapp.send(document_id, request.form['answer'], 1, 14)

   flash('Se ha solicitado el documento con éxito.', 'success')

   return redirect(url_for('documental_management_data.index', rut=request.form['rut']))

@document_request.route("/human_resources/document_request/review/<id>", methods=['GET'])
@document_request.route("/human_resources/document_request/review", methods=['POST'])
def review(id = ''):
   if id != '':
      DocumentRequest.status(id, '', 5)
   else:
      id = request.form['id']
      
      if current_user.rol_id == 3:
         DocumentRequest.status(id, request.form, 2)

         Whatsapp.send(id, request.form['answer'], 1, 14)
      else:
         DocumentRequest.status(id, request.form, 3)

         Whatsapp.send(id, request.form['answer'], 1, 15)

      if request.form['document_type_id'] == '6':
         Vacation.request(id, request.form)

   flash('Se ha aceptado el documento con éxito.', 'success')

   return redirect(url_for('documental_management_data.review', page=1))

@document_request.route("/human_resources/document_request/reject/<id>/<type_id>", methods=['GET'])
def reject(id = '', type_id = ''):
   Whatsapp.send(id, '1', 1, 16)

   DocumentEmployee.delete(id)

   if type_id == '6':
      Vacation.delete_by_document_id(id)
   
   flash('Se ha rechazado el documento.', 'success')

   return redirect(url_for('documental_management_data.review', page=1))

@document_request.route("/human_resources/document_request/detail/<int:rut>/<int:id>", methods=['GET'])
@document_request.route("/human_resources/document_request/detail", methods=['GET'])
def detail(rut = '', id = ''):
   document_type = DocumentType.get(id, 2)
   branch_offices = BranchOffice.get()
   job_positions = JobPosition.get()
   employee = Employee.get(rut)

   return render_template('human_resources/document_requests/document_requests_review.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employee = employee)

@document_request.route("/human_resources/document_request/download_mesh/<rut>/<period>", methods=['GET'])
def download_mesh(rut, period):
   settings = Setting.get()
   employee = Employee.get(rut)

   user = User.get_by_int_rut(rut)

   signature_exist = Dropbox.exist('/signature/', employee.signature)

   if signature_exist == 1:
   
      signature = Dropbox.get('/signature/', employee.signature)
   
      data = ['', user.visual_rut, '', signature]
   else:
      signature = ''

      data = ['', user.visual_rut, '', signature]

   mesh_data = MeshDatum.get_per_day(rut, period)

   pdf = Pdf.create_business_hours_pdf('business_hours', data, mesh_data)

   with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_file:
      temp_file.write(pdf)

      file_path = '/business_hours/horario.pdf'  # Ruta y nombre de archivo en Dropbox
      dbx = dropbox.Dropbox(settings.dropbox_token)
      with open(temp_file.name, 'rb') as file:
         dbx.files_upload(file.read(), file_path, mode=dropbox.files.WriteMode.overwrite)

   response = make_response(pdf)
   response.headers['Content-Type'] = 'application/pdf'
   response.headers['Content-Disposition'] = 'attachment; filename=horario.pdf'

   return response

@document_request.route("/human_resources/document_request/download/<int:id>", methods=['GET'])
def download(id):
   document_employee = DocumentEmployee.get_by_id(id)

   if document_employee.document_type_id == 1:
      employee = Employee.get(document_employee.rut)
      information_letter = InformationLetter.get(document_employee.id)

      full_name = employee.names + " " + employee.father_lastname + " " + employee.mother_lastname
      rut = employee.visual_rut
      description = information_letter.description

      signature_exist = Dropbox.exist('/signature/', employee.signature)

      if signature_exist == 1:
   
         signature = Dropbox.get('/signature/', employee.signature)
   
         data = [full_name, rut, description, signature]
      else:
         signature = ''

         data = [full_name, rut, description, signature]

      pdf = Pdf.create_pdf('warning_letter', data)
   elif document_employee.document_type_id == 4:
      employee = Employee.get(document_employee.rut)
      employee_labor_datum = EmployeeLaborDatum.get(document_employee.rut)
      job_position = JobPosition.get(employee_labor_datum.job_position_id)
      employee_type = EmployeeType.get(employee_labor_datum.employee_type_id)

      full_name = employee.names + " " + employee.father_lastname + " " + employee.mother_lastname
      rut = employee.visual_rut
      entrance_company = str(employee_labor_datum.entrance_company)
      entrance_company = entrance_company.split('-')
      entrance_company = entrance_company[2] + "-" + entrance_company[1] + "-" + entrance_company[0]
      signature = employee.signature

      signature_exist = Dropbox.exist('/signature/', employee.signature)

      current_date = datetime.now().strftime('%Y-%m-%d')

      current_date = Helper.document_date(str(current_date))

      entrance_date = Helper.document_date(str(employee_labor_datum.entrance_company))

      if signature_exist == 1:
         
         signature = Dropbox.get('/signature/', employee.signature)

         data = [full_name, rut, entrance_company, signature, current_date, job_position.job_position, employee_type.employee_type, entrance_date]

      else:
         signature = ''

         data = [full_name, rut, entrance_company, signature, current_date, job_position.job_position, employee_type.employee_type, entrance_date]

      pdf = Pdf.create_pdf('antique_certification', data)

      response = make_response(pdf)
      response.headers['Content-Type'] = 'application/pdf'
      response.headers['Content-Disposition'] = 'attachment; filename=document.pdf'

   elif document_employee.document_type_id == 6:
      employee = Employee.get(document_employee.rut)
      employee_labor_datum = EmployeeLaborDatum.get(document_employee.rut)

      full_name = employee.names + " " + employee.father_lastname + " " + employee.mother_lastname
      rut = employee.visual_rut
      entrance_company = str(employee_labor_datum.entrance_company)
      entrance_company = entrance_company.split('-')
      entrance_company = entrance_company[2] + "-" + entrance_company[1] + "-" + entrance_company[0]
      legal = Vacation.legal(document_employee.rut)
      taken_days = Vacation.taken_days(document_employee.rut)
      balance = Vacation.balance(legal, taken_days)
      signature = employee.signature

      vacations = Vacation.get_by_major(document_employee.rut, '', 2, 10)

      total_vacations = Vacation.get_total(document_employee.rut, 2)

      signature_exist = Dropbox.exist('/signature/', employee.signature)
      
      if signature_exist == 1:
         signature = Dropbox.get('/signature/', employee.signature)
       
         data = [full_name, rut, entrance_company, signature, legal, taken_days, balance]
      else:
         signature = ''

         data = [full_name, rut, entrance_company, signature, legal, taken_days, balance]

      pdf = Pdf.create_vacation_pdf('vacation', data, vacations, total_vacations)

      response = make_response(pdf)
      response.headers['Content-Type'] = 'application/pdf'
      response.headers['Content-Disposition'] = 'attachment; filename=vacations.pdf'

   elif document_employee.document_type_id == 36:
      employee = Employee.get(document_employee.rut)
      employee_labor_datum = EmployeeLaborDatum.get(document_employee.rut)

      full_name = employee.names + " " + employee.father_lastname + " " + employee.mother_lastname
      rut = employee.visual_rut
      entrance_company = str(employee_labor_datum.entrance_company)
      entrance_company = entrance_company.split('-')
      entrance_company = entrance_company[2] + "-" + entrance_company[1] + "-" + entrance_company[0]
      legal = ProgressiveVacation.legal(document_employee.rut)
      taken_days = ProgressiveVacation.taken_days(document_employee.rut)
      balance = ProgressiveVacation.balance(legal, taken_days)
      signature = employee.signature

      vacations = ProgressiveVacation.get_by_major(document_employee.rut, '', 2, 10)

      total_vacations = ProgressiveVacation.get_total(document_employee.rut, 2)

      signature_exist = Dropbox.exist('/signature/', employee.signature)
      
      if signature_exist == 1:
         signature = Dropbox.get('/signature/', employee.signature)
       
         data = [full_name, rut, entrance_company, signature, legal, taken_days, balance]
      else:
         signature = ''

         data = [full_name, rut, entrance_company, signature, legal, taken_days, balance]

      pdf = Pdf.create_vacation_pdf('progressive_vacation', data, vacations, total_vacations)

      response = make_response(pdf)
      response.headers['Content-Type'] = 'application/pdf'
      response.headers['Content-Disposition'] = 'attachment; filename=document.pdf'

   return response