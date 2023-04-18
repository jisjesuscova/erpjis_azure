from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.checks.check import Check
from app.branch_offices.branch_office import BranchOffice
from app.months.month import Month
from app.years.year import Year
from app.check_group_questions.check_group_question import CheckGroupQuestion
from app.check_questions.check_question import CheckQuestion

check_group_question = Blueprint("check_group_questions", __name__)

@check_group_question.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@check_group_question.route("/check_group_question/show/<int:id>", methods=['GET'])
def index(id):
   check_group_questions = CheckGroupQuestion.get(id)

   return render_template('human_resource/checks/checks.html', check_group_questions = check_group_questions)