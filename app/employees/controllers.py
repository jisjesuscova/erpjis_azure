from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need, db
from app.models.models import EmployeeModel
from app.genders.gender import Gender
from app.employees.employee import Employee
from app.nationalities.nationality import Nationality
from app.contract_data.contract_datum import ContractDatum
from app.users.user import User
from app.audits.audit import Audit
from app.branch_offices.branch_office import BranchOffice
from app.clock_users.clock_user import ClockUser
import datetime

employee = Blueprint("employees", __name__)

@employee.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@employee.route("/human_resources/employees", methods=['GET'])
@employee.route("/human_resources/employees/<int:page>", methods=['GET'])
def index(page=1):
   employees = Employee.get('', page)
   branch_offices = BranchOffice.get()

   return render_template('administrator/human_resources/employees/employees.html', employees = employees, branch_offices = branch_offices)

@employee.route("/human_resources/employees/search/<int:page>", methods=['POST'])
def search(page=1):
   employees = Employee.search(request.form, page)
   branch_offices = BranchOffice.get()

   return render_template('administrator/human_resources/employees/employees.html', employees = employees, branch_offices = branch_offices)


@employee.route("/human_resources/employee/create", methods=['GET'])
def create():
   genders = Gender.get()
   nationalities = Nationality.get()
   uid = ClockUser.get_last_uid()
   current_date = datetime.datetime.now()

   return render_template('administrator/human_resources/personal_data/personal_data_create.html', genders = genders, nationalities = nationalities, uid = uid, current_date = current_date)

@employee.route("/human_resources/employee/store", methods=['POST'])
def store():
   employee = Employee.store(request.form)
   Audit.store(request.form, 'personal_data/store')
   ContractDatum.store(request.form)
   Audit.store(request.form, 'contract_data/store')
   User.store(request.form)
   Audit.store(request.form, 'user/store')
   ClockUser.store(request.form)
   Audit.store(request.form, 'clock_user/store')

   return redirect(url_for('personal_data.show', rut = employee.rut))

