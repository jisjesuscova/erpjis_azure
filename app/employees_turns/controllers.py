from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.employees_turns.employee_turn import EmployeeTurn

employee_turn = Blueprint("employees_turns", __name__)

@employee_turn.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@employee_turn.route("/employees_turns/check/<int:rut>", methods=['GET'])
@employee_turn.route("/employees_turns/check", methods=['GET'])
def check(rut):
    EmployeeTurn.delete_old_ones(rut)
    
    return str(1)