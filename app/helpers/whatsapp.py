import requests
import json
from app.news.new import New
from app.dropbox_data.dropbox import Dropbox
from app.whatsapp_groups_rols.whatsapp_group_rol import WhatsappGroupRol
from app.whatsapp_templates.whatsapp_template import WhatsappTemplate
from app.employees.employee import Employee
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.documents_employees.document_employee import DocumentEmployee
from app.document_types.document_type import DocumentType
from app.supervisors.supervisor import Supervisor
from app.settings.setting import Setting

class Whatsapp:
    @staticmethod
    def send(id = '', answer = '', group_id = '', template_type_id = ''):
        settings = Setting.get()
        
        if answer == '1':
            if template_type_id == 4:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                whatsapp_groups_rols = WhatsappGroupRol.get(group_id)

                for whatsapp_group_rol in whatsapp_groups_rols:
                    employees = Employee.get_by_rol(whatsapp_group_rol.rol_id)
                    
                    new = New.get(id)

                    response = Dropbox.get('/blogs/', new.picture)

                    for employee in employees:
                        if employee['rut'] == 27141399:
                            url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                            payload = json.dumps({
                            "messaging_product": "whatsapp",
                            "to": "56" + str(employee['cellphone']),
                            "type": "template",
                            "template": {
                                "name": str(whatsapp_template.whatsapp_template),
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
                                        "link": response
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
                                        "text": "https://example.com/blog/login/token/blog_id"
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
            elif template_type_id == 13:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                document_employee = DocumentEmployee.get_by_id(id)

                document_type = DocumentType.get(document_employee.document_type_id)
                
                employee_labor_datum = EmployeeLaborDatum.get(document_employee.rut)

                supervisors = Supervisor.get(employee_labor_datum.branch_office_id)

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                for supervisor in supervisors:
                    supervisor_data = Employee.get(supervisor.rut)

                    payload = json.dumps({
                                "messaging_product": "whatsapp",
                                "to": "56" + str(supervisor_data.cellphone),
                                "type": "template",
                                "template": {
                                    "name": str(whatsapp_template.whatsapp_template),
                                    "language": {
                                    "code": "es"
                                    },
                                    "components": [
                                    {
                                        "type": "body",
                                        "parameters": [
                                        {
                                            "type": "text",
                                            "text": supervisor_data.nickname
                                        },
                                        {
                                            "type": "text",
                                            "text": document_type.document_type
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
            elif template_type_id == 14:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                document_employee = DocumentEmployee.get_by_id(id)

                document_type = DocumentType.get(document_employee.document_type_id)
                
                employee = Employee.get(document_employee.rut)

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                payload = json.dumps({
                                "messaging_product": "whatsapp",
                                "to": "56" + str(employee.cellphone),
                                "type": "template",
                                "template": {
                                    "name": str(whatsapp_template.whatsapp_template),
                                    "language": {
                                    "code": "es"
                                    },
                                    "components": [
                                    {
                                        "type": "body",
                                        "parameters": [
                                        {
                                            "type": "text",
                                            "text": employee.nickname
                                        },
                                        {
                                            "type": "text",
                                            "text": document_type.document_type
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
            elif template_type_id == 15:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                document_employee = DocumentEmployee.get_by_id(id)

                document_type = DocumentType.get(document_employee.document_type_id)
                
                employee = Employee.get(document_employee.rut)

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                payload = json.dumps({
                                "messaging_product": "whatsapp",
                                "to": "56" + str(employee.cellphone),
                                "type": "template",
                                "template": {
                                    "name": str(whatsapp_template.whatsapp_template),
                                    "language": {
                                    "code": "es"
                                    },
                                    "components": [
                                    {
                                        "type": "body",
                                        "parameters": [
                                        {
                                            "type": "text",
                                            "text": employee.nickname
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

            elif template_type_id == 16:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                document_employee = DocumentEmployee.get_by_id(id)

                document_type = DocumentType.get(document_employee.document_type_id)
                
                employee = Employee.get(document_employee.rut)

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                payload = json.dumps({
                                "messaging_product": "whatsapp",
                                "to": "56" + str(employee.cellphone),
                                "type": "template",
                                "template": {
                                    "name": str(whatsapp_template.whatsapp_template),
                                    "language": {
                                    "code": "es"
                                    },
                                    "components": [
                                    {
                                        "type": "body",
                                        "parameters": [
                                        {
                                            "type": "text",
                                            "text": employee.nickname
                                        },
                                        {
                                            "type": "text",
                                            "text": document_type.document_type
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

        return 1