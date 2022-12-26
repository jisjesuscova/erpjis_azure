from flask import Blueprint, render_template, request
from flask_login import login_required
from app import app, regular_employee_rol_need
from ZK import ZK, const
import sys
import os
import json
from datetime import datetime
from app.attendances.attendance import Attendance

control_clock = Blueprint("control_clocks", __name__)

@control_clock.route("/control_clocks/store", methods=['GET', 'POST'])
def store():
   attendance = Attendance.store(request.form)

   return str(attendance)
