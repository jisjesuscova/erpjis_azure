from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need, db
from app.models.models import EmployeeModel, AuditModel
from app.genders.gender import Gender
from app.employees.employee import Employee
from app.nationalities.nationality import Nationality
from app.contract_data.contract_datum import ContractDatum
from app.users.user import User
from app.audits.audit import Audit
from datetime import datetime

employee = Blueprint("employees", __name__)

@employee.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@employee.route("/human_resources/employees", methods=['GET'])
@employee.route("/human_resources/employees/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('human_resources/employees/employees.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False))

@employee.route("/human_resources/employee/create", methods=['GET'])
def create():
   genders = Gender.get()
   nationalities = Nationality.get()

   return render_template('human_resources/personal_data/personal_data_create.html', genders = genders, nationalities = nationalities)

@employee.route("/human_resources/employee/store", methods=['POST'])
def store():
   employee = Employee.store(request.form)
   Audit.store(request.form, 'personal_data/store')
   ContractDatum.store(request.form)
   Audit.store(request.form, 'contract_data/store')
   User.store(request.form)
   Audit.store(request.form, 'user/store')

   return redirect(url_for('personal_data.show', rut = employee.rut))

