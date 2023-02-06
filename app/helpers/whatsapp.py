from app.models.models import WhatsappTemplateModel, EmployeeModel, UserModel
import requests
import os
import json
from app.news.new import New

class Whatsapp:
    @staticmethod
    def send(id, answer, template_type_id):
        if answer == '1':
            if template_type_id == 4:
                whatsapp_template = WhatsappTemplateModel.query.filter_by(id=template_type_id).first()

                employees = EmployeeModel.query\
                        .join(UserModel, UserModel.rut == EmployeeModel.rut)\
                        .add_columns(UserModel.nickname, EmployeeModel.cellphone, EmployeeModel.rut, UserModel.api_token).all()

                new = New.get(id)

                url = 'https://graph.facebook.com/v15.0/101066132689690/messages'
                headers = {
                    'Authorization': 'Bearer EAAFYECjSEkQBAJ20serunJpO0pdq9ZAvVpWJREZCfVSm7cXH8ni1U0SbTzuDLV674xrQqSH6p4PzluutK31Uu0jj9NQM8NIfaRoAhZA0eCFRdBFnwpjFJYnrVR0ZCS9eCFFVeEJQB7QvxypwGoxZAATLYCG7qJOfJDFyeSPliwklKYesVX7ZCj',
                    'Content-Type': 'application/json'
                }

                for employee in employees:
                    if employee['rut'] == 27141399:
                        data = {
                            "messaging_product": "whatsapp",
                            "to": '56' + str(employee['cellphone']),
                            "type": "template",
                            "template": {
                                "name": whatsapp_template.whatsapp_template,
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
                                                    "link": 'https://www.dropbox.com/s/5pz1j4jxoegtni2/4146229493615906_nueva_noticia_5_02_2023.jpg?dl=0'
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "type": "body",
                                        "parameters": [
                                            {
                                                "type": "text",
                                                "text": employee['nickname']
                                            },
                                            {
                                                "type": "text",
                                                "text": new.title
                                            }
                                        ]
                                    },
                                    {
                                        "type": "button",
                                        "index": "0",
                                        "sub_type": "url",
                                        "parameters": [
                                            {
                                                "type": "text",
                                                "text": f"blog/login/{employee['api_token']}/{employee['rut']}"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                        
                        response = requests.post(url, headers=headers, data=json.dumps(data))

                        print(response)
        return 1