from flask import Blueprint, render_template, redirect, request, url_for
from app.branch_offices.branch_office import BranchOffice


mesh_datum = Blueprint("mesh_data", __name__)

@mesh_datum.before_request
def constructor():
   pass

@mesh_datum.route("/mesh_data", methods=['GET'])
def index():
   branch_offices = BranchOffice.get()
   
   return render_template('mesh_data/mesh_data.html', branch_offices = branch_offices)