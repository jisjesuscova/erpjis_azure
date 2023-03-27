from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.employees.employee import Employee
from app.honoraries.honorary import Honorary

honorary = Blueprint("honoraries", __name__)

@honorary.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@honorary.route("/human_resources/honoraries", methods=['GET'])
def index():
   honoraries = Honorary.get()

   return render_template('administrator/human_resources/honoraries/honoraries.html', honoraries = honoraries)

@honorary.route("/human_resources/vacation/create/<int:rut>", methods=['GET'])
@honorary.route("/human_resources/vacation/create", methods=['GET'])
def create(rut):
   employees = Employee.get()

   return render_template('administrator/human_resources/vacations/vacations_create.html', rut = rut, employees = employees)