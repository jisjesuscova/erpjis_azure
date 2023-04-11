from flask import Blueprint, render_template, redirect, request, url_for, make_response, send_file
from flask_login import login_required, current_user
from app import regular_employee_rol_need
from app.settlement_data.settlement_datum import SettlementDatum
from app.helpers.pdf import Pdf
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.dropbox_data.dropbox import Dropbox
from app.helpers.helper import Helper
from app.documents_employees.document_employee import DocumentEmployee
from app.helpers.helper import Helper
from app.old_documents_employees.old_document_employee import OldDocumentEmployee
import os
from app.helpers.file import File
from app.helpers.whatsapp import Whatsapp

settlement_datum = Blueprint("settlement_data", __name__)

@settlement_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@settlement_datum.route("/management_payroll/settlement_data/<int:rut>/<int:page>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/<int:rut>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data", methods=['GET'])
def index(rut = '', page = 1):
    status_id = Helper.is_active(rut)

    if status_id == 1:
        documents_employees = DocumentEmployee.get_by_type(rut, 5, page)
    else:
        documents_employees = OldDocumentEmployee.get_by_type(rut, 5, page)

    settlement_button_status_id = 1

    if current_user.rol_id == 1:
        return render_template('collaborator/management_payrolls/settlement_data/settlement_data_download.html', settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 2:
        return render_template('incharge/management_payrolls/settlement_data/settlement_data_download.html', settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 3:
        return render_template('supervisor/management_payrolls/settlement_data/settlement_data_download.html', settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 4:
        return render_template('administrator/management_payrolls/settlement_data/settlement_data_download.html', settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)

@settlement_datum.route("/management_payroll/settlement_data/uploaded/<int:page>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/uploaded", methods=['GET'])
def uploaded(page = 1):
    documents_employees = DocumentEmployee.get_by_type('', 5, page)

    return render_template('administrator/management_payrolls/settlement_data/settlement_data.html', documents_employees = documents_employees)


@settlement_datum.route("/management_payroll/settlement_data/create", methods=['GET'])
def create():

   return render_template('administrator/management_payrolls/settlement_data/settlement_data_create.html')


@settlement_datum.route("/management_payroll/settlement_data/store/<period>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/store", methods=['GET'])
def store(period = ''):

    SettlementDatum.store(period)

    return redirect(url_for('settlement_data.index', period = period))


@settlement_datum.route("/management_payroll/settlement_data/store", methods=['POST'])
def upload_store():
    files = request.files.getlist('file')
    month = request.form.get('month')
    year = request.form.get('year')
    period = year + '-' + month + '-01'

    for file in files:
        detail = Helper.split(file.filename, '_')
        filename = Dropbox.upload_local_cloud(detail[3] + "_" + str(month) + "-" + str(year), "_settlement", request.files, "/salary_settlements/", "app/static/dist/files/settlement_data/", 0)
        document_id = DocumentEmployee.store_by_dropbox(detail[3], filename, 5, 2, period)
        Whatsapp.send(document_id, '1', 4, 12)

    return redirect(url_for('settlement_data.uploaded'))

@settlement_datum.route("/management_payroll/settlement_data/uploaded/download/<int:id>", methods=['GET'])
def uploaded_download(id):
    document_employee = DocumentEmployee.get_by_id(id)

    if document_employee.old_document_status_id == 1:
        response = Dropbox.get('/salary_settlements/', document_employee.support)

        return redirect(response)
    else:
        settlement_datum = SettlementDatum.download(id)

        with open(os.path.join('app/static/dist/files/settlement_data/' + settlement_datum), 'rb') as f:
            data = f.read()

        response = make_response(data)
        response.headers['Content-Disposition'] = 'attachment; filename=' + settlement_datum
        response.headers['Content-Type'] = 'application/pdf'

        return response

@settlement_datum.route("/management_payroll/settlement_data/uploaded/sign/<int:id>", methods=['GET'])
def sign(id):
    document_employee = DocumentEmployee.get_by_id(id)

    if document_employee.old_document_status_id == 1:
        response = Dropbox.get('/salary_settlements/', document_employee.support)

        return redirect(response)
    else:
        settlement_datum = SettlementDatum.download(id)

        with open(os.path.join('app/static/dist/files/settlement_data/' + settlement_datum), 'rb') as f:
            data = f.read()

        response = make_response(data)
        response.headers['Content-Disposition'] = 'attachment; filename=' + settlement_datum
        response.headers['Content-Type'] = 'application/pdf'

        return response


@settlement_datum.route("/management_payroll/settlement_data/download/<rut>/<period>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/download", methods=['GET'])
def download(rut = '', period = ''):
    header_data = HrEmployeeInput.header_settlement(rut, period)
    positive_data = HrEmployeeInput.positive_settlement(rut, period)
    negative_data = HrEmployeeInput.negative_settlement(rut, period)
    settlement_positive_name = HrEmployeeInput.settlement_positive_name(rut, period)
    settlement_negative_name = HrEmployeeInput.settlement_negative_name(rut, period)
    total_positive_data = HrEmployeeInput.total_settlement(settlement_positive_name)
    total_negative_data = HrEmployeeInput.total_settlement(settlement_negative_name)
    total_values = HrEmployeeInput.total_values(rut, period)

    response = Pdf.create_settlement('settlement', header_data, positive_data, settlement_positive_name, negative_data, settlement_negative_name, total_positive_data, total_negative_data, total_values)

    return response

@settlement_datum.route("/management_payroll/settlement_data/search/<int:page>", methods=['POST'])
def search(page=1):
   documents_employees = DocumentEmployee.get_by_type('', 5, page, request.form)

   return render_template('administrator/management_payrolls/settlement_data/settlement_data.html', documents_employees = documents_employees)

@settlement_datum.route("/management_payroll/settlement_data/delete/<int:rut>/<int:id>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/delete", methods=['GET'])
def delete(rut, id):
    document_employee = DocumentEmployee.get_by_id(id)

    if document_employee.support != None:
        Dropbox.delete('/settlement_data/', document_employee.support)
        File.delete('app/static/dist/files/end_document_data', document_employee.support)

    DocumentEmployee.delete(id)

    return redirect(url_for('settlement_data.uploaded'))



