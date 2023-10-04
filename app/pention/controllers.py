from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import PentionModel
from app.pention.pention import Pention

pention = Blueprint("pention", __name__)

@pention.before_request
def constructor():
   pass

@pention.route("/master_data/pention/create", methods=['GET'])
def create():

   return render_template('master_data/pention/pention_create.html')

@pention.route("/master_data/pention", methods=['GET'])
@pention.route("/master_data/pention/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/pention/pention.html', pention = PentionModel.query.paginate(page=page, per_page=20, error_out=False))
@pention.route("/master_data/pention/store", methods=['POST'])
def store():
   Pention.store(request.form)

   return redirect(url_for('pention.index'))


@pention.route("/master_data/pention/edit/<int:id>", methods=['GET'])
@pention.route("/master_data/pention/edit", methods=['GET'])
def edit(id):
   pention = Pention.get(id)

   return render_template('master_data/pention/pention_edit.html', pention = pention, id = id)

@pention.route("/master_data/pention/<int:id>", methods=['POST'])
@pention.route("/master_data/pention", methods=['POST'])
def update(id):
   Pention.update(request.form, id)

   return redirect(url_for('pention.index'))

@pention.route("/master_data/pention/delete/<int:id>", methods=['GET'])
@pention.route("/master_data/pention/delete", methods=['GET'])
def delete(id):
   Pention.delete(id)

   return redirect(url_for('pention.index'))
