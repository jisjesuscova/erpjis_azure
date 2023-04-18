from flask import Blueprint, redirect, request, url_for, flash, render_template
from flask_login import login_required
from app import regular_employee_rol_need
from app.dropbox_data.dropbox import Dropbox
from app.check_answers.check_answer import CheckAnswer
from app.check_questions.check_question import CheckQuestion
from app.helpers.file import File
from app.checks.check import Check
from app.check_group_question_details.check_group_question_detail import CheckGroupQuestionDetail

check_answer = Blueprint("check_answers", __name__)

@check_answer.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@check_answer.route("/check_answer/store", methods=['POST'])
def store():
   id = request.form['id']

   if 'file' in request.files:
      if request.files['file'].filename != '':
         support = Dropbox.upload(id, '_foto', request.files, "/checks/", "app/static/dist/files/check_data/", 0)
      else:
         support = ''
   else:
      support = ''
   
   CheckGroupQuestionDetail.store(request.form, id, support)

   return '1'

@check_answer.route("/check_answer/show/<int:check_id>/<int:check_question_id>", methods=['GET'])
def show(check_id, check_question_id):
   check = Check.get(check_id)
   check_question = CheckQuestion.get_filter_by(check_question_id)
   check_answer = CheckAnswer.get(check_question_id)

   return render_template('human_resource/checks/check_answers_show.html', check = check, check_question = check_question, check_answer = check_answer)
