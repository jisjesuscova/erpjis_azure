import requests
import json
from app.news.new import New
from app.dropbox_data.dropbox import Dropbox
from app.whatsapp_groups_rols.whatsapp_group_rol import WhatsappGroupRol
from app.whatsapp_templates.whatsapp_template import WhatsappTemplate
from app.employees.employee import Employee
from app.documents_employees.document_employee import DocumentEmployee
from app.settings.setting import Setting
from app.helpers.helper import Helper
from app.users.user import User
from app.document_types.document_type import DocumentType
from app.birthdays.birthday import Birthday
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.supervisors.supervisor import Supervisor
from app.branch_offices.branch_office import BranchOffice
from app.employee_bank_accounts.employee_bank_account import EmployeeBankAccount
import pytz
from datetime import datetime
from app.control_clock_no_marks.control_clock_no_mark import ControlClockNoMark

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

                    image = Dropbox.get('/blogs/', new.picture)

                    for employee in employees:
                        user = User.get_by_int_rut(employee['rut'])

                        url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                        payload = json.dumps({
                                "messaging_product": "whatsapp",
                                "to": "56" + str("935887241"),
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
                                            "text": "login/" + str(user.api_token)
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
            elif template_type_id == 9:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                birthday = Birthday.get(id)

                send_employee = Employee.get(birthday.send_rut)

                send_employee_labor_data = EmployeeLaborDatum.get(birthday.send_rut)

                receive_employee = Employee.get(birthday.receive_rut)

                branch_office = BranchOffice.get(send_employee_labor_data.branch_office_id)

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                payload = json.dumps({
                                "messaging_product": "whatsapp",
                                "to": "56" + str(receive_employee.cellphone),
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
                                            "text": receive_employee.nickname
                                        },
                                        {
                                            "type": "text",
                                            "text": send_employee.nickname
                                        },
                                        {
                                            "type": "text",
                                            "text": branch_office.branch_office
                                        },
                                        {
                                            "type": "text",
                                            "text": birthday.message
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
            elif template_type_id == 12:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                whatsapp_groups_rols = WhatsappGroupRol.get(group_id)

                document_employee = DocumentEmployee.get_by_id(id)

                date = Helper.split(str(document_employee.added_date), '-')

                period = str(date[1]) + "-" + str(date[0])

                employee = Employee.get(document_employee.rut)

                user = User.get_by_int_rut(document_employee.rut)

                image = 'http://jisparking.com/public/backend/img/settlement_image.jpeg';

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
                                        "text": user.nickname
                                    },
                                    {
                                        "type": "text",
                                        "text": period
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
                                        "text": "login/" + str(user.api_token)
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
            elif template_type_id == 17:
                whatsapp_template = WhatsappTemplate.get(template_type_id)

                employee = Employee.get(id)

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
            elif template_type_id == 18:
                whatsapp_template = WhatsappTemplate.get(template_type_id)
                employee_bank_account = EmployeeBankAccount.get_by_id(id)
                employee = Employee.get(employee_bank_account.rut)
                users = User.get_by_rol_id(4)

                for user in users:
                    hr_employee = Employee.get(user.rut)

                    url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                    payload = json.dumps({
                                    "messaging_product": "whatsapp",
                                    "to": "56" + "935887241",
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
                                                "text": hr_employee.nickname
                                            },
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
            elif template_type_id == 19:
                whatsapp_template = WhatsappTemplate.get(template_type_id)
                hr_employee = Employee.get(id)

                santiago_timezone = pytz.timezone('Chile/Continental')
                current_date = datetime.now(santiago_timezone).date()
                current_date = str(current_date)

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                payload = json.dumps({
                                    "messaging_product": "whatsapp",
                                    "to": "56" + "935887241",
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
                                                "text": hr_employee.nickname
                                            },
                                            {
                                                "type": "text",
                                                "text": current_date
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
            elif template_type_id == 20:
                whatsapp_template = WhatsappTemplate.get(template_type_id)
                hr_employee = Employee.get(id)

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                payload = json.dumps({
                                    "messaging_product": "whatsapp",
                                    "to": "56" + "935887241",
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
                                                "text": hr_employee.nickname
                                            },
                                            {
                                                "type": "text",
                                                "text": current_date
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
            elif template_type_id == 21:
                whatsapp_template = WhatsappTemplate.get(template_type_id)
                hr_employee = Employee.get(id)
                control_clock_no_mark = ControlClockNoMark.get_first(id)

                date = Helper.split(control_clock_no_mark.mark_date, ' ')
                date = Helper.split(date[0], '-')
                mark_date = date[2] + '-' + date[1] + '-' + date[0]

                url = "https://graph.facebook.com/v16.0/101066132689690/messages"

                payload = json.dumps({
                                    "messaging_product": "whatsapp",
                                    "to": "56" + hr_employee.cellphone,
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
                                                "text": hr_employee.nickname
                                            },
                                            {
                                                "type": "text",
                                                "text": mark_date
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