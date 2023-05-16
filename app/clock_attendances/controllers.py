from flask import Blueprint, request
from app.clock_attendances.clock_attendance import ClockAttendance
from app.mesh_data.mesh_datum import MeshDatum
import pytz
import datetime

clock_attendance = Blueprint("clock_attendances", __name__)

@clock_attendance.route("/clock_attendance/store", methods=['GET'])
def store():
   data = ClockAttendance.store(request.form)

   return str(data)

@clock_attendance.route("/clock_attendance/validate", methods=['GET'])
def validate():
   # Obtener la zona horaria de Santiago de Chile
   santiago_timezone = pytz.timezone('Chile/Continental')

   # Obtener la fecha y hora actual en Santiago de Chile
   fecha_actual = datetime.datetime.now(santiago_timezone)

   # Imprimir la fecha y hora actual en Santiago de Chile
   print("Fecha y hora actual en Santiago de Chile:", fecha_actual)

   return str(fecha_actual)