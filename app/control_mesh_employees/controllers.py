from flask import Blueprint, render_template_string, render_template, request, redirect, url_for, flash, jsonify, session, current_app
from app.total_mesh_data.total_mesh_datum import TotalMeshDatum

control_mesh_employee = Blueprint("control_mesh_employees", __name__)

@control_mesh_employee.before_request
def constructor():
   pass

@control_mesh_employee.route("/control_mesh_employee/<int:page>", methods=['GET'])
@control_mesh_employee.route("/control_mesh_employee", methods=['GET'])
def index(page=1):
   total_mesh_data = TotalMeshDatum.get_by_period('06-2023', page)
   title = "Control Tiempo"
   module_name = "Gestión Tiempo"
   
   return render_template('human_resource/control_mesh_employees/control_mesh_employee.html', module_name = module_name, title = title, total_mesh_data = total_mesh_data)

