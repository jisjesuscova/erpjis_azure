from flask import Blueprint, render_template, redirect, request, url_for, flash
from app.branch_offices.branch_office import BranchOffice
from app.mesh_data.mesh_datum import MeshDatum
from app.total_mesh_data.total_mesh_datum import TotalMeshDatum
from app.documents_employees.document_employee import DocumentEmployee

mesh_datum = Blueprint("mesh_data", __name__)

@mesh_datum.before_request
def constructor():
   pass

@mesh_datum.route("/mesh_data", methods=['GET'])
def index():
   total_mesh_data = TotalMeshDatum.get()
   title = "Mallas Horarias"
   module_name = "Gestión Tiempo"
   
   return render_template('human_resource/mesh_data/mesh_data.html', module_name = module_name, title = title, total_mesh_data = total_mesh_data)

@mesh_datum.route("/mesh_data/create", methods=['GET'])
def create():
   branch_offices = BranchOffice.get()
   
   return render_template('human_resource/mesh_data/mesh_data_create.html', branch_offices = branch_offices)

@mesh_datum.route("/mesh_data/store", methods=['POST'])
def store():
   id = DocumentEmployee.store(request.form)
   MeshDatum.store(id, request.form)
   
   flash('Malla Horaria creada con éxito', 'success')

   return redirect(url_for('mesh_data.index'))

@mesh_datum.route("/mesh_data/delete/<int:document_employee_id>/<int:rut>/<period>", methods=['GET'])
def delete(document_employee_id, rut, period):
   mesh_datum_status_id = MeshDatum.delete(rut, period)
   total_mesh_datum_status_id = TotalMeshDatum.delete(rut, period)
   document_employee_status_id = DocumentEmployee.delete(document_employee_id)
   
   if mesh_datum_status_id == 1 and total_mesh_datum_status_id == 1 and document_employee_status_id == 1:
      return '1'
   else:
      return '0'