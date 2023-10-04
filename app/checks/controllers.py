from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.checks.check import Check
from app.branch_offices.branch_office import BranchOffice
from app.months.month import Month
from app.years.year import Year
from app.check_group_questions.check_group_question import CheckGroupQuestion
from app.check_questions.check_question import CheckQuestion
from app.models.models import VacationModel, DocumentEmployeeModel, EndDocumentModel
from app import db
from datetime import datetime

check = Blueprint("checks", __name__)

@check.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@check.route("/checks/test", methods=['GET'])
def test():
   documents_employees = DocumentEmployeeModel.query.filter(
      DocumentEmployeeModel.document_type_id == 22,
      DocumentEmployeeModel.id > 5876
   ).all()

   i = 1

   for documents_employee in documents_employees:
      end_document = EndDocumentModel.query.filter_by(id=i).first()
      end_document.document_employee_id = documents_employee.id
      end_document.updated_date = datetime.now()

      db.session.add(end_document)

      db.session.commit()

      i = i + 1

   return '1'

@check.route("/checks/validate", methods=['GET'])
def validate():
   documents_employees = DocumentEmployeeModel.query.filter_by(document_type_id=5).all()

   for documents_employee in documents_employees:

      if documents_employee.support != None:
         d_e_m_u = DocumentEmployeeModel.query.filter_by(id=documents_employee.id).first()
         d_e_m_u.status_id = 4

         db.session.add(d_e_m_u)

         db.session.commit()

   return '1'

@check.route("/checks", methods=['GET'])
@check.route("/checks/<int:page>", methods=['GET'])
def index(page=1):
   checks = Check.get('', page)
   title = 'Revisión'
   module_name = 'Revisión'

   return render_template('human_resource/checks/checks.html', title = title, module_name = module_name, checks = checks)

@check.route("/check/create", methods=['GET'])
def create():
   months = Month.get()
   years = Year.get()
   branch_offices = BranchOffice.get()
   check_group_questions = CheckGroupQuestion.get()
   title = 'Crear Revisión'
   module_name = 'Revisión'

   return render_template('human_resource/checks/checks_create.html', title = title, module_name = module_name, branch_offices = branch_offices, months = months, years = years, check_group_questions = check_group_questions)

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

   return render_template('human_resource/checks/check_questions.html', title = title, check_questions = check_questions)

@check.route("/check/answer/<int:check_id>/<int:check_question_id>", methods=['GET'])
def answer(check_id, check_question_id):
   check_question = CheckQuestion.get_filter_by('', id)

   return render_template('human_resource/checks/check_answers_create.html', check_question = check_question, check_id = check_id, check_question_id = check_question_id)

@check.route("/check/delete/<int:id>", methods=['GET'])
def delete(id):
   Check.delete(id)
   CheckQuestion.delete(id)

   flash('Se ha borrado la revisión con éxito', 'success')

   return redirect(url_for('checks.index'))