from flask import Blueprint, render_template, redirect, request, url_for, make_response, flash
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
from app.helpers.helper import Helper
from app.end_documents.end_document import EndDocument
from app.old_documents_employees.old_document_employee import OldDocumentEmployee
from app.old_contract_data.old_contract_datum import OldContractDatum
from app.old_employees.old_employee import OldEmployee
from app.documentation_titles.documentation_title import DocumentationTitle

contract_datum = Blueprint("contract_data", __name__)

@contract_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@contract_datum.route("/human_resources/contract_data/<int:rut>", methods=['GET'])
@contract_datum.route("/human_resources/contract_data", methods=['GET'])
def show(rut):
   status_id = Helper.is_active(rut)

   documentation_titles_menu = DocumentationTitle.get()

   if status_id == 1:
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
      end_documents = EndDocument.get(rut)
      contract_data = DocumentEmployee.get_by_type(rut, 21)
      employee  = Employee.get(rut)

      empty_field_status_id = ContractDatum.empty_fields(rut)

      is_active = 1
   else:
      contract_datum = OldContractDatum.get(rut)
      contract_types = ContractType.get()
      branch_offices = BranchOffice.get()
      regions = Region.get()
      communes = Commune.get()
      civil_states = CivilState.get()
      healths = Health.get()
      pentions = Pention.get()
      job_positions = JobPosition.get()
      employee_types = EmployeeType.get()
      end_documents = EndDocument.get(rut)
      contract_data = OldDocumentEmployee.get_by_type(rut, 21)
      employee  = OldEmployee.get(rut)

      empty_field_status_id = 1

      is_active = 0

   employee_contract_datum_button_status_id = 1

   title = employee.visual_rut + ' - ' + employee.names + ' ' + employee.father_lastname + ' ' + employee.mother_lastname
   module_name = 'Recursos Humanos'
   
   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/contract_data/contract_data_update.html', documentation_titles_menu = documentation_titles_menu, employee_contract_datum_button_status_id = employee_contract_datum_button_status_id, contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes, is_active = is_active)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/contract_data/contract_data_update.html', documentation_titles_menu = documentation_titles_menu, employee_contract_datum_button_status_id = employee_contract_datum_button_status_id, contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes, is_active = is_active)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/contract_data/contract_data_update.html', documentation_titles_menu = documentation_titles_menu, employee_contract_datum_button_status_id = employee_contract_datum_button_status_id, contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes, is_active = is_active)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/contract_data/contract_data_update.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, empty_field_status_id = empty_field_status_id, employee_contract_datum_button_status_id = employee_contract_datum_button_status_id, contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes, contract_data = contract_data, end_documents = end_documents, is_active = is_active)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/contract_data/contract_data_update.html', documentation_titles_menu = documentation_titles_menu, employee_contract_datum_button_status_id = employee_contract_datum_button_status_id, contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes, is_active = is_active)

@contract_datum.route("/human_resources/contract_data/review/<int:rut>", methods=['GET'])
def review(rut):
   status_id = Helper.is_active(rut)

   documentation_titles_menu = DocumentationTitle.get()

   if status_id == 1:
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
      end_documents = EndDocument.get(rut)
      contract_data = DocumentEmployee.get_by_type(rut, 21)

      empty_field_status_id = ContractDatum.empty_fields(rut)

      is_active = 1
   else:
      contract_datum = OldContractDatum.get(rut)
      contract_types = ContractType.get()
      branch_offices = BranchOffice.get()
      regions = Region.get()
      communes = Commune.get()
      civil_states = CivilState.get()
      healths = Health.get()
      pentions = Pention.get()
      job_positions = JobPosition.get()
      employee_types = EmployeeType.get()
      end_documents = EndDocument.get(rut)
      contract_data = OldDocumentEmployee.get_by_type(rut, 21)

      empty_field_status_id = 1

      is_active = 0

   employee_contract_datum_button_status_id = 1

   return render_template('human_resource/human_resources/contract_data/contract_data_review.html', documentation_titles_menu = documentation_titles_menu, empty_field_status_id = empty_field_status_id, employee_contract_datum_button_status_id = employee_contract_datum_button_status_id, contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types, communes = communes, contract_data = contract_data, end_documents = end_documents, is_active = is_active)
                             

