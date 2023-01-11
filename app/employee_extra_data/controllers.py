from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.contract_data.contract_datum import ContractDatum
from app.audits.audit import Audit
from app.employee_types.employee_type import EmployeeType
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum

employee_extra_datum = Blueprint("employee_extra_data", __name__)

@employee_extra_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@employee_extra_datum.route("/human_resources/employee_extra_data/<int:rut>", methods=['GET'])
@employee_extra_datum.route("/human_resources/employee_extra_data", methods=['GET'])
def show(rut):
   extra_datum = ''
   employee_types = EmployeeType.get()

   return render_template('human_resources/extra_data/extra_data_update.html', extra_datum = extra_datum, employee_types = employee_types)


@employee_extra_datum.route("/human_resources/employee_extra_data/<int:rut>", methods=['POST'])
@employee_extra_datum.route("/human_resources/employee_extra_data", methods=['POST'])
def update(rut):
   ContractDatum.update(request.form, rut)
   Audit.store(request.form, 'employee/contract_data')

   return redirect(url_for('contract_data.show', rut = rut))