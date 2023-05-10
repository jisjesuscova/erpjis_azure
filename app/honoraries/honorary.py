from app.models.models import SupervisorModel, HonoraryModel, BankModel, BranchOfficeModel, RegionModel, CommunesModel, EmployeeModel, HonoraryReasonModel
from app.helpers.helper import Helper
from flask_login import current_user
from app import db
from datetime import datetime, date, timedelta
from sqlalchemy import func
import requests
import json
from app.communes.commune import Commune
from app.hr_settings.hr_setting import HrSetting
from os import sys
from libredte.sdk import LibreDTE
from app.branch_offices.branch_office import BranchOffice

class Honorary():
    @staticmethod
    def get(id, page):
        if id != '':
            honorary = HonoraryModel.query.filter_by(id = id).first()
        
            return honorary
        else:
            if current_user.rol_id == 4:
                honoraries = HonoraryModel.query\
                    .join(BankModel, BankModel.id == HonoraryModel.bank_id)\
                    .join(BranchOfficeModel, BranchOfficeModel.id == HonoraryModel.branch_office_id)\
                    .join(RegionModel, RegionModel.id == HonoraryModel.region_id)\
                    .join(CommunesModel, CommunesModel.id == HonoraryModel.commune_id)\
                    .join(EmployeeModel, EmployeeModel.rut == HonoraryModel.requested_by)\
                    .join(HonoraryReasonModel, HonoraryReasonModel.id == HonoraryModel.reason_id)\
                    .add_columns(HonoraryModel.status_id, HonoraryModel.id, HonoraryModel.rut, HonoraryModel.full_name, EmployeeModel.nickname, HonoraryReasonModel.reason, HonoraryModel.added_date).order_by(HonoraryModel.added_date.desc()).paginate(page=page, per_page=10, error_out=False)
            else:
                honoraries = HonoraryModel.query\
                    .join(BankModel, BankModel.id == HonoraryModel.bank_id)\
                    .join(BranchOfficeModel, BranchOfficeModel.id == HonoraryModel.branch_office_id)\
                    .join(RegionModel, RegionModel.id == HonoraryModel.region_id)\
                    .join(CommunesModel, CommunesModel.id == HonoraryModel.commune_id)\
                    .join(EmployeeModel, EmployeeModel.rut == HonoraryModel.requested_by)\
                    .join(HonoraryReasonModel, HonoraryReasonModel.id == HonoraryModel.reason_id)\
                    .join(SupervisorModel, SupervisorModel.branch_office_id == BranchOfficeModel.id)\
                    .filter(SupervisorModel.rut == current_user.rut)\
                    .add_columns(HonoraryModel.status_id, HonoraryModel.id, HonoraryModel.rut, HonoraryModel.full_name, EmployeeModel.nickname, HonoraryReasonModel.reason, HonoraryModel.added_date).order_by(HonoraryModel.added_date.desc()).paginate(page=page, per_page=50, error_out=False)
            
            return honoraries
        
    @staticmethod
    def accountability(honorary):
        gross_amount = Helper.get_honorary_net_value(honorary.amount)
        tax = Helper.get_honorary_tax_value(honorary.amount)
        date = Helper.split(str(honorary.added_date), " ")
        asset_name_date = Helper.asset_name_date(date[0])
        asset_date = Helper.asset_date(date[0])

        branch_office = BranchOffice.get(honorary.branch_office_id)
        accounting_asset_name = str(branch_office.branch_office) + "_443000344_" + str(asset_name_date) + "_Honorario_" + str(honorary.id)
        
        # datos a utilizar
        url = 'https://libredte.cl'
        hash = 'JXou3uyrc7sNnP2ewOCX38tWZ6BTm4D1'
        creator = '76063822-6';

        if honorary.foreigner_id == 1:
            data = {
                'fecha': asset_date,
                'glosa': accounting_asset_name,
                'detalle': {
                    'debe': {
                        111000102: gross_amount,
                    },
                    'haber': {
                        443000344: honorary.amount,
                        221000223: tax,
                    },
                },
                'operacion': 'E',
                'documentos': {
                    'emitidos': [
                        {
                            'dte': '',
                            'folio': '',
                        },
                    ],
                },
            }
        else:
            data = {
                'fecha': asset_date,
                'glosa': accounting_asset_name,
                'detalle': {
                    'debe': {
                        111000102: honorary.amount
                    },
                    'haber': {
                        443000344: honorary.amount
                    },
                },
                'operacion': 'E',
                'documentos': {
                    'emitidos': [
                        {
                            'dte': '',
                            'folio': '',
                        },
                    ],
                },
            }

        Cliente = LibreDTE(hash, url)

        # crear DTE temporal
        create_asset = Cliente.post('/lce/lce_asientos/crear/' + creator, data)
        if create_asset.status_code!=200 :
            print(create_asset.json())
        else:
            Honorary.update_accountability_honorary_status(honorary.id)

        return 1

    @staticmethod
    def current_get(page):
        # Obtener la fecha actual y restarle un mes
        one_month_ago = date.today().replace(day=1) - timedelta(days=1)
        one_month_ago_str = one_month_ago.strftime('%Y-%m')  # Formatear a 'YYYY-mm'

        # Filtrar la consulta para que solo devuelva resultados con fechas dentro del mes anterior
        honoraries = HonoraryModel.query\
            .join(BankModel, BankModel.id == HonoraryModel.bank_id)\
            .join(BranchOfficeModel, BranchOfficeModel.id == HonoraryModel.branch_office_id)\
            .join(RegionModel, RegionModel.id == HonoraryModel.region_id)\
            .join(CommunesModel, CommunesModel.id == HonoraryModel.commune_id)\
            .join(EmployeeModel, EmployeeModel.rut == HonoraryModel.requested_by)\
            .join(HonoraryReasonModel, HonoraryReasonModel.id == HonoraryModel.reason_id)\
            .filter(HonoraryModel.status_id == 2)\
            .filter(HonoraryModel.accountability_status_id == 0)\
            .filter(func.DATE_FORMAT(HonoraryModel.added_date, '%Y-%m') == one_month_ago_str)\
            .add_columns(HonoraryModel.accountability_status_id, HonoraryModel.status_id, HonoraryModel.id, HonoraryModel.rut, HonoraryModel.full_name, EmployeeModel.nickname, HonoraryReasonModel.reason, HonoraryModel.added_date)\
            .order_by(HonoraryModel.added_date.desc())\
            .paginate(page=page, per_page=10, error_out=False)
        
        return honoraries

    @staticmethod
    def store(data):
        if data['employee_to_replace'] == '':
            employee_to_replace = 0
        else:
            employee_to_replace = data['employee_to_replace']

        honorary = HonoraryModel()
        honorary.reason_id = data['reason_id']
        honorary.branch_office_id = data['branch_office_id']
        honorary.foreigner_id = data['foreigner_id']
        honorary.bank_id = data['bank_id']
        honorary.schedule_id = data['schedule_id']
        honorary.region_id = data['region_id']
        honorary.commune_id = data['commune_id']
        honorary.status_id = 1
        honorary.accountability_status_id = 0
        honorary.requested_by = current_user.rut
        honorary.employee_to_replace = employee_to_replace
        honorary.rut = data['rut']
        honorary.full_name = data['full_name']
        honorary.email = data['email']
        honorary.address = data['address']
        honorary.account_number = data['account_number']
        honorary.start_date = data['start_date']
        honorary.end_date = data['end_date']
        honorary.account_number = data['account_number']
        honorary.observation = data['observation']
        honorary.added_date = datetime.now()
        honorary.updated_date = datetime.now()

        db.session.add(honorary)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0
    
    @staticmethod
    def send(data):
        hr_settings = HrSetting.get()

        commune = Commune.get(data['commune_id'])
        current_date = Helper.get_time_Y_m_d()
        
        amount = Helper.remove_from_string('.', data['amount'])
        amount = round(int(amount) / float(hr_settings.percentage_honorary_bill))

        url = "https://apigateway.cl/api/v1/sii/bte/emitidas/emitir"

        payload = json.dumps({
                                "auth": {
                                    "pass": {
                                    "rut": "76063822-6",
                                    "clave": "JYM1"
                                    }
                                },
                                "boleta": {
                                    
                                    "Encabezado": {
                                        "IdDoc": {
                                            "FchEmis": current_date
                                        },
                                        "Emisor": {
                                            "RUTEmisor": '76063822-6'
                                        },
                                        "Receptor": {
                                            "RUTRecep": data['rut'],
                                            "RznSocRecep": data['full_name'],
                                            "DirRecep": data['address'],
                                            "CmnaRecep": commune.commune
                                        }
                                    },
                                    "Detalle": [
                                        {
                                            "NmbItem": 'Boleta de Honorarios para ' + data['full_name'],
                                            "MontoItem": amount
                                        }
                                    ]
                                }
                            })
        
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYWIyYWUwOGVmYjI1Y2MwMWU5ODUzOWViMDRhNjJkYzEzN2UxMDQyODRmNjY5MTNjMTAxMWM3Yzg1N2Q0NmZmNzY1NGM4NGQzYzM0YzRhMTAiLCJpYXQiOjE2NDk1Mjg4ODMsIm5iZiI6MTY0OTUyODg4MywiZXhwIjo0ODA1MjAyNDgzLCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.K03TeHk5geCY4NARl9UiV8SeeR6Pe4YT1E_Z_z5VLhTJwI36_780NiwxlBIE58hlX9XdjBZiVgpW3FSEYvGQo-6pv6tp9r6Yh9LB6Hi1j5YirwWQgOgPE_2kXBjtXVS84r97unEhpCGA0mGpbIJH0YNNFLYgZauoLzGjmooOYbAT6buhOG5_xTX25VhgscoaPeh_-KnbJVxpMf0YxMkDC7nE5VsI8mMloR3pOyfXpLUH5f3yjl2F8QNPtjRB25MJZnhetMozPUoDX8h5Lh5gcbYItQYtzZrU-3Cs8JMG7bu3fH74a5bej_HmLfdAP-3HP0CxOOhAY4Oppamf8zGwkvzPSeXZdPW79pZ9JEkfRFOfwuYbJA79-nawo_UiKc73HIHgGMFoR9wvfla5JDKrzTh3xoa2JsZUbMZ93iYqsurVMJt-suaqM1Lqcqa1nGZ8HovGgYeVf6RbQH1TJT-ckeGwgfor0Pi_vhhUc9Coxd9qQOAyiY_jHUVy16CQ4BlFkgsOQ9mwBuL5k4xHwNd3VBa_ktLeW36rrXSsaGXwoVLO9Bi19_-fijvrNRmAez3NTiODrMLNNLqXIk9MbUy0PWYAV1Ylq_gdJhJXEED0_iTe6MwA_OrAwVN18U0DQopKwIDLqQoRTAPlcWR1PEO5sBs3jHFclc_BaoHqfG5_W2U',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        return 1

    @staticmethod
    def update_accountability_honorary_status(id):

        honorary = HonoraryModel.query.filter_by(id=id).first() 
        honorary.accountability_status_id = 1

        db.session.add(honorary)

        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def update(data, id):
        if data['employee_to_replace'] == '':
            employee_to_replace = 0
        else:
            employee_to_replace = data['employee_to_replace']

        if data['foreigner_id'] == '1':
            Honorary.send(data)

        honorary = HonoraryModel.query.filter_by(id=id).first()
        honorary.reason_id = data['reason_id']
        honorary.branch_office_id = data['branch_office_id']
        honorary.foreigner_id = data['foreigner_id']
        honorary.bank_id = data['bank_id']
        honorary.schedule_id = data['schedule_id']
        honorary.region_id = data['region_id']
        honorary.commune_id = data['commune_id']
        honorary.status_id = 2
        honorary.employee_to_replace = employee_to_replace
        honorary.rut = data['rut']
        honorary.full_name = data['full_name']
        honorary.email = data['email']
        honorary.address = data['address']
        honorary.account_number = data['account_number']
        honorary.start_date = data['start_date']
        honorary.end_date = data['end_date']
        honorary.account_number = data['account_number']
        honorary.observation = data['observation']
        honorary.amount = Helper.remove_from_string('.', data['amount'])
        honorary.updated_date = datetime.now()

        db.session.add(honorary)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def delete(id):
        honorary = HonoraryModel.query.filter_by(id=id).first()

        db.session.delete(honorary)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0