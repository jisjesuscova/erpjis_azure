from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.family_core_data.family_core_datum import FamilyCoreDatum
from app.genders.gender import Gender
from app.family_types.family_type import FamilyType
from datetime import datetime

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
    
    return render_template('human_resources/family_core_data/family_core_data.html', family_core_data = family_core_data, rut = rut)


@family_core_datum.route("/human_resources/family_core_data/show/<int:rut>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/show", methods=['GET'])
def show(rut):
   genders = Gender.get()
   family_types = FamilyType.get()

   return render_template('human_resources/family_core_data/family_core_data_create.html', genders = genders, rut = rut, family_types = family_types)

@family_core_datum.route("/human_resources/family_core_data/edit/<int:rut>/<int:id>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/edit", methods=['GET'])
def edit(rut, id):
   genders = Gender.get()
   family_types = FamilyType.get()
   family_core_datum = FamilyCoreDatum.get(id, '')

   return render_template('human_resources/family_core_data/family_core_data_edit.html', family_core_datum = family_core_datum, genders = genders, rut = rut, family_types = family_types)

@family_core_datum.route("/human_resources/family_core_data/update/<int:rut>/<int:id>", methods=['POST'])
@family_core_datum.route("/human_resources/family_core_data/update", methods=['POST'])
def update(rut, id):
   FamilyCoreDatum.update(id, request.form)

   return redirect(url_for('family_core_data.index', rut = rut))

@family_core_datum.route("/human_resources/family_core_data/delete/<int:rut>/<int:id>", methods=['GET'])
@family_core_datum.route("/human_resources/family_core_data/delete", methods=['GET'])
def delete(rut, id):
   FamilyCoreDatum.delete(id)

   return redirect(url_for('family_core_data.index', rut = rut))

@family_core_datum.route("/human_resources/family_core_datum/store", methods=['POST'])
def store():
   FamilyCoreDatum.store(request.form)
   Audit.store(request.form, 'personal_data/store')

   return redirect(url_for('family_core_data.index', rut = request.form['rut']))