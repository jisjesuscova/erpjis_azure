from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import GenderModel
from app.genders.gender import Gender

gender = Blueprint("genders", __name__)

@gender.before_request
def constructor():
   pass

@gender.route("/master_data/genders/create", methods=['GET'])
def create():

   return render_template('master_data/genders/genders_create.html')

@gender.route("/master_data/genders", methods=['GET'])
@gender.route("/master_data/genders/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/genders/genders.html', genders = GenderModel.query.paginate(page=page, per_page=20, error_out=False))

@gender.route("/master_data/genders/store", methods=['POST'])
def store():
   Gender.store(request.form)

   return redirect(url_for('genders.index'))

@gender.route("/master_data/gender/<int:id>", methods=['GET'])
@gender.route("/master_data/gender", methods=['GET'])
def show(id):
   gender = Gender.get(id)

   return render_template('master_data/genders/genders_update.html', gender = gender, id = id)

@gender.route("/master_data/gender/<int:id>", methods=['POST'])
@gender.route("/master_data/gender", methods=['POST'])
def update(id):
   Gender.update(request.form, id)

   return redirect(url_for('genders.index'))

@gender.route("/master_data/gender/delete/<int:id>", methods=['GET'])
@gender.route("/master_data/gender/delete", methods=['GET'])
def delete(id):
   Gender.delete(id)

   return redirect(url_for('genders.index'))
