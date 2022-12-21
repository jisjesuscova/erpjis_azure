from flask import Blueprint
from flask_login import login_required
from app import app, regular_employee_rol_need
from app.helpers.pdf import Pdf

abandon_day = Blueprint("abandon_days", __name__)

@abandon_day.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@abandon_day.route("/human_resources/abandon_day/document", methods=['GET'])
def document():
   data = ['Jesus', 'Cova']
   response = Pdf.create_pdf('abandon_day', data)

   return response