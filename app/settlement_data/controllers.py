import dropbox
from flask import Blueprint, render_template, redirect, request, url_for, make_response, send_file
from flask_login import login_required, current_user
from app import regular_employee_rol_need
from app.settlement_data.settlement_datum import SettlementDatum
from app.helpers.pdf import Pdf
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.dropbox_data.dropbox import Dropbox
from app.helpers.helper import Helper
from app.documents_employees.document_employee import DocumentEmployee
from app.old_documents_employees.old_document_employee import OldDocumentEmployee
import os
from app.helpers.file import File
from app.helpers.whatsapp import Whatsapp
from app.employees.employee import Employee
from app.old_employees.old_employee import OldEmployee
from app.documentation_titles.documentation_title import DocumentationTitle
from app.users.user import User
from dropbox.exceptions import AuthError, ApiError
from app.settings.setting import Setting

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
    documentation_titles_menu = DocumentationTitle.get()

    if status_id == 1:
        documents_employees = DocumentEmployee.get_by_type(rut, 5, page)
        employee  = Employee.get(rut)
    else:
        documents_employees = OldDocumentEmployee.get_by_type(rut, 5, page)
        employee  = OldEmployee.get(rut)

    settlement_button_status_id = 1

    title = employee.visual_rut + ' - ' + employee.names + ' ' + employee.father_lastname + ' ' + employee.mother_lastname
    module_name = 'Recursos Humanos'

    if current_user.rol_id == 1:
        return render_template('collaborator/management_payrolls/settlement_data/settlement_data_download.html', documentation_titles_menu = documentation_titles_menu, settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 2:
        return render_template('incharge/management_payrolls/settlement_data/settlement_data_download.html', documentation_titles_menu = documentation_titles_menu, settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 3:
        return render_template('supervisor/management_payrolls/settlement_data/settlement_data_download.html', documentation_titles_menu = documentation_titles_menu, settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 4:
        return render_template('human_resource/management_payrolls/settlement_data/settlement_data_download.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 5:
        return render_template('designer/management_payrolls/settlement_data/settlement_data_download.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)
    elif current_user.rol_id == 6:
        return render_template('management/management_payrolls/settlement_data/settlement_data_download.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, settlement_button_status_id = settlement_button_status_id, documents_employees = documents_employees, rut = rut)

@settlement_datum.route("/management_payroll/settlement_data/uploaded/<int:page>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/uploaded", methods=['GET'])
def uploaded(page = 1):
    documents_employees = DocumentEmployee.get_by_type('', 5, page)
    documentation_titles_menu = DocumentationTitle.get()

    values = ['', '', '', '']

    return render_template('human_resource/management_payrolls/settlement_data/settlement_data.html', documentation_titles_menu = documentation_titles_menu, documents_employees = documents_employees, values = values)


@settlement_datum.route("/management_payroll/settlement_data/create", methods=['GET'])
def create():
   documentation_titles_menu = DocumentationTitle.get()

   return render_template('human_resource/management_payrolls/settlement_data/settlement_data_create.html', documentation_titles_menu = documentation_titles_menu)


@settlement_datum.route("/management_payroll/settlement_data/store/<period>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/store", methods=['GET'])
def store(period = ''):

    SettlementDatum.store(period)

    return redirect(url_for('settlement_data.index', period = period))


@settlement_datum.route("/management_payroll/settlement_data/store", methods=['POST'])
def upload_store():
    settings = Setting.get()
    files = request.files.getlist('file')
    dbx = dropbox.Dropbox(settings.dropbox_token)
    month = request.form.get('month')
    year = request.form.get('year')
    period = year + '-' + month + '-01'

    for file in files:
        detail = Helper.split(file.filename, '_')
        file_path = '/salary_settlements/' + file.filename
        check_user_rut = User.check_rut(detail[3])
        check_employee_rut = Employee.check_rut(detail[3])

        if check_user_rut == 1 and check_employee_rut == 1:
            dbx.files_upload(file.stream.read(), file_path, mode=dropbox.files.WriteMode('overwrite'))
            document_id = DocumentEmployee.store_by_dropbox(detail[3], file.filename, 5, 3, period)
            Whatsapp.send(document_id, '1', 4, 12)

    return redirect(url_for('settlement_data.uploaded'))

    """
    files = request.files.getlist('file')
    month = request.form.get('month')
    year = request.form.get('year')
    period = year + '-' + month + '-01'

    for file in files:
        detail = Helper.split(file.filename, '_')
        check_user_rut = User.check_rut(detail[3])
        check_employee_rut = Employee.check_rut(detail[3])
        if check_user_rut == 1 and check_employee_rut == 1:
            filename = Dropbox.upload_local_cloud(detail[3] + "_" + str(month) + "-" + str(year), "_settlement", request.files, "/salary_settlements/", "app/static/dist/files/settlement_data/", 0)
            document_id = DocumentEmployee.store_by_dropbox(detail[3], filename, 5, 2, period)
            Whatsapp.send(document_id, '1', 4, 12)
    """
    return redirect(url_for('settlement_data.uploaded'))

@settlement_datum.route("/management_payroll/settlement_data/uploaded/download/<int:id>", methods=['GET'])
def uploaded_download(id):
    document_employee = DocumentEmployee.get_by_id(id)

    if document_employee.old_document_status_id == 1:
        response = Dropbox.get('/salary_settlements/', document_employee.support)

        return redirect(response)
    else:
        """
        settlement_datum = SettlementDatum.download(id)

        with open(os.path.join('app/static/dist/files/settlement_data/' + settlement_datum), 'rb') as f:
            data = f.read()

        response = make_response(data)
        response.headers['Content-Disposition'] = 'attachment; filename=' + settlement_datum
        response.headers['Content-Type'] = 'application/pdf'

        return response
        """
        response = Dropbox.get('/salary_settlements/', document_employee.support)

        return redirect(response)

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

@settlement_datum.route("/management_payroll/settlement_data/search/<int:page>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/search", methods=['GET'])
def search(page=1):
    rut = request.args.get('rut')
    names = request.args.get('names')
    father_lastname = request.args.get('father_lastname')
    mother_lastname = request.args.get('mother_lastname')

    documentation_titles_menu = DocumentationTitle.get()

    # Crear un arreglo para almacenar los valores
    values = []

    # Agregar los valores obtenidos al arreglo
    values.append(rut)
    values.append(names)
    values.append(father_lastname)
    values.append(mother_lastname)
    documents_employees = DocumentEmployee.get_by_type_array_data('', 5, page, values)

    return render_template('human_resource/management_payrolls/settlement_data/settlement_data_search.html', documentation_titles_menu = documentation_titles_menu, documents_employees = documents_employees, values = values)

@settlement_datum.route("/management_payroll/settlement_data/delete/<int:rut>/<int:id>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/delete", methods=['GET'])
def delete(rut, id):
    document_employee = DocumentEmployee.get_by_id(id)

    if document_employee.support != None:
        Dropbox.delete('/settlement_data/', document_employee.support)
        File.delete('app/static/dist/files/end_document_data', document_employee.support)

    DocumentEmployee.delete(id)

    return redirect(url_for('settlement_data.uploaded'))



