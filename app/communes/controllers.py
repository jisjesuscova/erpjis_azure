from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import CommunesModel
from app.region.region import Region
from app.communes.communes import Communes

communes = Blueprint("communes", __name__)

@communes.before_request
def constructor():
   pass

@communes.route("/master_data/communes/create", methods=['GET'])
def create():
   regions = Region.get()

   return render_template('master_data/communes/communes_create.html', regions= regions)

@communes.route("/master_data/communes", methods=['GET'])
@communes.route("/master_data/communes/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/communes/communes.html', communes = CommunesModel.query.paginate(page=page, per_page=20, error_out=False))
@communes.route("/master_data/communes/store", methods=['POST'])
def store():
   Communes.store(request.form)

   return redirect(url_for('communes.index'))


@communes.route("/master_data/communes/edit/<int:id>", methods=['GET'])
@communes.route("/master_data/communes/edit", methods=['GET'])
def edit(id):
   communes = Communes.get(id)

   return render_template('master_data/communes/communes_edit.html', communes = communes, id = id)

@communes.route("/master_data/communes/<int:id>", methods=['POST'])
@communes.route("/master_data/communes", methods=['POST'])
def update(id):
   Communes.update(request.form, id)

   return redirect(url_for('communes.index'))

@communes.route("/master_data/communes/delete/<int:id>", methods=['GET'])
@communes.route("/master_data/communes/delete", methods=['GET'])
def delete(id):
   Communes.delete(id)

   return redirect(url_for('communes.index'))
