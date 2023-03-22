from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.kardex_data.kardex_datum import KardexDatum
from app.document_types.document_type import DocumentType
from app.dropbox_data.dropbox import Dropbox
from app.uniforms.uniform import Uniform
from app.old_uniforms.old_uniform import OldUniform
from app.helpers.helper import Helper
from app.uniform_types.uniform_type import UniformType

uniform = Blueprint("uniforms", __name__)

@uniform.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@uniform.route("/human_resources/uniform/<int:rut>", methods=['GET'])
def index(rut):
   status_id = Helper.is_active(rut)

   if status_id == 1:
      uniforms = Uniform.get(rut)

      is_active = 1
   else:
      uniforms = OldUniform.get(rut)

      is_active = 0

   uniform_button_status_id = 1

   return render_template('administrator/human_resources/uniforms/uniforms.html', uniform_button_status_id = uniform_button_status_id, uniforms = uniforms, rut = rut, is_active = is_active)

@uniform.route("/human_resources/uniform/create/<int:rut>", methods=['GET'])
@uniform.route("/human_resources/uniform/create", methods=['GET'])
def create(rut):
   uniform_types = UniformType.get()

   return render_template('administrator/human_resources/uniforms/uniforms_create.html', rut = rut, uniform_types = uniform_types)

@uniform.route("/human_resources/uniform/delete/<int:rut>/<int:id>", methods=['GET'])
@uniform.route("/human_resources/uniform/delete", methods=['GET'])
def delete(rut, id):
   Uniform.delete(id)

   flash('El registro ha sido borrado con éxito', 'success')

   return redirect(url_for('uniforms.index', rut = rut))

@uniform.route("/human_resources/uniform/store", methods=['POST'])
def store():
   status_id = Uniform.store(request.form)

   flash('El registro ha sido guardado con éxito', 'success')

   if status_id == 1:
      return '1'
   else:
      return '0'