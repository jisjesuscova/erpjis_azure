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
    documentation_titles_menu = DocumentationTitle.get()

    documentations = Documentation.get('', page)

    return render_template('human_resource/documentations/documentations.html', documentation_titles_menu = documentation_titles_menu, documentations = documentations)

@documentation.route("/documentation/create", methods=['GET'])
def create():
    documentation_titles_menu = DocumentationTitle.get()

    title = 'Crear Documentación'
    module_name = 'Documentación'
    return render_template('human_resource/documentations/documentations_create.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name)

@documentation.route("/documentation/store", methods=['POST'])
def store():
    status_id = Documentation.store(request.form)

    flash("La documentación ha sido publicada con éxito.", "success")

    return redirect(url_for('documentations.index'))

@documentation.route("/documentation/show/<int:id>", methods=['GET'])
def show(id):
    documentation_titles = DocumentationTitle.get(id)

    documentation_titles_menu = DocumentationTitle.get()

    documentation = Documentation.get(id)

    description = Markup(documentation.description)

    return render_template('human_resource/documentations/documentation_show.html', description = description, documentation_titles = documentation_titles, documentation_titles_menu = documentation_titles_menu)
