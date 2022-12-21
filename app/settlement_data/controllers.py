from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.settlement_data.settlement_datum import SettlementDatum
from app.helpers.pdf import Pdf
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput

settlement_datum = Blueprint("settlement_data", __name__)

@settlement_datum.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@settlement_datum.route("/management_payroll/settlement_data/<period>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data", methods=['GET'])
def index(period = ''):

    settlements = SettlementDatum.get(period)

    return render_template('management_payrolls/settlement_data/settlement_data_download.html', settlements = settlements, period = period)


@settlement_datum.route("/management_payroll/settlement_data/store/<period>", methods=['GET'])
@settlement_datum.route("/management_payroll/settlement_data/store", methods=['GET'])
def store(period = ''):

    SettlementDatum.store(period)

    return redirect(url_for('settlement_data.index', period = period))


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
    print(negative_data)
    response = Pdf.create_settlement('settlement', header_data, positive_data, settlement_positive_name, negative_data, settlement_negative_name, total_positive_data, total_negative_data, total_values)

    return response

