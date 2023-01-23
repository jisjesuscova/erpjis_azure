from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.contract_schedules.contract_schedule import ContractSchedule
from app.audits.audit import Audit
from app.employee_types.employee_type import EmployeeType
from app.pentions.pention import Pention
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app.healths.health import Health

employee_extra_datum = Blueprint("employee_extra_data", __name__)

@employee_extra_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@employee_extra_datum.route("/human_resources/employee_extra_data/<int:rut>", methods=['GET'])
@employee_extra_datum.route("/human_resources/employee_extra_data", methods=['GET'])
def show(rut):
   employee_extra_datum = EmployeeExtraDatum.get(rut)
   contract_schedules = ContractSchedule.get()
   pentions = Pention.get()
   healths = Health.get()

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/extra_data/extra_data_update.html', employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/extra_data/extra_data_update.html', employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/extra_data/extra_data_update.html', employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/extra_data/extra_data_update.html', employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths)

@employee_extra_datum.route("/human_resources/employee_extra_data/<int:rut>", methods=['POST'])
@employee_extra_datum.route("/human_resources/employee_extra_data", methods=['POST'])
def update(rut):
   EmployeeExtraDatum.update(request.form, rut)

   return redirect(url_for('employee_extra_data.show', rut = rut))