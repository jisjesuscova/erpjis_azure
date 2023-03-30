from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.branch_offices.branch_office import BranchOffice
from app.honoraries.honorary import Honorary
from app.region.region import Region
from app.banks.bank import Bank
from app.communes.commune import Commune
from app.honorary_reasons.honorary_reason import HonoraryReason

honorary = Blueprint("honoraries", __name__)

@honorary.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@honorary.route("/human_resources/honoraries/<int:page>", methods=['GET'])
@honorary.route("/human_resources/honoraries", methods=['GET'])
def index(page=1):
   honoraries = Honorary.get('', page)

   title = "Honorarios"

   module_name = "Recursos Humanos"

   return render_template('administrator/human_resources/honoraries/honoraries.html', honoraries = honoraries, title = title, module_name = module_name)

@honorary.route("/human_resources/honorary/create", methods=['GET'])
def create():
   regions = Region.get()
   banks = Bank.get()
   branch_offices = BranchOffice.get()
   honorary_reasons = HonoraryReason.get()

   title = "Crear Honorario"

   module_name = "Recursos Humanos"

   return render_template('administrator/human_resources/honoraries/honoraries_create.html', honorary_reasons = honorary_reasons, title = title, module_name = module_name,  branch_offices = branch_offices, regions = regions, banks = banks)


@honorary.route("/human_resources/honorary/store", methods=['POST'])
def store():
   status_id = Honorary.store(request.form)

   if status_id == 1:
      return '1'
   else:
      return '0'

@honorary.route("/human_resources/honorary/update/<int:id>", methods=['POST'])
def update(id):
   status_id = Honorary.update(request.form, id)

   if status_id == 1:
      return '1'
   else:
      return '0'


@honorary.route("/human_resources/honorary/edit/<int:id>", methods=['GET'])
def edit(id):
   honorary = Honorary.get(id, '')
   regions = Region.get()
   banks = Bank.get()
   communes = Commune.get()
   branch_offices = BranchOffice.get()
   honorary_reasons = HonoraryReason.get()
   employees = Employee.get_all()

   title = "Revisar Honorario"

   module_name = "Recursos Humanos"

   return render_template('administrator/human_resources/honoraries/honoraries_update.html', employees = employees, honorary_reasons = honorary_reasons, communes = communes, honorary = honorary, title = title, module_name = module_name,  branch_offices = branch_offices, regions = regions, banks = banks)

@honorary.route("/human_resources/honorary/delete/<int:id>", methods=['GET'])
def delete(id):
   Honorary.delete(id)
   flash('Se ha borrado el honorario con éxito.', 'success')

   return redirect(url_for('honoraries.index'))