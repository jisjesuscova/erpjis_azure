from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.end_documents.end_document import EndDocument

end_document = Blueprint("end_documents", __name__)

@end_document.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@end_document.route("/human_resources/end_document/create/<int:rut>", methods=['GET'])
def create(rut):
   indemnity_years_service = 0
   substitute_compensation = 0
      
   return render_template('administrator/human_resources/end_documents/end_document_data.html', rut = rut, indemnity_years_service = indemnity_years_service, substitute_compensation = substitute_compensation)

@end_document.route("/human_resources/end_document/store", methods=['POST'])
def store():
   return redirect(url_for('personal_data.show', rut = request.form['rut']))

@end_document.route("/human_resources/end_document/indemnity_years_service/<int:rut>", methods=['POST'])
def indemnity_years_service(rut):
   indemnity_years_service = EndDocument.indemnity_years_service(rut)
   substitute_compensation = 0

   return render_template('administrator/human_resources/end_documents/end_document_data.html', rut = rut, substitute_compensation = substitute_compensation)

@end_document.route("/human_resources/end_document/substitute_compensation/<int:rut>", methods=['POST'])
def substitute_compensation(rut):
   indemnity_years_service = EndDocument.indemnity_years_service(rut)
   substitute_compensation = 0

   return render_template('administrator/human_resources/end_documents/end_document_data.html', rut = rut, indemnity_years_service = indemnity_years_service, substitute_compensation = substitute_compensation)

@end_document.route("/human_resources/end_document/fertility_proportional", methods=['POST'])
def fertility_proportional():
   return redirect(url_for('end_documents.create', rut = request.form['rut']))