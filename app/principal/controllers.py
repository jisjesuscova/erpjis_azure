from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import PrincipalModel
from app.principal.principal import Principal

principal = Blueprint("principal", __name__)

@principal.before_request
def constructor():
   pass

@principal.route("/master_data/principal/create", methods=['GET'])
def create():

   return render_template('master_data/principal/principal_create.html')

@principal.route("/master_data/principal", methods=['GET'])
@principal.route("/master_data/principal/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/principal/principal.html', principal = PrincipalModel.query.paginate(page=page, per_page=20, error_out=False))
@principal.route("/master_data/principal/store", methods=['POST'])
def store():
   Principal.store(request.form)

   return redirect(url_for('principal.index'))


@principal.route("/master_data/principal/edit/<int:id>", methods=['GET'])
@principal.route("/master_data/principal/edit", methods=['GET'])
def edit(id):
   principal = Principal.get(id)

   return render_template('master_data/principal/principal_edit.html', principal = principal, id = id)

@principal.route("/master_data/principal/<int:id>", methods=['POST'])
@principal.route("/master_data/principal", methods=['POST'])
def update(id):
   Principal.update(request.form, id)

   return redirect(url_for('principal.index'))

@principal.route("/master_data/principal/delete/<int:id>", methods=['GET'])
@principal.route("/master_data/principal/delete", methods=['GET'])
def delete(id):
   Principal.delete(id)

   return redirect(url_for('principal.index'))
