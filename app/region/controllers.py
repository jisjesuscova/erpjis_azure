from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import RegionModel
from app.region.region import Region

region = Blueprint("region", __name__)

@region.before_request
def constructor():
   pass

@region.route("/master_data/region/create", methods=['GET'])
def create():

   return render_template('master_data/region/region_create.html')

@region.route("/master_data/region", methods=['GET'])
@region.route("/master_data/region/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/region/region.html', region = RegionModel.query.paginate(page=page, per_page=20, error_out=False))
@region.route("/master_data/region/store", methods=['POST'])
def store():
   Region.store(request.form)

   return redirect(url_for('region.index'))


@region.route("/master_data/region/edit/<int:id>", methods=['GET'])
@region.route("/master_data/region/edit", methods=['GET'])
def edit(id):
   region = Region.get(id)

   return render_template('master_data/region/region_edit.html', region = region, id = id)

@region.route("/master_data/region/<int:id>", methods=['POST'])
@region.route("/master_data/region", methods=['POST'])
def update(id):
   Region.update(request.form, id)

   return redirect(url_for('region.index'))

@region.route("/master_data/region/delete/<int:id>", methods=['GET'])
@region.route("/master_data/region/delete", methods=['GET'])
def delete(id):
   Region.delete(id)

   return redirect(url_for('region.index'))
