from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.documentations.documentation import Documentation
from markupsafe import Markup
from app.documentation_titles.documentation_title import DocumentationTitle
from app.documentation_sub_titles.documentation_sub_title import DocumentationSubTitle

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

    documentations = Documentation.get(current_user.rut, '', page)

    if current_user.rol_id == 4:
        return render_template('human_resource/documentations/documentations.html', documentation_titles_menu = documentation_titles_menu, documentations = documentations)
    elif current_user.rol_id == 5:
        return render_template('designer/documentations/documentations.html', documentation_titles_menu = documentation_titles_menu, documentations = documentations)
    elif current_user.rol_id == 6:
        return render_template('management/documentations/documentations.html', documentation_titles_menu = documentation_titles_menu, documentations = documentations)

@documentation.route("/documentation/create", methods=['GET'])
def create():
    documentation_titles_menu = DocumentationTitle.get()

    title = 'Crear Documentación'
    module_name = 'Documentación'
    
    if current_user.rol_id == 4:
        return render_template('human_resource/documentations/documentations_create.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name)
    elif current_user.rol_id == 5:
        return render_template('designer/documentations/documentations_create.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name)
    elif current_user.rol_id == 6:
        return render_template('management/documentations/documentations_create.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name)

@documentation.route("/documentation/store", methods=['POST'])
def store():
    status_id = Documentation.store(request.form)

    flash("La documentación ha sido publicada con éxito.", "success")

    return redirect(url_for('documentations.index'))

@documentation.route("/documentation/update/<int:id>", methods=['POST'])
def update(id):
    status_id = Documentation.update(id, request.form)

    flash("La documentación ha sido actualizada con éxito.", "success")

    return redirect(url_for('documentations.index'))

@documentation.route("/documentation/delete/<int:id>", methods=['GET'])
def delete(id):
    Documentation.delete(id)
    DocumentationTitle.delete(id)
    DocumentationSubTitle.delete(id)

    flash("La documentación ha sido borrada con éxito.", "success")

    return redirect(url_for('documentations.index'))

@documentation.route("/documentation/show/<int:id>", methods=['GET'])
def show(id):
    documentation_titles = DocumentationTitle.get(id)

    documentation_titles_menu = DocumentationTitle.get()

    documentation = Documentation.get('', id, '')

    description = Markup(documentation.markdown_description)

    if current_user.rol_id == 1:
        return render_template('collaborator/documentations/documentation_show.html', description = description, documentation_titles = documentation_titles, documentation_titles_menu = documentation_titles_menu)
    elif current_user.rol_id == 2:
        return render_template('incharge/documentations/documentation_show.html', description = description, documentation_titles = documentation_titles, documentation_titles_menu = documentation_titles_menu)
    elif current_user.rol_id == 3:
        return render_template('supervisor/documentations/documentation_show.html', description = description, documentation_titles = documentation_titles, documentation_titles_menu = documentation_titles_menu)
    elif current_user.rol_id == 4:
        return render_template('human_resource/documentations/documentation_show.html', description = description, documentation_titles = documentation_titles, documentation_titles_menu = documentation_titles_menu)
    elif current_user.rol_id == 5:
        return render_template('designer/documentations/documentation_show.html', description = description, documentation_titles = documentation_titles, documentation_titles_menu = documentation_titles_menu)
    elif current_user.rol_id == 6:
        return render_template('management/documentations/documentation_show.html', description = description, documentation_titles = documentation_titles, documentation_titles_menu = documentation_titles_menu)
    
@documentation.route("/documentation/edit/<int:id>", methods=['GET'])
def edit(id):
    documentation_titles_menu = DocumentationTitle.get()

    documentation = Documentation.get('', id, '')

    title = 'Editar Documentación'
    module_name = 'Documentación'

    if current_user.rol_id == 4:
        return render_template('human_resource/documentations/documentations_edit.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, documentation = documentation)
    elif current_user.rol_id == 5:
        return render_template('designer/documentations/documentations_edit.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, documentation = documentation)
    elif current_user.rol_id == 6:
        return render_template('management/documentations/documentations_edit.html', documentation_titles_menu = documentation_titles_menu, title = title, module_name = module_name, documentation = documentation)