from flask import Blueprint, request
from app.clock_attendances.clock_attendance import ClockAttendance

clock_attendance = Blueprint("clock_attendances", __name__)

@clock_attendance.route("/clock_attendance/store", methods=['GET'])
def store():

   return str(request.form)