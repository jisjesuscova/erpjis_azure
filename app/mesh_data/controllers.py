from flask import Blueprint, render_template, redirect, request, url_for
from app.branch_offices.branch_office import BranchOffice
from app.mesh_data.mesh_datum import MeshDatum

mesh_datum = Blueprint("mesh_data", __name__)

@mesh_datum.before_request
def constructor():
   pass

@mesh_datum.route("/mesh_data", methods=['GET'])
def index():
   branch_offices = BranchOffice.get()
   
   return render_template('administrator/mesh_data/mesh_data.html', branch_offices = branch_offices)

@mesh_datum.route("/mesh_data/store", methods=['POST'])
def store():
   status_id = MeshDatum.store(request.form)
   
   if status_id == 1:
      return '1'
   else:
      return '0'