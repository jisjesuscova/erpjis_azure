from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.branch_offices.branch_office import BranchOffice
from app.honoraries.honorary import Honorary

honorary = Blueprint("honoraries", __name__)

@honorary.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@honorary.route("/human_resources/honoraries/<int:page>", methods=['GET'])
@honorary.route("/human_resources/honoraries", methods=['GET'])
def index(page=1):
   honoraries = Honorary.get(page)

   title = "Honorarios"

   module_name = "Recursos Humanos"

   return render_template('administrator/human_resources/honoraries/honoraries.html', honoraries = honoraries, title = title, module_name = module_name)

@honorary.route("/human_resources/honorary/create", methods=['GET'])
def create():
   branch_offices = BranchOffice.get()

   return render_template('administrator/human_resources/honoraries/honoraries_create.html', branch_offices = branch_offices)