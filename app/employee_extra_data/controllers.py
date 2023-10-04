from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.contract_schedules.contract_schedule import ContractSchedule
from app.pentions.pention import Pention
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app.healths.health import Health
from app.helpers.helper import Helper
from app.old_employee_extra_data.old_employee_extra_datum import OldEmployeeExtraDatum
from app import db
from app.employees.employee import Employee
from app.old_employees.old_employee import OldEmployee
from app.documentation_titles.documentation_title import DocumentationTitle

employee_extra_datum = Blueprint("employee_extra_data", __name__)

@employee_extra_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@employee_extra_datum.route("/human_resources/employee_extra_data/<int:rut>", methods=['GET'])
@employee_extra_datum.route("/human_resources/employee_extra_data", methods=['GET'])
def show(rut):
   status_id = Helper.is_active(rut)
   documentation_titles_menu = DocumentationTitle.get()

   if status_id == 1:
      employee_extra_datum = EmployeeExtraDatum.get(rut)
      contract_schedules = ContractSchedule.get()
      pentions = Pention.get()
      healths = Health.get()
      regime_id = None
      employee  = Employee.get(rut)

      empty_field_status_id = EmployeeExtraDatum.empty_fields(rut)

      is_active = 1
   else:
      employee_extra_datum = OldEmployeeExtraDatum.get(rut)
      contract_schedules = ContractSchedule.get()
      pentions = Pention.get()
      healths = Health.get()
      regime_id = None
      employee  = OldEmployee.get(rut)

      empty_field_status_id = 1

      is_active = 0

   employee_extra_datum_button_status_id = 1

   title = employee.visual_rut + ' - ' + employee.names + ' ' + employee.father_lastname + ' ' + employee.mother_lastname
   module_name = 'Recursos Humanos'

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/extra_data/extra_data_update.html', documentation_titles_menu = documentation_titles_menu, empty_field_status_id = empty_field_status_id, employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/extra_data/extra_data_update.html', documentation_titles_menu = documentation_titles_menu, empty_field_status_id = empty_field_status_id, employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/extra_data/extra_data_update.html', documentation_titles_menu = documentation_titles_menu, empty_field_status_id = empty_field_status_id, employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/extra_data/extra_data_update.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, empty_field_status_id = empty_field_status_id, employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/extra_data/extra_data_update.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, empty_field_status_id = empty_field_status_id, employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)

@employee_extra_datum.route("/human_resources/employee_extra_data/<int:rut>", methods=['POST'])
@employee_extra_datum.route("/human_resources/employee_extra_data", methods=['POST'])
def update(rut):
   status_id = EmployeeExtraDatum.update(request.form, rut)

   flash('Se ha actualizado los datos extras con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'
