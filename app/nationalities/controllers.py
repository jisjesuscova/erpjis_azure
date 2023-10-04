from flask import Blueprint, render_template
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.models.models import NationalityModel

nationality = Blueprint("nationalities", __name__)

@nationality.before_request
def constructor():
   pass

@nationality.route("/master_data/nationalities", methods=['GET'])
def index():
   return 