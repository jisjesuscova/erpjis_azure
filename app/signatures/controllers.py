from flask import Blueprint, request, redirect, url_for
from app.dropbox_data.dropbox import Dropbox
from app import csrf_protect
import base64
from app.employees.employee import Employee
from flask_login import current_user

signature = Blueprint("signatures", __name__)

@signature.route("/signature/store", methods=['POST'])
@csrf_protect.exempt
def store():
    signature = request.form['signature']
    signature = signature.split(',')
    signature = signature[1]

    signature = base64.b64decode(signature)

    signature = Dropbox.signature(signature)

    Employee.update_signature(signature, current_user.rut)

    return redirect(url_for('personal_data.show', rut = current_user.rut))

@signature.route("/signature/delete", methods=['GET'])
@csrf_protect.exempt
def delete():
    rut = current_user.rut

    employee = Employee.get(rut)

    Dropbox.delete('/signatures/', employee.signature)

    Employee.update_signature('', current_user.rut)

    return redirect(url_for('personal_data.show', rut = rut))