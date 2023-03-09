from flask import Blueprint, redirect, request, url_for, flash, render_template
from flask_login import login_required
from app import regular_employee_rol_need
from app.dropbox_data.dropbox import Dropbox
from app.check_answers.check_answer import CheckAnswer
from app.check_questions.check_question import CheckQuestion
from app.helpers.file import File
from app.checks.check import Check

check_answer = Blueprint("check_answers", __name__)

@check_answer.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@check_answer.route("/check_answer/store", methods=['POST'])
def store():
   check_question_id = CheckQuestion.status(request.form['check_question_id'])

   if check_question_id == 1:
      if request.files['file'].filename != '':
         support = Dropbox.upload(request.form['check_question_id'], '_check', request.files, "/checks/", "app/static/dist/files/check_data/")
         CheckAnswer.store(request.form, support)
         CheckQuestion.update(request.form['check_question_id'], 2)
   else:
      check_answer = CheckAnswer.get(request.form['check_question_id'])
      Dropbox.delete('/checks/', check_answer.support)
      File.delete("app/static/dist/files/check_data/", check_answer.support)
      
      if request.files['file'].filename != '':
         support = Dropbox.upload(request.form['check_question_id'], '_check', request.files, "/checks/", "app/static/dist/files/check_data/")
         CheckAnswer.update(request.form, support)
         CheckQuestion.update(request.form['check_question_id'], 2)

   flash('La pregunta ha sido respondida con éxito', 'success')

   return redirect(url_for('checks.show', id = request.form['check_id']))

@check_answer.route("/check_answer/show/<int:check_id>/<int:check_question_id>", methods=['GET'])
def show(check_id, check_question_id):
   check = Check.get(check_id)
   check_question = CheckQuestion.get_filter_by(check_question_id)
   check_answer = CheckAnswer.get(check_question_id)

   return render_template('administrator/checks/check_answers_show.html', check = check, check_question = check_question, check_answer = check_answer)
