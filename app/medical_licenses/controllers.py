from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.medical_licenses.medical_license import MedicalLicense
from app.medical_license_types.medical_license_type import MedicalLicenseType
from app.patology_types.patology_type import PatologyType
from app.dropbox_data.dropbox import Dropbox
from datetime import datetime

medical_license = Blueprint("medical_licenses", __name__)

@medical_license.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@medical_license.route("/human_resources/medical_licenses/<int:rut>", methods=['GET'])
@medical_license.route("/human_resources/medical_licenses", methods=['GET'])
def index(rut):
   medical_licenses = MedicalLicense.get(rut)

   return render_template('human_resources/medical_licenses/medical_licenses.html', medical_licenses = medical_licenses, rut = rut)


@medical_license.route("/human_resources/medical_license/create/<int:rut>", methods=['GET'])
@medical_license.route("/human_resources/medical_license/create", methods=['GET'])
def create(rut):
   medical_license_types = MedicalLicenseType.get()
   patology_types = PatologyType.get()

   return render_template('human_resources/medical_licenses/medical_licenses_create.html', rut = rut, medical_license_types = medical_license_types, patology_types = patology_types)

@medical_license.route("/human_resources/medical_license/edit/<int:rut>/<int:id>", methods=['GET'])
@medical_license.route("/human_resources/medical_license/edit", methods=['GET'])
def edit(rut, id):
   MedicalLicense.get(id, '')

   return render_template('human_resources/medical_licenses/medical_licenses_edit.html', rut = rut)

@medical_license.route("/human_resources/medical_license/update/<int:rut>/<int:id>", methods=['POST'])
@medical_license.route("/human_resources/medical_license/update", methods=['POST'])
def update(rut, id):
   MedicalLicense.update(id, request.form)

   return redirect(url_for('medical_licenses.index', rut = rut))

@medical_license.route("/human_resources/medical_license/delete/<int:rut>/<int:id>", methods=['GET'])
@medical_license.route("/human_resources/medical_license/delete", methods=['GET'])
def delete(rut, id):
   MedicalLicense.delete(id)

   return redirect(url_for('medical_licenses.index', rut = rut))

@medical_license.route("/human_resources/medical_license/store/<int:rut>", methods=['POST'])
@medical_license.route("/human_resources/medical_license/store", methods=['POST'])
def store(rut):
   MedicalLicense.store(request.form)

   return redirect(url_for('medical_licenses.index', rut = rut))