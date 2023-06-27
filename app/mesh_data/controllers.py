from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from app.branch_offices.branch_office import BranchOffice
from app.mesh_data.mesh_datum import MeshDatum
from app.total_mesh_data.total_mesh_datum import TotalMeshDatum
from app.documents_employees.document_employee import DocumentEmployee
from app.pre_employee_turns.pre_employee_turn import PreEmployeeTurn
from app.clock_attendances.clock_attendance import ClockAttendance

mesh_datum = Blueprint("mesh_data", __name__)

@mesh_datum.before_request
def constructor():
   pass

@mesh_datum.route("/mesh_data", methods=['GET', 'POST'])
def index():
   period = request.form.get('period')

   if period is not None:
      mesh_data = MeshDatum.get_all_with_df_group_by(period)
   else:
      mesh_data = ''

   title = "Mallas Horarias"
   module_name = "Gestión Tiempo"
   
   return render_template('human_resource/mesh_data/mesh_data.html', module_name = module_name, title = title, mesh_data = mesh_data)

@mesh_datum.route("/mesh_data/create", methods=['GET'])
def create():
   branch_offices = BranchOffice.get()
   
   return render_template('human_resource/mesh_data/mesh_data_create.html', branch_offices = branch_offices)

@mesh_datum.route("/mesh_data/store", methods=['POST'])
def store():
   id = DocumentEmployee.store_mesh_datum(request.form)
   MeshDatum.store(id, request.form)
   
   flash('Malla Horaria creada con éxito', 'success')

   return redirect(url_for('mesh_data.index'))

@mesh_datum.route("/mesh_data/pre_mesh_data/delete/<int:rut>", methods=['GET'])
def pre_mesh_data_delete(rut):
   PreEmployeeTurn.delete_by_rut(rut)
   
   return str('1')

@mesh_datum.route("/mesh_data/delete/<int:document_employee_id>/<int:rut>/<period>", methods=['GET'])
def delete(document_employee_id, rut, period):
   mesh_datum_status_id = MeshDatum.delete(rut, period)
   total_mesh_datum_status_id = TotalMeshDatum.delete(rut, period)
   document_employee_status_id = DocumentEmployee.delete(document_employee_id)
   
   return redirect(url_for('mesh_data.index'))

@mesh_datum.route("/mesh_data/report_per_days", methods=['GET'])
def report_per_days():
   date = ''

   return render_template('human_resource/mesh_data/report_mesh_data_per_days/report_mesh_data_per_days.html', date = date)

@mesh_datum.route("/mesh_data/report_per_days/search", methods=['GET', 'POST'])
def search_report_per_days():
   date = request.args.get('date')
   clock_attendances = ClockAttendance.registered_all_punch_hours(date)

   return render_template('human_resource/mesh_data/report_mesh_data_per_days/report_mesh_data_per_days.html', clock_attendances = clock_attendances.to_dict(orient='records'), date = date)

@mesh_datum.route("/mesh_data/report_per_branch_offices", methods=['GET'])
def report_per_branch_offices():
   branch_offices = BranchOffice.get()

   return render_template('human_resource/mesh_data/report_per_branch_offices/report_per_branch_offices.html', branch_offices = branch_offices)

@mesh_datum.route("/mesh_data/report_per_branch_office", methods=['GET'])
def show_report_per_branch_office():
   return render_template('human_resource/mesh_data/report_per_branch_offices/show_report_per_branch_office.html')

@mesh_datum.route("/mesh_data/get_data_per_branch_office", methods=['GET'])
def get_data_per_branch_office():

   mesh_data = MeshDatum.all_planned_mesh(80, '06-2023')

   return jsonify(mesh_data)