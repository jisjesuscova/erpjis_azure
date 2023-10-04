from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import StatusesModel
from app.statuses_group.statuses_group import Statuses_group
from app.statuses.statuses import Statuses

statuses = Blueprint("statuses", __name__)

@statuses.before_request
def constructor():
   pass

@statuses.route("/master_data/statuses/create", methods=['GET'])
def create():
   statuses_groups = Statuses_group.get()

   return render_template('master_data/statuses/statuses_create.html', statuses_groups = statuses_groups)

@statuses.route("/master_data/statuses", methods=['GET'])
@statuses.route("/master_data/statuses/<int:page>", methods=['GET'])
def index(page=1): 
   statuses = Statuses.get()
   return render_template('master_data/statuses/statuses.html', statuses = statuses)
@statuses.route("/master_data/statuses/store", methods=['POST'])
def store():
   Statuses.store(request.form)

   return redirect(url_for('statuses.index'))


@statuses.route("/master_data/statuses/edit/<int:id>", methods=['GET'])
@statuses.route("/master_data/statuses/edit", methods=['GET'])
def edit(id):
   statuses = Statuses.get(id)

   return render_template('master_data/statuses/statuses_edit.html', statuses = statuses, id = id)

@statuses.route("/master_data/statuses/<int:id>", methods=['POST'])
@statuses.route("/master_data/statuses", methods=['POST'])
def update(id):
   Statuses.update(request.form, id)

   return redirect(url_for('statuses.index'))

@statuses.route("/master_data/statuses/delete/<int:id>", methods=['GET'])
@statuses.route("/master_data/statuses/delete", methods=['GET'])
def delete(id):
   Statuses.delete(id)

   return redirect(url_for('statuses.index'))
