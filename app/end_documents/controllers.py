from flask import Blueprint, render_template, redirect, request, url_for, flash, make_response
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.end_documents.end_document import EndDocument
from app.documents_employees.document_employee import DocumentEmployee
from app.old_documents_employees.old_document_employee import OldDocumentEmployee
from app.old_employee_extra_data.old_employee_extra_datum import OldEmployeeExtraDatum
from app.old_employee_labor_data.old_employee_labor_datum import OldEmployeeLaborDatum
from app.old_employees.old_employee import OldEmployee
from app.old_medical_licenses.old_medical_license import OldMedicalLicense
from app.old_vacations.old_vacation import OldVacation
from app.contract_data.contract_datum import ContractDatum
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.employees.employee import Employee
from app.medical_licenses.medical_license import MedicalLicense
from app.vacations.vacation import Vacation
from app.helpers.helper import Helper
from app.dropbox_data.dropbox import Dropbox
from app.helpers.pdf import Pdf
from app.causals.causal import Causal
from app.job_positions.job_position import JobPosition
from app.helpers.file import File
from app.hr_settings.hr_setting import HrSetting

end_document = Blueprint("end_documents", __name__)

@end_document.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@end_document.route("/human_resources/end_document/create/<int:rut>", methods=['GET'])
def create(rut):
   voluntary_indemnity = 0
   indemnity_years_service = 0
   substitute_compensation = 0
   fertility_proportional = 0
   total = 0
   legal = Vacation.legal(rut)
   taken_days = Vacation.taken_days(rut)
   balance = Vacation.balance(legal, taken_days)
  
   return render_template('human_resource/human_resources/end_documents/end_document_data.html', rut = rut, balance = balance, voluntary_indemnity = voluntary_indemnity, indemnity_years_service = indemnity_years_service, substitute_compensation = substitute_compensation, fertility_proportional= fertility_proportional, total = total)

@end_document.route("/human_resources/end_document/indemnity_years_service", methods=['POST'])
def indemnity_years_service():
   rut = request.form['rut']
   indemnity_years_service = EndDocument.indemnity_years_service(rut, request.form['exit_company'])

   return str(indemnity_years_service)
  
@end_document.route("/human_resources/end_document/substitute_compensation", methods=['POST'])
def substitute_compensation():
   substitute_compensation = EndDocument.substitute_compensation(request.form['rut'])

   return str(substitute_compensation)

@end_document.route("/human_resources/end_document/fertility_proportional", methods=['POST'])
def fertility_proportional():
   fertility_proportional = EndDocument.fertility_proportional(request.form['rut'], request.form['exit_company'], request.form['balance'], request.form['number_holidays'])
   total_vacations = EndDocument.total_vacations(request.form['rut'], request.form['exit_company'], request.form['balance'], request.form['number_holidays'])

   return str(fertility_proportional) +"_"+ str(total_vacations)

@end_document.route("/human_resources/end_document/store", methods=['POST'])
def store():
   id = DocumentEmployee.store(request.form)
   EndDocument.store(id, request.form)
   status_id = request.form['employee_status_id']
   rut = request.form['rut']
   exit_company = request.form['exit_company']

   medical_license_order_id = OldMedicalLicense.get_last_order(rut)
   vacation_order_id = OldVacation.get_last_order(rut)
   document_employee_order_id = OldDocumentEmployee.get_last_order(rut)
   employee_extra_datum_order_id = OldEmployeeExtraDatum.get_last_order(rut)
   employee_labor_datum_order_id = OldEmployeeLaborDatum.get_last_order(rut)
   employee_order_id = OldEmployee.get_last_order(rut)

   OldMedicalLicense.finish(rut, medical_license_order_id)
   OldVacation.finish(rut, vacation_order_id)
   OldDocumentEmployee.finish(rut, document_employee_order_id)
   OldEmployeeExtraDatum.finish(rut, employee_extra_datum_order_id)
   OldEmployeeLaborDatum.finish(rut, employee_labor_datum_order_id)
   OldEmployee.finish(rut, employee_order_id)
   OldEmployeeLaborDatum.end(rut, exit_company, status_id)

   flash('Se ha creado un nuevo finiquito', 'success')

   return '1'

