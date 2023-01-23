from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.family_core_data.family_core_datum import FamilyCoreDatum
from app.genders.gender import Gender
from app.family_types.family_type import FamilyType
from datetime import datetime
from app.dropbox_data.dropbox import Dropbox

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
   
   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/family_core_data/family_core_data.html', family_core_data = family_core_data, rut = rut)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/family_core_data/family_core_data.html', family_core_data = family_core_data, rut = rut)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/family_core_data/family_core_data.html', family_core_data = family_core_data, rut = rut)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/family_core_data/family_core_data.html', family_core_data = family_core_data, rut = rut)

@family_core_datum.route("/human_resources/family_core_data/create/<int:rut>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/create", methods=['GET'])
def create(rut):
   genders = Gender.get()
   family_types = FamilyType.get()

   return render_template('administrator/human_resources/family_core_data/family_core_data_create.html', genders = genders, rut = rut, family_types = family_types)

@family_core_datum.route("/human_resources/family_core_data/edit/<int:rut>/<int:id>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/edit", methods=['GET'])
def edit(rut, id):
   genders = Gender.get()
   family_types = FamilyType.get()
   family_core_datum = FamilyCoreDatum.get(id, '')

   return render_template('administrator/human_resources/family_core_data/family_core_data_edit.html', family_core_datum = family_core_datum, genders = genders, rut = rut, family_types = family_types)

@family_core_datum.route("/human_resources/family_core_data/update/<int:rut>/<int:id>", methods=['POST'])
@family_core_datum.route("/human_resources/family_core_data/update", methods=['POST'])
def update(rut, id):
   if request.files['file'].filename != '':
      support = Dropbox.born_document(request.form['family_rut'], "_born_document", request.files, "/families/", "C:/Users/jesus/OneDrive/Desktop/erpjis_azure/", 1)
      FamilyCoreDatum.update(id, request.form, support)
   else:
      family_core_data = FamilyCoreDatum.get(id)
      FamilyCoreDatum.update(id, request.form, family_core_data.support)

   return redirect(url_for('family_core_data.index', rut = rut))

@family_core_datum.route("/human_resources/family_core_data/delete/<int:rut>/<int:id>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/delete", methods=['GET'])
def delete(rut, id):
   family_core_data = FamilyCoreDatum.get(id)
   FamilyCoreDatum.delete(id)
   Dropbox.delete('/families/', family_core_data.support)

   return redirect(url_for('family_core_data.index', rut = rut))

@family_core_datum.route("/human_resources/family_core_datum/store", methods=['POST'])
def store():
   if request.files['file'].filename != '':
      support = Dropbox.born_document(request.form['family_rut'], "_born_document", request.files, "/families/", "C:/Users/jesus/OneDrive/Desktop/erpjis_azure/", 1)
      FamilyCoreDatum.store(request.form, support)

   Audit.store(request.form, 'personal_data/store')

   return redirect(url_for('family_core_data.index', rut = request.form['rut']))

@family_core_datum.route("/human_resources/family_core_datum/download/<int:id>", methods=['GET'])
def download(id):
    family_core_datum = FamilyCoreDatum.get(id)
    response = Dropbox.get('/families/', family_core_datum.support)

    return redirect(response)