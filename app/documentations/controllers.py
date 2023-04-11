from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.documentations.documentation import Documentation

documentation = Blueprint("documentations", __name__)

@documentation.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@documentation.route("/documentation", methods=['GET'])
def index():
    documentations = Documentation.get()

    return render_template('administrator/documentations/index.html')