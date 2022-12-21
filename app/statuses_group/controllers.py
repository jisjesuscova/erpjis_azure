from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import statuses_groupModel
from app.statuses_group.statuses_group import Statuses_group

statuses_group = Blueprint("statuses_group", __name__)

@statuses_group.before_request
def constructor():
   pass

@statuses_group.route("/master_data/statuses_group/create", methods=['GET'])
def create():

   return render_template('master_data/statuses_group/statuses_group_create.html')

@statuses_group.route("/master_data/statuses_group", methods=['GET'])
@statuses_group.route("/master_data/statuses_group/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/statuses_group/statuses_group.html', statuses_group = statuses_groupModel.query.paginate(page=page, per_page=20, error_out=False))
@statuses_group.route("/master_data/statuses_group/store", methods=['POST'])
def store():
   Statuses_group.store(request.form)

   return redirect(url_for('statuses_group.index'))


@statuses_group.route("/master_data/statuses_group/edit/<int:id>", methods=['GET'])
@statuses_group.route("/master_data/statuses_group/edit", methods=['GET'])
def edit(id):
   statuses_group = Statuses_group.get(id)

   return render_template('master_data/statuses_group/statuses_group_edit.html', statuses_group = statuses_group, id = id)

@statuses_group.route("/master_data/statuses_group/<int:id>", methods=['POST'])
@statuses_group.route("/master_data/statuses_group", methods=['POST'])
def update(id):
   Statuses_group.update(request.form, id)

   return redirect(url_for('statuses_group.index'))

@statuses_group.route("/master_data/statuses_group/delete/<int:id>", methods=['GET'])
@statuses_group.route("/master_data/statuses_group/delete", methods=['GET'])
def delete(id):
   Statuses_group.delete(id)

   return redirect(url_for('statuses_group.index'))
