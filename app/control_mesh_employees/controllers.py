from flask import Blueprint, render_template_string, render_template, request, redirect, url_for, flash, jsonify, session, current_app
from app.total_mesh_data.total_mesh_datum import TotalMeshDatum
from app.mesh_data.mesh_datum import MeshDatum
from app.clock_attendances.clock_attendance import ClockAttendance

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

@control_mesh_employee.route("/control_mesh_employee/show/<int:rut>/<period>", methods=['GET'])
def show(rut, period):
   exist_start_end_mark = ClockAttendance.check_exist_marks(rut, period)

   if exist_start_end_mark == 1:
      mesh_data = MeshDatum.planned_mesh(rut, period)
      clock_attendances = ClockAttendance.registered_hours(rut, period)
      total_mesh_clock_data = ClockAttendance.controlled_hours(mesh_data, clock_attendances)
      mesh_data_grouped_by_week = MeshDatum.planned_mesh_by_week(rut, period)
      clock_attendances_grouped_by_week = ClockAttendance.registered_hours_by_week(total_mesh_clock_data)
      total_grouped_by_week = ClockAttendance.controlled_hours_by_week(mesh_data_grouped_by_week, clock_attendances_grouped_by_week)

      title = "Detalle del Control Tiempo"
      module_name = "Gestión Tiempo"
      return render_template('human_resource/control_mesh_employees/show_control_mesh_employee.html', module_name = module_name, title = title, mesh_data = mesh_data.to_dict(orient='records'), clock_attendances = clock_attendances.to_dict(orient='records'), total_mesh_clock_data = total_mesh_clock_data.to_dict(orient='records'), mesh_data_grouped_by_week = mesh_data_grouped_by_week.to_dict(orient='records'), clock_attendances_grouped_by_week = clock_attendances_grouped_by_week.to_dict(orient='records'), total_grouped_by_week = total_grouped_by_week.to_dict(orient='records'))
   else:
      flash('El trabajador no tiene marcas en el mes.', 'error')

      return redirect(url_for('mesh_data.index'))
