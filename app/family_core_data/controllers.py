from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.family_core_data.family_core_datum import FamilyCoreDatum
from app.genders.gender import Gender
from app.family_types.family_type import FamilyType
from app.dropbox_data.dropbox import Dropbox
from app.helpers.file import File
from app.employees.employee import Employee
from app.helpers.helper import Helper
from app.old_employees.old_employee import OldEmployee
from app.documentation_titles.documentation_title import DocumentationTitle

family_core_datum = Blueprint("family_core_data", __name__)

@family_core_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@family_core_datum.route("/human_resources/family_core_data/<int:rut>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data", methods=['GET'])
def index(rut):
   family_core_data = FamilyCoreDatum.get('', rut)
   documentation_titles_menu = DocumentationTitle.get()

   family_core_button_status_id = 1

   status_id = Helper.is_active(rut)

   if status_id == 1:
      employee  = Employee.get(rut)
   else:
      employee  = OldEmployee.get(rut)

   title = employee.visual_rut + ' - ' + employee.names + ' ' + employee.father_lastname + ' ' + employee.mother_lastname
   module_name = 'Recursos Humanos'
   
   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/family_core_data/family_core_data.html', documentation_titles_menu = documentation_titles_menu, family_core_button_status_id = family_core_button_status_id, family_core_data = family_core_data, rut = rut)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/family_core_data/family_core_data.html', documentation_titles_menu = documentation_titles_menu, family_core_button_status_id = family_core_button_status_id, family_core_data = family_core_data, rut = rut)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/family_core_data/family_core_data.html', documentation_titles_menu = documentation_titles_menu, family_core_button_status_id = family_core_button_status_id, family_core_data = family_core_data, rut = rut)
   elif current_user.rol_id == 4:
      return render_template('human_resource/human_resources/family_core_data/family_core_data.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, family_core_button_status_id = family_core_button_status_id, family_core_data = family_core_data, rut = rut)
   elif current_user.rol_id == 5:
      return render_template('designer/human_resources/family_core_data/family_core_data.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, family_core_button_status_id = family_core_button_status_id, family_core_data = family_core_data, rut = rut)


@family_core_datum.route("/human_resources/family_core_data/create/<int:rut>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/create", methods=['GET'])
def create(rut):
   genders = Gender.get()
   family_types = FamilyType.get()
   documentation_titles_menu = DocumentationTitle.get()

   return render_template('human_resource/human_resources/family_core_data/family_core_data_create.html', documentation_titles_menu = documentation_titles_menu, genders = genders, rut = rut, family_types = family_types)

@family_core_datum.route("/human_resources/family_core_data/edit/<int:rut>/<int:id>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/edit", methods=['GET'])
def edit(rut, id):
   genders = Gender.get()
   family_types = FamilyType.get()
   family_core_datum = FamilyCoreDatum.get(id, '')
   documentation_titles_menu = DocumentationTitle.get()

   return render_template('human_resource/human_resources/family_core_data/family_core_data_edit.html', documentation_titles_menu = documentation_titles_menu, family_core_datum = family_core_datum, genders = genders, rut = rut, family_types = family_types, id = id)

@family_core_datum.route("/human_resources/family_core_data/update/<int:rut>/<int:id>", methods=['POST'])
@family_core_datum.route("/human_resources/family_core_data/update", methods=['POST'])
def update(rut, id):
   if 'file' in request.files:
      family_core_data = FamilyCoreDatum.get(id)
      support = Dropbox.born_document(request.form['family_rut'], "_born_document", request.files, "/intranet_jisparking_files/", "app/static/dist/files/family_data/", 0)
      File.delete("app/static/dist/files/family_data/", family_core_data.support)

      status_id = FamilyCoreDatum.update(id, request.form, support)
   else:
      family_core_data = FamilyCoreDatum.get(id)
      status_id = FamilyCoreDatum.update(id, request.form, family_core_data.support)

   flash('El familiar ha sido actualizado con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'

@family_core_datum.route("/human_resources/family_core_data/delete/<int:rut>/<int:id>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/delete", methods=['GET'])
def delete(rut, id):
   family_core_data = FamilyCoreDatum.get(id)
   FamilyCoreDatum.delete(id)
   Dropbox.delete('/families/', family_core_data.support)
   File.delete("app/static/dist/files/family_data/", family_core_data.support)

   flash('El familiar ha sido borrado con éxito', 'success')

   return redirect(url_for('family_core_data.index', rut = rut))

@family_core_datum.route("/human_resources/family_core_datum/store", methods=['POST'])
def store():
   if 'file' in request.files:
      support = Dropbox.born_document(request.form['family_rut'], "_born_document", request.files, "/intranet_jisparking_files/", "app/static/dist/files/family_data/", 0)
      print(support)
      status_id = FamilyCoreDatum.store(request.form, support)

   Audit.store(request.form, 'personal_data/store')

   flash('El familiar ha sido agregado con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'

@family_core_datum.route("/human_resources/family_core_datum/download/<int:id>", methods=['GET'])
def download(id):
    family_core_datum = FamilyCoreDatum.get(id)
    response = Dropbox.get('/intranet_jisparking_files/', family_core_datum.support)

    return redirect(response)