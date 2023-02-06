from flask import Blueprint, render_template, redirect, request, url_for, jsonify

from app.models.models import CommunesModel
from app.region.region import Region
from app.communes.commune import Commune

commune = Blueprint("communes", __name__)

@commune.before_request
def constructor():
   pass

@commune.route("/master_data/communes/create", methods=['GET'])
def create():
   regions = Region.get()

   return render_template('master_data/communes/communes_create.html', regions= regions)

@commune.route("/master_data/communes", methods=['GET'])
@commune.route("/master_data/communes/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/communes/communes.html', communes = CommunesModel.query.paginate(page=page, per_page=20, error_out=False))

@commune.route("/master_data/communes/store", methods=['POST'])
def store():
   Commune.store(request.form)

   return redirect(url_for('communes.index'))

@commune.route("/master_data/communes/edit/<int:id>", methods=['GET'])
@commune.route("/master_data/communes/edit", methods=['GET'])
def edit(id):
   communes = Commune.get(id)

   return render_template('master_data/communes/communes_edit.html', communes = communes, id = id)

@commune.route("/master_data/communes/region/<int:id>", methods=['GET'])
def region(id):
   communes = Commune.region(id)
   
   return jsonify([commune.to_dict() for commune in communes])

@commune.route("/master_data/communes/<int:id>", methods=['POST'])
@commune.route("/master_data/communes", methods=['POST'])
def update(id):
   Commune.update(request.form, id)

   return redirect(url_for('communes.index'))

@commune.route("/master_data/communes/delete/<int:id>", methods=['GET'])
@commune.route("/master_data/communes/delete", methods=['GET'])
def delete(id):
   Commune.delete(id)

   return redirect(url_for('communes.index'))
