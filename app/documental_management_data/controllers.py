from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.models.models import EmployeeModel, DocumentTypeModel
from app.document_types.document_type import DocumentType
from datetime import datetime
from app.documents_employees.document_employee import DocumentEmployee
from app.kardex_data.kardex_datum import KardexDatum

documental_management_datum = Blueprint("documental_management_data", __name__)

@documental_management_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@documental_management_datum.route("/human_resources/documental_management_datum/create", methods=['GET'])
def create():
   if current_user.rol_id == 1:
      document_type_values = [2, 4]

      document_types = DocumentType.get('', 2, '', '', document_type_values)
   else:
      document_types = DocumentType.get('', 2, '', '', '')
   
   return render_template('human_resources/documental_management_data/documental_management_data_create.html', document_types = document_types)

@documental_management_datum.route("/human_resources/documental_management_data", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/<int:page>", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/<int:rut>/<int:page>", methods=['GET'])
def index(rut = '', page=1):
   documents_employees = KardexDatum.get(rut)

   return render_template('human_resources/documental_management_data/documental_management_data.html', employees = EmployeeModel.query.paginate(page=page, per_page=20, error_out=False), documents_employees = documents_employees)


@documental_management_datum.route("/human_resources/documental_management_data/show/<int:rut><int:page>", methods=['GET'])
@documental_management_datum.route("/human_resources/documental_management_data/show", methods=['GET'])
def show(rut, page=1):
   documents_employees = DocumentEmployee.get(rut, page)

   return render_template('human_resources/documental_management_data/documental_management_data_documents.html', documents_employees = documents_employees)

