from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.branch_offices.branch_office import BranchOffice
from app.honoraries.honorary import Honorary
from app.region.region import Region
from app.banks.bank import Bank
from app.communes.commune import Commune
from app.honorary_reasons.honorary_reason import HonoraryReason
from app.documentation_titles.documentation_title import DocumentationTitle
import requests

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
   documentation_titles_menu = DocumentationTitle.get()

   title = "Honorarios"

   module_name = "Recursos Humanos"

   if current_user.rol_id == 3:
      return render_template('supervisor/human_resources/honoraries/honoraries.html', documentation_titles_menu = documentation_titles_menu, honoraries = honoraries, title = title, module_name = module_name)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/honoraries/honoraries.html', documentation_titles_menu = documentation_titles_menu, honoraries = honoraries, title = title, module_name = module_name)

@honorary.route("/human_resources/honorary/create", methods=['GET'])
def create():
   regions = Region.get()
   banks = Bank.get()
   branch_offices = BranchOffice.get()
   honorary_reasons = HonoraryReason.get()
   documentation_titles_menu = DocumentationTitle.get()

   title = "Crear Honorario"

   module_name = "Recursos Humanos"

   if current_user.rol_id == 3:
      return render_template('supervisor/human_resources/honoraries/honoraries_create.html', documentation_titles_menu = documentation_titles_menu, honorary_reasons = honorary_reasons, title = title, module_name = module_name,  branch_offices = branch_offices, regions = regions, banks = banks)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/honoraries/honoraries_create.html', documentation_titles_menu = documentation_titles_menu, honorary_reasons = honorary_reasons, title = title, module_name = module_name,  branch_offices = branch_offices, regions = regions, banks = banks)

@honorary.route("/human_resources/honorary/accountability/<int:id>", methods=['GET'])
def accountability(id):
   honorary = Honorary.get(id, '')

   Honorary.accountability(honorary)

   return redirect(url_for('honoraries.to_upload'))

@honorary.route("/human_resources/honorary/to_upload", methods=['GET'])
def to_upload(page = 1):
   honoraries = Honorary.current_get(page)
   title = "Ejecutar Carga Honorarios"
   module_name = "Recursos Humanos"

   return render_template('human_resource/human_resources/honoraries/honoraries_to_upload.html', honoraries = honoraries, title = title, module_name = module_name)

@honorary.route("/human_resources/honorary/store", methods=['POST'])
def store():
   status_id = Honorary.store(request.form)

   flash('Se ha creado el honorario con éxito.', 'success')

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
   documentation_titles_menu = DocumentationTitle.get()

   title = "Revisar Honorario"

   module_name = "Recursos Humanos"

   return render_template('human_resource/human_resources/honoraries/honoraries_update.html', documentation_titles_menu = documentation_titles_menu, employees = employees, honorary_reasons = honorary_reasons, communes = communes, honorary = honorary, title = title, module_name = module_name,  branch_offices = branch_offices, regions = regions, banks = banks)

@honorary.route("/human_resources/honorary/delete/<int:id>", methods=['GET'])
def delete(id):
   Honorary.delete(id)
   
   flash('Se ha borrado el honorario con éxito.', 'success')

   return redirect(url_for('honoraries.index'))