from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.audits.audit import Audit
from app.family_core_data.family_core_datum import FamilyCoreDatum
from app.genders.gender import Gender
from app.family_types.family_type import FamilyType
from datetime import datetime
from app.dropbox_data.dropbox import Dropbox

end_document = Blueprint("end_documents", __name__)

@end_document.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@end_document.route("/human_resources/end_document/<int:rut>", methods=['GET'])
@end_document.route("/end_docucment/end_document", methods=['GET'])
def create(rut):

    return render_template('administrator/human_resources/end_documents/end_document_data.html', rut = rut)