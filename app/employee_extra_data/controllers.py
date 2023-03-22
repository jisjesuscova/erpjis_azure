from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.contract_schedules.contract_schedule import ContractSchedule
from app.pentions.pention import Pention
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app.healths.health import Health
from app.helpers.helper import Helper
from app.old_employee_extra_data.old_employee_extra_datum import OldEmployeeExtraDatum
from app.models.models import EmployeeExtraModel
from app import db

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

   if status_id == 1:
      employee_extra_datum = EmployeeExtraDatum.get(rut)
      contract_schedules = ContractSchedule.get()
      pentions = Pention.get()
      healths = Health.get()
      regime_id = None

      is_active = 1
   else:
      employee_extra_datum = OldEmployeeExtraDatum.get(rut)
      contract_schedules = ContractSchedule.get()
      pentions = Pention.get()
      healths = Health.get()
      regime_id = None


      is_active = 0

   employee_extra_datum_button_status_id = 1

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/extra_data/extra_data_update.html', employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/extra_data/extra_data_update.html', employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/extra_data/extra_data_update.html', employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/extra_data/extra_data_update.html', employee_extra_datum_button_status_id = employee_extra_datum_button_status_id, employee_extra_datum = employee_extra_datum, contract_schedules = contract_schedules, pentions = pentions, rut = rut, healths = healths, is_active = is_active, regime_id = regime_id)

@employee_extra_datum.route("/human_resources/employee_extra_data/<int:rut>", methods=['POST'])
@employee_extra_datum.route("/human_resources/employee_extra_data", methods=['POST'])
def update(rut):

   employee_extra_datum = EmployeeExtraModel.query.filter_by(rut=rut).first()
   employee_extra_datum.contract_schedule_id = request.form['contract_schedule_id']
   employee_extra_datum.extreme_zone_id = request.form['extreme_zone_id']
   employee_extra_datum.employee_type_id = request.form['employee_type_id']
   employee_extra_datum.young_job_status_id = request.form['young_job_status_id']
   employee_extra_datum.be_paid_id = request.form['be_paid_id']
   employee_extra_datum.disability_id = request.form['disability_id']
   employee_extra_datum.suplemental_health_insurance_id = request.form['suplemental_health_insurance_id']
   employee_extra_datum.progressive_vacation_status_id = request.form['progressive_vacation_status_id']
   employee_extra_datum.progressive_vacation_date = request.form['progressive_vacation_date']
   employee_extra_datum.pensioner_id = request.form['pensioner_id']
   db.session.add(employee_extra_datum)
   db.session.commit()

   return str(request.form['pensioner_id'])
