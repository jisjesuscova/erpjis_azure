from flask import Blueprint, render_template
from flask_login import login_required
from app import app, regular_employee_rol_need

home = Blueprint("home", __name__)

@home.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@home.route("/home", methods=['GET'])
def index():
   return render_template('home/index.html')