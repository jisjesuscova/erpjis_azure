from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.medical_licenses.medical_license import MedicalLicense
from app.medical_license_types.medical_license_type import MedicalLicenseType
from app.patology_types.patology_type import PatologyType
from app.dropbox_data.dropbox import Dropbox
from app.helpers.helper import Helper
from app.documents_employees.document_employee import DocumentEmployee
from app.helpers.file import File
from app.old_medical_licenses.old_medical_license import OldMedicalLicense
from app.old_documents_employees.old_document_employee import OldDocumentEmployee

medical_license = Blueprint("medical_licenses", __name__)

@medical_license.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@medical_license.route("/human_resources/medical_licenses/<int:rut>", methods=['GET'])
@medical_license.route("/human_resources/medical_licenses", methods=['GET'])
def index(rut):
   status_id = Helper.is_active(rut)
   
   if status_id == 1:
      is_active = 1

      medical_licenses = MedicalLicense.get(rut)
   else:
      is_active = 0

      medical_licenses = OldMedicalLicense.get(rut)

   if current_user.rol_id == 1:
      return render_template('collaborator/human_resources/medical_licenses/medical_licenses.html', medical_licenses = medical_licenses, rut = rut, is_active = is_active)
   elif current_user.rol_id == 2:
      return render_template('incharge/human_resources/medical_licenses/medical_licenses.html', medical_licenses = medical_licenses, rut = rut, is_active = is_active)
   elif current_user.rol_id == 3:
      return render_template('supervisor/human_resources/medical_licenses/medical_licenses.html', medical_licenses = medical_licenses, rut = rut, is_active = is_active)
   elif current_user.rol_id == 4:
      return render_template('administrator/human_resources/medical_licenses/medical_licenses.html', medical_licenses = medical_licenses, rut = rut, is_active = is_active)

@medical_license.route("/human_resources/medical_license/create/<int:rut>", methods=['GET'])
@medical_license.route("/human_resources/medical_license/create", methods=['GET'])
def create(rut):
   medical_license_types = MedicalLicenseType.get()
   patology_types = PatologyType.get()

   return render_template('administrator/human_resources/medical_licenses/medical_licenses_create.html', rut = rut, medical_license_types = medical_license_types, patology_types = patology_types)

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

@medical_license.route("/human_resources/medical_license/delete/<int:id>/<int:rut>", methods=['GET'])
@medical_license.route("/human_resources/medical_license/delete", methods=['GET'])
def delete(id, rut):
   document_employee = DocumentEmployee.get_by_id(id)
   DocumentEmployee.delete(id)
   MedicalLicense.delete(id)
   Dropbox.delete('/medical_licenses/', document_employee.support)
   File.delete('app/static/dist/files/medical_license_data/', document_employee.support)

   flash('Se ha borrado la licendia m??dica con ??xito.', 'success')

   return redirect(url_for('medical_licenses.index', rut = rut))

@medical_license.route("/human_resources/medical_license/store/<int:rut>", methods=['POST'])
@medical_license.route("/human_resources/medical_license/store", methods=['POST'])
def store(rut):
   id = DocumentEmployee.store(request.form)

   MedicalLicense.store(id, request.form)

   return redirect(url_for('medical_licenses.index', rut = rut))

@medical_license.route("/human_resources/medical_license/upload/<int:id>/<int:rut>", methods=['GET', 'POST'])
@medical_license.route("/human_resources/medical_license/upload", methods=['GET', 'POST'])
def upload(id, rut):
   if request.method == 'POST':
      support = Dropbox.upload(rut, '_licecia_medica', request.files, "/medical_licenses/", "app/static/dist/files/medical_license_data/")
      MedicalLicense.upload(id, support)

      return redirect(url_for('medical_licenses.index', rut = rut))
   else:
      return render_template('administrator/human_resources/medical_licenses/medical_licenses_upload.html', id = id, rut = rut)


@medical_license.route("/human_resources/medical_license/download/<int:id>/<int:rut>", methods=['GET'])
def download(id, rut):
   status_id = Helper.is_active(rut)

   if status_id == 1:
      medical_license = DocumentEmployee.get_by_id(id)
   else:
      medical_license = OldDocumentEmployee.get_by_id(id)

   response = Dropbox.get('/medical_licenses/', medical_license.support)

   return redirect(response)