@end_document.route("/human_resources/end_document/delete/<int:end_document_id>/<int:document_employee_id>/<int:rut>", methods=['GET'])
def delete(end_document_id, document_employee_id, rut):
   old_document_employee = OldDocumentEmployee.get_by_id(document_employee_id)

   if old_document_employee.support != None:
      Dropbox.delete('/end_documents/', old_document_employee.support)
      File.delete('app/static/dist/files/end_document_data/', old_document_employee.support)

   OldDocumentEmployee.end_document_delete(rut)
   EndDocument.delete(end_document_id)

   medical_license_order_id = OldMedicalLicense.get_last_order(rut)
   medical_license_order_id = Helper.get_last_order_id_to_restore(medical_license_order_id)
   MedicalLicense.restore(rut, medical_license_order_id)

   vacation_order_id = OldVacation.get_last_order(rut)
   vacation_order_id = Helper.get_last_order_id_to_restore(vacation_order_id)
   Vacation.restore(rut, vacation_order_id)

   document_employee_order_id = OldDocumentEmployee.get_last_order(rut)
   document_employee_order_id = Helper.get_last_order_id_to_restore(document_employee_order_id)
   DocumentEmployee.restore(rut, document_employee_order_id)

   employee_extra_datum_order_id = OldEmployeeExtraDatum.get_last_order(rut)
   employee_extra_datum_order_id = Helper.get_last_order_id_to_restore(employee_extra_datum_order_id)
   EmployeeExtraDatum.restore(rut, employee_extra_datum_order_id)

   employee_labor_datum_order_id = OldEmployeeLaborDatum.get_last_order(rut)
   employee_labor_datum_order_id = Helper.get_last_order_id_to_restore(employee_labor_datum_order_id)
   EmployeeLaborDatum.restore(rut, employee_labor_datum_order_id)

   employee_order_id = OldEmployee.get_last_order(rut)
   employee_order_id = Helper.get_last_order_id_to_restore(employee_order_id)
   Employee.restore(rut, employee_order_id)

   ContractDatum.restore(rut)

   flash('Se ha activado nuevamente al empleado', 'success')
   
   return redirect(url_for('contract_data.show', rut = rut))


@end_document.route("/human_resources/end_document/upload/<int:id>/<int:rut>", methods=['GET', 'POST'])
@end_document.route("/human_resources/end_document/upload", methods=['GET', 'POST'])
def upload(id, rut):
   if request.method == 'POST':
      support = Dropbox.upload(rut, '_finiquito', request.files, "/end_documents/", "app/static/dist/files/end_document_data/")
      EndDocument.upload(id, support)

      flash('Se ha subido el finiquito correctamente', 'success')

      return redirect(url_for('contract_data.show', rut = rut))
   else:
      return render_template('human_resource/human_resources/end_documents/end_documents_upload.html', id = id, rut = rut)


@end_document.route("/human_resources/end_document/download/<int:id>/<int:rut>", methods=['GET'])
def download(id, rut):
   status_id = Helper.is_active(rut)

   if status_id == 1:
      end_document = DocumentEmployee.get_by_id(id)
   else:
      end_document = OldDocumentEmployee.get_by_id(id)

   response = Dropbox.get('/end_documents/', end_document.support)

   return redirect(response)

@end_document.route("/human_resources/end_document/document/<int:rut>/<int:id>", methods=['GET'])
def document(rut, id):
   old_employee_labor_datum = OldEmployeeLaborDatum.get(rut)
   old_employee = OldEmployee.get(rut)
   exit_company_date = Helper.document_date(str(old_employee_labor_datum.exit_company))
   full_name = old_employee.names +" "+  old_employee.father_lastname +" "+  old_employee.mother_lastname
   job_position = JobPosition.get(old_employee_labor_datum.job_position_id)
   end_document = EndDocument.get_by_rut(old_employee.rut)
   causal = Causal.get(end_document.causal_id)
   total = Helper.fix_thousands(end_document.total)
   entrance_company = Helper.document_date(str(old_employee_labor_datum.entrance_company))
   fertility_proportional = Helper.fix_thousands(end_document.fertility_proportional)
   voluntary_indemnity = Helper.fix_thousands(end_document.voluntary_indemnity)
   substitute_compensation = Helper.fix_thousands(end_document.substitute_compensation)
   indemnity_years_service = Helper.fix_thousands(end_document.indemnity_years_service)

   data = [exit_company_date, full_name, old_employee.visual_rut, job_position.job_position, entrance_company, causal.causal, indemnity_years_service, substitute_compensation, voluntary_indemnity, end_document.fertility_proportional_days, fertility_proportional, total]

   pdf = Pdf.create_pdf('end_document', data)
  
   response = make_response(pdf)
   response.headers['Content-Type'] = 'application/pdf'
   response.headers['Content-Disposition'] = 'attachment; filename=document.pdf'

   return response