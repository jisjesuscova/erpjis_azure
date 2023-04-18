from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.employee_bank_accounts.employee_bank_account import EmployeeBankAccount
from app.helpers.whatsapp import Whatsapp

employee_bank_account = Blueprint("employee_bank_accounts", __name__)

@employee_bank_account.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@employee_bank_account.route("/human_resources/employee_bank_account/store", methods=['POST'])
def store():
   if current_user.rol_id == 4:
      id = EmployeeBankAccount.store(request.form, 1)
   else:
      id = EmployeeBankAccount.store(request.form, 0)

      if id != 0:
         Whatsapp.send(id, '1', 1, 18)

   flash('Se ha ingresado la solicitud de cambio de datos bancarios con éxito', 'success')

   if id != 0:
      return '1'
   else:
      return '0'

@employee_bank_account.route("/human_resources/employee_bank_account/accept/<int:id>", methods=['POST'])
def accept(id):
   status_id = EmployeeBankAccount.accept(id)

   flash('Se ha aceptado los datos bancarios con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'

@employee_bank_account.route("/human_resources/employee_bank_account/reject/<int:id>", methods=['POST'])
def reject(id):
   status_id = EmployeeBankAccount.delete(id)

   flash('Se ha rechazado los datos bancarios con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'
