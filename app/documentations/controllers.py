from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.documentations.documentation import Documentation
from markupsafe import Markup
from app.documentation_titles.documentation_title import DocumentationTitle

documentation = Blueprint("documentations", __name__)

@documentation.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@documentation.route("/documentation/<int:page>", methods=['GET'])
@documentation.route("/documentation", methods=['GET'])
def index(page=1):
    documentations = Documentation.get('', page)

    return render_template('human_resource/documentations/documentations.html', documentations = documentations)

@documentation.route("/documentation/create", methods=['GET'])
def create():
    title = 'Crear Documentación'
    module_name = 'Documentación'
    return render_template('human_resource/documentations/documentations_create.html', title = title, module_name = module_name)

@documentation.route("/documentation/store", methods=['POST'])
def store():
    status_id = Documentation.store(request.form)

    flash("La documentación ha sido publicada con éxito.", "success")

    return redirect(url_for('documentations.index'))

@documentation.route("/documentation/show/<int:id>", methods=['GET'])
def show(id):
    documentation_titles = DocumentationTitle.get(id)

    for documentation_title in documentation_titles:
        print(documentation_title.sub_titles)

    return '1'