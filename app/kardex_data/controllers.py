from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.kardex_data.kardex_datum import KardexDatum
from app.document_types.document_type import DocumentType
from app.dropbox_data.dropbox import Dropbox
from datetime import datetime

kardex_datum = Blueprint("kardex_data", __name__)

@kardex_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@kardex_datum.route("/human_resources/kardex_data/<int:rut>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data", methods=['GET'])
def index(rut):
   documents_employees = KardexDatum.get(rut)

   return render_template('human_resources/kardex_data/kardex_data.html', documents_employees = documents_employees, rut = rut)


@kardex_datum.route("/human_resources/kardex_data/show/<int:rut>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/show", methods=['GET'])
def show(rut):
   document_types = DocumentType.get('', 1, '', '')

   return render_template('human_resources/kardex_data/kardex_data_create.html', rut = rut, document_types = document_types)

@kardex_datum.route("/human_resources/kardex_data/edit/<int:rut>/<int:id>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/edit", methods=['GET'])
def edit(rut, id):
   KardexDatum.get(id, '')

   return render_template('human_resources/kardex_data/kardex_data_edit.html', rut = rut)

@kardex_datum.route("/human_resources/kardex_data/update/<int:rut>/<int:id>", methods=['POST'])
@kardex_datum.route("/human_resources/kardex_data/update", methods=['POST'])
def update(rut, id):
   KardexDatum.update(id, request.form)

   return redirect(url_for('kardex_data.index', rut = rut))

@kardex_datum.route("/human_resources/kardex_data/delete/<int:rut>/<int:id>", methods=['GET'])
@kardex_datum.route("/human_resources/kardex_data/delete", methods=['GET'])
def delete(rut, id):
   KardexDatum.delete(id)

   return redirect(url_for('kardex_data.index', rut = rut))


@kardex_datum.route("/human_resources/kardex_datum/store", methods=['POST'])
def store():
   support = Dropbox.upload(request.files, "/kardex/", "C:/Users/jesus/OneDrive/Desktop/erp_jis_v1/erp_jis_v1/erp_jis/")
   if support != 0:
      KardexDatum.store(request.form, support)

   return redirect(url_for('kardex_data.index', rut = request.form['rut']))