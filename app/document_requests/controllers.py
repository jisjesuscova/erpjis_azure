from flask import Blueprint, render_template, redirect, request, url_for, flash, send_file, make_response
from flask_login import login_required
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

   return render_template('human_resources/document_requests/document_requests_create.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employees = employees)

@document_request.route("/human_resources/document_requests/store", methods=['POST'])
def store():
   document_id = DocumentRequest.store(request.form)
   DocumentRequest.storebytype(document_id, request.form)

   flash('Se ha solicitado el documento con éxito.', 'success')

   return redirect(url_for('documental_management_data.index'))

@document_request.route("/human_resources/document_request/detail/<int:rut>/<int:id>", methods=['GET'])
@document_request.route("/human_resources/document_request/detail", methods=['GET'])
def detail(rut = '', id = ''):
   document_type = DocumentType.get(id, 2)
   branch_offices = BranchOffice.get()
   job_positions = JobPosition.get()
   employee = Employee.get(rut)

   return render_template('human_resources/document_requests/document_requests_review.html', document_type = document_type, branch_offices = branch_offices, job_positions = job_positions, employee = employee)

@document_request.route("/human_resources/document_request/download/<int:id>", methods=['GET'])
def download(id):
   document_employee = DocumentEmployee.get_by_id(id)
   if document_employee.document_type_id == 1:
      employee = Employee.get(document_employee.rut)
      information_letter = InformationLetter.get(document_employee.id)

      full_name = employee.names + " " + employee.father_lastname + " " + employee.mother_lastname
      rut = employee.visual_rut
      description = information_letter.description
      data = [full_name, rut, description]

      pdf = Pdf.create_pdf('warning_letter', data)
   elif document_employee.document_type_id == 2:
      employee = Employee.get(document_employee.rut)
      employee_labor_datum = EmployeeLaborDatum.get(document_employee.rut)

      full_name = employee.names + " " + employee.father_lastname + " " + employee.mother_lastname
      rut = employee.visual_rut
      entrance_company = employee_labor_datum.entrance_company
      data = [full_name, rut, entrance_company]

      pdf = Pdf.create_pdf('antique_certification', data)

   response = make_response(pdf)
   response.headers['Content-Type'] = 'application/pdf'
   response.headers['Content-Disposition'] = 'attachment; filename=document.pdf'

   return response