@contract_datum.route("/human_resources/contract_data/<int:rut>", methods=['POST'])
@contract_datum.route("/human_resources/contract_data", methods=['POST'])
def update(rut):
   status_id = ContractDatum.update(request.form, rut)
   Audit.store(request.form, 'employee/contract_data')

   flash('Se ha actualizado el contrato con éxito.', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'

@contract_datum.route("/human_resources/contract_data/generate", methods=['POST'])
def generate():
   ContractDatum.get(request.form['rut'])

   DocumentEmployee.store(request.form)

   flash('Se ha generado el contrato con éxito.', 'success')

   return redirect(url_for('contract_data.show', rut = request.form['rut']))

@contract_datum.route("/human_resources/contract_data/delete/<int:rut>/<int:id>", methods=['GET'])
@contract_datum.route("/human_resources/contract_data/delete", methods=['GET'])
def delete(rut, id):
   document_employee = DocumentEmployee.get_by_id(id)

   if document_employee.support != None:
      Dropbox.delete('/contracts/', document_employee.support)

   DocumentEmployee.delete(id)

   flash('Se ha borrado el contrato con éxito.', 'success')

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
   entrance_company_date = Helper.document_date(str(employee_labor_datum.entrance_company))
   first_extention_contract = Helper.extention_contract(employee_labor_datum.entrance_company)
   first_extention_contract_last_day = Helper.get_last_day(first_extention_contract)
   first_extention_contract_last_day = Helper.american_date(first_extention_contract_last_day)
   first_extention_contract_last_day = Helper.document_date(str(first_extention_contract_last_day))
   second_extention_contract = Helper.extention_contract(first_extention_contract)
   second_extention_contract_last_day = Helper.get_last_day(second_extention_contract)
   second_extention_contract_last_day = Helper.american_date(second_extention_contract_last_day)
   second_extention_contract_last_day = Helper.document_date(str(second_extention_contract_last_day))
   pention = Pention.get(employee_labor_datum.pention_id)
   health = Health.get(employee_labor_datum.health_id)
   salary = Helper.fix_thousands(employee_labor_datum.salary)

   if pention != None:
      pention = pention.pention
   else:
      pention = 'Sin AFP'
   
   data = [entrance_company_date, full_name, employee.visual_rut, employee_labor_datum.address, commune.commune, civil_state.civil_state, job_position.job_position, branch_office.branch_office, branch_office.address, job_position.functions, employee_labor_datum.employee_type_id, salary, first_extention_contract_last_day, second_extention_contract_last_day, pention, health.health, employee.personal_email]
   
   if employee_labor_datum.job_position_id == 10 or employee_labor_datum.job_position_id == 9 or employee_labor_datum.job_position_id == 8 or employee_labor_datum.job_position_id == 7 or employee_labor_datum.job_position_id == 6:
      if employee_labor_datum.employee_type_id == 1:
         pdf = Pdf.create_pdf('multifunctional_employee_contract', data)
      else:
         pdf = Pdf.create_pdf('part_time_multifunctional_employee_contract', data)

   elif employee_labor_datum.job_position_id == 15:
      pdf = Pdf.create_pdf('hr_manager_contract', data)
  
   response = make_response(pdf)
   response.headers['Content-Type'] = 'application/pdf'
   response.headers['Content-Disposition'] = 'attachment; filename=document.pdf'

   return response

@contract_datum.route("/human_resources/contract_data/upload/<int:id>/<int:rut>", methods=['GET', 'POST'])
@contract_datum.route("/human_resources/contract_data/upload", methods=['GET', 'POST'])
def upload(id = '', rut = ''):
   if request.method == 'POST':
      support = Dropbox.upload(request.form['rut'], '_contrato', request.files, "/contracts/", "app/static/dist/files/contract_data/")

      DocumentEmployee.update_file(request.form['id'], support)

      flash('Se ha subido el contrato con éxito.', 'success')

      return redirect(url_for('contract_data.show', rut = request.form['rut']))
   else:
      return render_template('human_resource/human_resources/contract_data/contract_data_upload.html', id = id, rut = rut)