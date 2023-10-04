from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import ZoneModel
from app.zones.zone import Zone

zone = Blueprint("zones", __name__)

@zone.before_request
def constructor():
   pass

@zone.route("/master_data/zones/create", methods=['GET'])
def create():

   return render_template('master_data/zones/zones_create.html')

@zone.route("/master_data/zones", methods=['GET'])
@zone.route("/master_data/zones/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/zones/zone.html', zones = ZoneModel.query.paginate(page=page, per_page=20, error_out=False))

@zone.route("/master_data/zones/store", methods=['POST'])
def store():
   Zone.store(request.form)

   return redirect(url_for('zones.index'))


@zone.route("/master_data/zones/edit/<int:id>", methods=['GET'])
@zone.route("/master_data/zones/edit", methods=['GET'])
def edit(id):
   zone = Zone.get(id)

   return render_template('master_data/zones/zones_edit.html', zone = zone, id = id)

@zone.route("/master_data/zones/<int:id>", methods=['POST'])
@zone.route("/master_data/zones", methods=['POST'])
def update(id):
   Zone.update(request.form, id)

   return redirect(url_for('zones.index'))

@zone.route("/master_data/zones/delete/<int:id>", methods=['GET'])
@zone.route("/master_data/zones/delete", methods=['GET'])
def delete(id):
   Zone.delete(id)

   return redirect(url_for('zones.index'))
