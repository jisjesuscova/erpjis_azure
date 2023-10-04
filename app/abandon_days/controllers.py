from flask import Blueprint
from flask_login import login_required
from app import app, regular_employee_rol_need, db
from app.helpers.pdf import Pdf
from app.users.user import User
from werkzeug.security import generate_password_hash
import random
from app.employees.employee import Employee
from app.whatsapp_templates.whatsapp_template import WhatsappTemplate
import json
from app.settings.setting import Setting
import requests
from datetime import datetime
from app.models.models import UserModel
from app.models.models import EmployeeModel

abandon_day = Blueprint("abandon_days", __name__)

@abandon_day.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@abandon_day.route("/human_resources/abandon_day/document", methods=['GET'])
def document():
   users = User.get()

   for user in users:
      if user.password == '' or user.password == None:
         settings = Setting.get()

         employee = Employee.get(user.rut)
         password = str(random.randint(1234, 123456))
         qty = EmployeeModel.query.filter_by(rut=user.rut).count()

         edit_user = UserModel.query.filter_by(rut=user.rut).first()
         edit_user.password = generate_password_hash(str(password))
         edit_user.updated_date = datetime.now()

         db.session.add(edit_user)
         db.session.commit()




         image = 'https://jisparking.com/public/backend/img/noticia.jpeg';

         url = "https://graph.facebook.com/v16.0/101066132689690/messages"

         if qty > 0:
            payload = json.dumps({
                            "messaging_product": "whatsapp",
                            "to": "56" + str(employee.cellphone),
                            "type": "template",
                            "template": {
                                "name": "nueva_intranet_v2",
                                "language": {
                                "code": "es"
                                },
                                "components": [
                                {
                                    "type": "header",
                                    "parameters": [
                                    {
                                        "type": "image",
                                        "image": {
                                        "link": image
                                        }
                                    }
                                    ]
                                },
                                {
                                    "type": "body",
                                    "parameters": [
                                    {
                                        "type": "text",
                                        "text": employee.nickname
                                    },
                                    {
                                        "type": "text",
                                        "text": user.visual_rut
                                    },
                                    {
                                        "type": "text",
                                        "text": password
                                    }
                                    ]
                                }
                                ]
                            }
                            })
            headers = {
                                'Authorization': settings.facebook_token,
                                'Content-Type': 'application/json'
                                }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)

   return '1'