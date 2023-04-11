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

@documentation.route("/documentation/<int:page>", methods=['GET'])
@documentation.route("/documentation", methods=['GET'])
def index(page=1):
    documentations = Documentation.get(page)

    return render_template('administrator/documentations/documentations.html', documentations = documentations)

@documentation.route("/documentation/create", methods=['GET'])
def create():
    return render_template('administrator/documentations/documentations_create.html')

@documentation.route("/documentation/create", methods=['POST'])
def store():
    return '1'