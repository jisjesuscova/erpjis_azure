from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.branch_offices.branch_office import BranchOffice
from app.check_group_question_details.check_group_question_detail import CheckGroupQuestionDetail

check_group_question = Blueprint("check_group_questions", __name__)

@check_group_question.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@check_group_question.route("/check_group_question/show/<int:id>", methods=['GET'])
def show(id):
   check_group_question_details = CheckGroupQuestionDetail.get(id)
   branch_offices = BranchOffice.get()
   check_group_question_quantity = CheckGroupQuestionDetail.quantity(id)

   return render_template('human_resource/check_group_question_details/check_group_question_details.html', id = id, check_group_question_quantity = check_group_question_quantity, check_group_question_details = check_group_question_details, branch_offices = branch_offices)