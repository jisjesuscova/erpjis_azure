from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import regular_employee_rol_need
from app.genders.gender import Gender
from app.employees.employee import Employee
from app.nationalities.nationality import Nationality
from app.contract_data.contract_datum import ContractDatum
from app.users.user import User
from app.audits.audit import Audit
from app.branch_offices.branch_office import BranchOffice
from app.clock_users.clock_user import ClockUser
import datetime
from app.helpers.whatsapp import Whatsapp
from app.birthdays.birthday import Birthday
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum

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
   title = 'Empleados'
   module_name = 'Recursos Humanos'

   return render_template('human_resource/human_resources/employees/employees.html', title = title, module_name = module_name, employees = employees, branch_offices = branch_offices)

@employee.route("/human_resources/employees/search/<int:page>", methods=['POST'])
def search(page=1):
   employees = Employee.search(request.form, page)
   branch_offices = BranchOffice.get()

   return render_template('human_resource/human_resources/employees/employees.html', employees = employees, branch_offices = branch_offices)

@employee.route("/human_resources/employee/create", methods=['GET'])
def create():
   genders = Gender.get()
   nationalities = Nationality.get()
   uid = ClockUser.get_last_uid()
   current_date = datetime.datetime.now()
   title = 'Crear empleado'
   module_name = 'Recursos Humanos'

   return render_template('human_resource/human_resources/personal_data/personal_data_create.html', title = title, module_name = module_name, genders = genders, nationalities = nationalities, uid = uid, current_date = current_date)

@employee.route("/human_resources/employee/store", methods=['POST'])
def store():
   employee_status_id = Employee.store(request.form)
   Audit.store(request.form, 'personal_data/store')
   contract_datum_status_id = ContractDatum.store(request.form)
   Audit.store(request.form, 'employee_extra_data/store')
   employee_extra_datum_id = EmployeeExtraDatum.store(request.form)
   Audit.store(request.form, 'contract_data/store')
   user_status_id = User.store(request.form)
   Audit.store(request.form, 'user/store')
   clock_user_status_id = ClockUser.store(request.form)
   Audit.store(request.form, 'clock_user/store')

   flash('El empleado ha sido registrado con éxito', 'success')

   if employee_status_id != 0 and contract_datum_status_id != 0 and employee_extra_datum_id != 0 and user_status_id != 0 and clock_user_status_id != 0:
      return '1'
   else:
      return '0'

@employee.route("/human_resources/employee/congratulate/<int:rut>", methods=['GET'])
@employee.route("/human_resources/employee/congratulate", methods=['POST'])
def congratulate(rut = ''):
   if request.method == 'POST':
      birthday = Birthday.store(request.form)

      Whatsapp.send(birthday.id, '1', 1, 9)

      return redirect(url_for('home.index'))
   else:
      employee = Employee.get(rut)

      return render_template('human_resource/human_resources/birthdays/birthdays.html', employee = employee, rut = rut)

@employee.route("/human_resources/employee/check_rut", methods=['POST'])
def check_rut():
   rut = request.form['rut']

   status_id = Employee.check_rut(rut)

   if status_id == 1:
      return '1'
   else:
      return '0'
   
@employee.route("/human_resources/employee/check_cellphone", methods=['POST'])
def check_cellphone():
   cellphone = request.form['cellphone']

   status_id = Employee.check_cellphone(cellphone)

   if status_id == 1:
      return '1'
   else:
      return '0'