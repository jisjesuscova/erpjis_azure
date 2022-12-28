from flask import Blueprint, request
from app.clock_attendances.clock_attendance import ClockAttendance

clock_attendance = Blueprint("clock_attendances", __name__)

@clock_attendance.route("/clock_attendance/store", methods=['GET', 'POST'])
def store():
   clock_attendance = ClockAttendance.store(request.form)

   return str(clock_attendance)