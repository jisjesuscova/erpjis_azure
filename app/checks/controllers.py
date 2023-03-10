from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.checks.check import Check
from app.branch_offices.branch_office import BranchOffice
from app.months.month import Month
from app.years.year import Year
from app.check_group_questions.check_group_question import CheckGroupQuestion
from app.check_questions.check_question import CheckQuestion

check = Blueprint("checks", __name__)

@check.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@check.route("/checks", methods=['GET'])
@check.route("/checks/<int:page>", methods=['GET'])
def index(page=1):
   checks = Check.get('', page)

   return render_template('administrator/checks/checks.html', checks = checks)

@check.route("/check/create", methods=['GET'])
def create():
   months = Month.get()
   years = Year.get()
   branch_offices = BranchOffice.get()
   check_group_questions = CheckGroupQuestion.get()

   return render_template('administrator/checks/checks_create.html', branch_offices = branch_offices, months = months, years = years, check_group_questions = check_group_questions)

@check.route("/checks/store", methods=['POST'])
def store():
   check = Check.store(request.form)
   CheckQuestion.group_questions(check.id, request.form['check_group_question_id'])

   flash('La revisión ha sido creada con éxito', 'success')

   return redirect(url_for('checks.index'))

@check.route("/check/show/<int:id>", methods=['GET'])
def show(id):
   check = Check.get(id)

   check_questions = CheckQuestion.get(id)

   title = check.check_title

   return render_template('administrator/checks/check_questions.html', title = title, check_questions = check_questions)

@check.route("/check/answer/<int:check_id>/<int:check_question_id>", methods=['GET'])
def answer(check_id, check_question_id):
   check_question = CheckQuestion.get_filter_by('', id)

   return render_template('administrator/checks/check_answers_create.html', check_question = check_question, check_id = check_id, check_question_id = check_question_id)

@check.route("/check/delete/<int:id>", methods=['GET'])
def delete(id):
   Check.delete(id)
   CheckQuestion.delete(id)

   flash('Se ha borrado la revisión con éxito', 'success')

   return redirect(url_for('checks.index'))