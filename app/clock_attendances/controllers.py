from flask import Blueprint, request, render_template, redirect, url_for, flash, session, jsonify
from flask_login import login_required, current_user
from app import regular_employee_rol_need
from app.clock_attendances.clock_attendance import ClockAttendance
from app.mesh_data.mesh_datum import MeshDatum
import pytz
import datetime
from app.alerts.alert import Alert
from app.helpers.whatsapp import Whatsapp
from app.control_clock_no_marks.control_clock_no_mark import ControlClockNoMark
from app.helpers.helper import Helper
from app.clock_attendances.clock_attendance import ClockAttendance
from app.employees.employee import Employee

clock_attendance = Blueprint("clock_attendances", __name__)

@clock_attendance.before_request
def constructor():
   if request.endpoint == 'clock_attendances.special_store' or request.endpoint == 'clock_attendances.mark':
      if not current_user.is_authenticated:
            return redirect(url_for('login'))

@clock_attendance.route("/clock_attendance/store", methods=['GET'])
def store():
   data = ClockAttendance.store(request.form)

   return str(data)

@clock_attendance.route("/clock_attendance/special_store", methods=['POST'])
def special_store():
   
   date = Helper.split(request.form['added_date'], '-')
   date = date [2] +"-"+ date [1] +"-"+ date [0]
   mark_date = date + ' ' + request.form['mark_hour']
   ClockAttendance.special_store(request.form, mark_date)
   ControlClockNoMark.update(request.form['id'], mark_date)

   flash('Usted ha marcado correctamente')

   return redirect(url_for('clock_attendances.mark'))

@clock_attendance.route("/clock_attendance/check", methods=['POST'])
def check():
   if request.form['status_id'] == '2':
      ControlClockNoMark.update_status(request.form['id'], 2)

      flash('Usted ha aceptado la marca', 'success')
   else:
      Whatsapp.send(request.form['rut'], str(1), '', 21)

      ControlClockNoMark.delete(request.form['id'])

      clock_attendance = ClockAttendance.get_by_mark_date(request.form['rut'], request.form['mark_date'])

      ClockAttendance.delete(clock_attendance.id)

      flash('Usted ha rechazado la marca', 'success')

   return redirect(url_for('clock_attendances.mark'))


@clock_attendance.route("/clock_attendance/mark", methods=['GET'])
def mark():
   title = "Marcas faltantes"

   module_name = "Gestión tiempo"
   
   if current_user.rol_id == 1:
      mark_data = ControlClockNoMark.get(current_user.rut)

      return render_template('collaborator/clocks/mark_data.html', mark_data = mark_data, title = title, module_name = module_name)
   else:
      mark_data = ControlClockNoMark.get()

      return render_template('human_resource/clocks/mark_data.html', mark_data = mark_data, title = title, module_name = module_name)

@clock_attendance.route("/clock_attendance/validate", methods=['GET'])
def validate():
   santiago_timezone = pytz.timezone('Chile/Continental')
   current_date = datetime.datetime.now(santiago_timezone).date()
   format_current_date = current_date.strftime("%Y-%m-%d")

   current_hour = datetime.datetime.now(santiago_timezone).time()
   format_current_hour = current_hour.strftime("%H:%M:%S")

   mesh_data = MeshDatum.get_by_date(format_current_date)

   for mesh_datum in mesh_data:
      check_attendance_id = ClockAttendance.checked_attedance(mesh_datum.rut, format_current_date, 0)
      check_alert_id = Alert.check_alert(mesh_datum.rut, format_current_date, 1)

      if check_attendance_id == 1 and check_alert_id == 0:

         entrance_status = ClockAttendance.validate(mesh_datum.turn_id, format_current_hour, 0)

         if entrance_status == 0:
            Alert.store(mesh_datum.rut, 1)
            Whatsapp.send(mesh_datum.rut, str(1), '', 19)
            ControlClockNoMark.store(mesh_datum.rut, 0)

      check_attendance_id = ClockAttendance.checked_attedance(mesh_datum.rut, format_current_date, 1)
      check_alert_id = Alert.check_alert(mesh_datum.rut, format_current_date, 2)

      if check_attendance_id == 1 and check_alert_id == 0:

         exit_status = ClockAttendance.validate(mesh_datum.turn_id, format_current_hour, 1)

         if exit_status == 0:
            Alert.store(mesh_datum.rut, 2)
            Whatsapp.send(mesh_datum.rut, str(1), '', 20)
            ControlClockNoMark.store(mesh_datum.rut, 1)

   return str(format_current_date)

@clock_attendance.route("/clock_attendance/alert/<int:rut>/<date>", methods=['GET'])
def alert(rut, date):
   ClockAttendance.alert_employee_about_left_hours(rut, date)

   return redirect(url_for('mesh_data.report_per_days'))

@clock_attendance.route("/clock_attendance/register/<int:rut>/<date>", methods=['GET'])
def register(rut, date):
   clock_attendances = ClockAttendance.user_registered_all_punch_hours(rut, date)

   return render_template('human_resource/mesh_data/report_mesh_data_per_days/edit_mesh_data_per_days.html', clock_attendances = clock_attendances.to_dict(orient='records'))

@clock_attendance.route("/clock_attendance/store_as_human_resource", methods=['POST'])
def store_as_human_resource():
   ClockAttendance.store_as_human_resource(request.form)

   flash('Usted le ha marcado correctamente las horas al trabajador', 'success')

   return redirect(url_for('mesh_data.report_per_days'))