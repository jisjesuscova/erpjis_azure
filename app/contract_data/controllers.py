from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.contract_data.contract_datum import ContractDatum
from app.contract_types.contract_type import ContractType
from app.branch_offices.branch_office import BranchOffice
from app.region.region import Region
from app.civil_states.civil_state import CivilState
from app.healths.health import Health
from app.pention.pention import Pention
from app.job_positions.job_position import JobPosition
from app.audits.audit import Audit
from app.employee_types.employee_type import EmployeeType
from datetime import datetime

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
   civil_states = CivilState.get()
   healths = Health.get()
   pentions = Pention.get()
   job_positions = JobPosition.get()
   employee_types = EmployeeType.get()

   return render_template('human_resources/contract_data/contract_data_update.html', contract_datum = contract_datum, rut = rut, contract_types = contract_types, branch_offices = branch_offices, regions = regions, civil_states = civil_states, healths = healths, pentions = pentions, job_positions = job_positions, employee_types = employee_types)


@contract_datum.route("/human_resources/contract_data/<int:rut>", methods=['POST'])
@contract_datum.route("/human_resources/contract_data", methods=['POST'])
def update(rut):
   ContractDatum.update(request.form, rut)
   Audit.store(request.form, 'employee/contract_data')

   return redirect(url_for('contract_data.show', rut = rut))