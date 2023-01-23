from flask import Blueprint, render_template, redirect, request, url_for, make_response
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.contract_data.contract_datum import ContractDatum
from app.contract_types.contract_type import ContractType
from app.branch_offices.branch_office import BranchOffice
from app.region.region import Region
from app.civil_states.civil_state import CivilState
from app.healths.health import Health
from app.pention.pention import Pention
from app.communes.commune import Commune
from app.job_positions.job_position import JobPosition
from app.audits.audit import Audit
from app.employee_types.employee_type import EmployeeType
from app.documents_employees.document_employee import DocumentEmployee
from app.dropbox_data.dropbox import Dropbox
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.employees.employee import Employee
from app.helpers.pdf import Pdf

contract_datum = Blueprint("contract_data", __name__)

@contract_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@contract_datum.route("/human_resources/contract_data/<int:rut>", methods=['GET'])
@contract_datum.route("/human_resources/contract_data", methods=['GET'])
def show(rut):
   contract_datum = ContractDatum.get(rut)
   contract_types = ContractType.get()
   branch_offices = BranchOffice.get()
   regions = Region.get()
   communes = Commune.get()
   civil_states = CivilState.get()
   healths = Health.get()
   pentions = Pention.get()
   job_positions = JobPosition.get()
   employee_types = EmployeeType.get()

   contract_data = DocumentEmployee.get_by_type(rut, 21)

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/contract_data/contract_data_update.html', contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/contract_data/contract_data_update.html', contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/contract_data/contract_data_update.html', contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/contract_data/contract_data_update.html', contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes, contract_data = contract_data)

@contract_datum.route("/human_resources/contract_data/<int:rut>", methods=['POST'])
@contract_datum.route("/human_resources/contract_data", methods=['POST'])
def update(rut):
   ContractDatum.update(request.form, rut)
   Audit.store(request.form, 'employee/contract_data')

   return redirect(url_for('contract_data.show', rut = rut))

@contract_datum.route("/human_resources/contract_data/generate", methods=['POST'])
def generate():
   ContractDatum.get(request.form['rut'])

   DocumentEmployee.store(request.form)

   return redirect(url_for('contract_data.show', rut = request.form['rut']))

@contract_datum.route("/human_resources/contract_data/delete/<int:rut>/<int:id>", methods=['GET'])
@contract_datum.route("/human_resources/contract_data/delete", methods=['GET'])
def delete(rut, id):
   document_employee = DocumentEmployee.get_by_id(id)

   if document_employee.support != None:
      Dropbox.delete('/contracts/', document_employee.support)

   DocumentEmployee.delete(id)

   return redirect(url_for('contract_data.show', rut = rut))

@contract_datum.route("/human_resources/contract_data/download/<int:id>", methods=['GET'])
def download(id):
   document_employee = DocumentEmployee.get_by_id(id)
   response = Dropbox.get('/contracts/', document_employee.support)

   return redirect(response)

@contract_datum.route("/human_resources/contract_data/document/<int:rut>/<int:id>", methods=['GET'])
def document(rut, id):
   document_employee = DocumentEmployee.get_by_id(id)

   employee = Employee.get(document_employee.rut)
   employee_labor_datum = EmployeeLaborDatum.get(document_employee.rut)
   branch_office = BranchOffice.get(employee_labor_datum.branch_office_id)
   commune = Commune.get(employee_labor_datum.commune_id)
   civil_state = CivilState.get(employee_labor_datum.civil_state_id)
   full_name = employee.names + " " + employee.father_lastname + " " + employee.mother_lastname
   job_position = JobPosition.get(employee_labor_datum.job_position_id)
   signature_exist = Dropbox.exist('/signature/', employee.signature)

   if signature_exist == 1:
   
      signature = Dropbox.get('/signature/', employee.signature)
   
      data = [employee_labor_datum.entrance_company, full_name, employee.visual_rut, employee_labor_datum.address, commune.commune, civil_state.civil_state, job_position.job_position, branch_office.branch_office]
   else:
      signature = ''

      data = [employee_labor_datum.entrance_company, full_name, rut, employee_labor_datum.address, commune.commune, employee_labor_datum.civil_state_id, job_position.job_position, signature]

   pdf = Pdf.create_pdf('contract', data)
  
   response = make_response(pdf)
   response.headers['Content-Type'] = 'application/pdf'
   response.headers['Content-Disposition'] = 'attachment; filename=document.pdf'

   return response