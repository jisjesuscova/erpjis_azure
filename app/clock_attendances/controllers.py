from flask import Blueprint, request, render_template, redirect, url_for, flash, session, jsonify
from app.clock_attendances.clock_attendance import ClockAttendance
from app.mesh_data.mesh_datum import MeshDatum
import pytz
import datetime
from app.alerts.alert import Alert
from app.helpers.whatsapp import Whatsapp
from app.control_clock_no_marks.control_clock_no_mark import ControlClockNoMark
from app.helpers.helper import Helper

clock_attendance = Blueprint("clock_attendances", __name__)

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

   return redirect(url_for('clock_attendances.mark', rut=request.form['rut']))

@clock_attendance.route("/clock_attendance/mark/<int:rut>", methods=['GET'])
def mark(rut):
   mark_data = ControlClockNoMark.get(rut)

   return render_template('collaborator/clocks/mark_data.html', mark_data = mark_data)

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

   return '1'