from flask import request
from app.models.models import SettlementDatumModel, DocumentEmployeeModel, EmployeeModel
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.employees.employee import Employee
from app import db
from datetime import datetime
from app.helpers.helper import Helper
import fitz
from PIL import Image
import os
import dropbox
from app.settings.setting import Setting

class SettlementDatum():
    @staticmethod
    def get(period = '', page=''):

        if period == '':
            settlements = SettlementDatumModel.query.paginate(page=page, per_page=20, error_out=False)
        else:
            settlements = SettlementDatumModel.query.filter_by(period=period).all()

        return settlements

    @staticmethod
    def get_by_rut(rut, page):
        settlements = SettlementDatumModel.query.filter_by(rut=rut).all()

        return settlements
    
    @staticmethod
    def count(rut, period):
        quantity = SettlementDatumModel.query.filter_by(rut=rut, period=period).count()

        return quantity

    def delete(rut, period):
        settlement_datum = SettlementDatumModel.query.filter_by(rut=rut, period=period).first()

        db.session.delete(settlement_datum)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def store(period):
        hr_employees = HrEmployeeInput.get('', period)

        for hr_employee in hr_employees:
            quantity =  SettlementDatum.count(hr_employee.rut, period)
            employee = Employee.get(hr_employee.rut)
            
            if quantity > 0:
                SettlementDatum.delete(hr_employee.rut, period)

            settlement_datum  = SettlementDatumModel()
            settlement_datum.rut = hr_employee.rut
            settlement_datum.visual_rut = employee.visual_rut
            settlement_datum.period = period
            settlement_datum.support = ''
            settlement_datum.added_date = datetime.now()
            settlement_datum.updated_date = datetime.now()

            db.session.add(settlement_datum)
            try:
                db.session.commit()

                return settlement_datum
            except Exception as e:
                return {'msg': 'Data could not be stored'}

    @staticmethod
    def download(id):
        settlement_datum = DocumentEmployeeModel.query.filter_by(id = id).first()

        support = settlement_datum.support

        word_to_find = 'signed'
        
        count = support.count(word_to_find)

        employee = EmployeeModel.query.filter_by(rut = settlement_datum.rut).first()
        
        if employee.signature != None and employee.signature != '':
            if count == 0:
                with fitz.open(os.path.join('app/static/dist/files/settlement_data/' + settlement_datum.support)) as pdf_document:
                    img_rect = fitz.Rect(300, 550, 600, 650)
                    page = pdf_document[0]

                    page.insert_image(img_rect, filename=os.path.join('app/static/dist/files/signature_data/' + employee.signature))

                    pdf_document.save(os.path.join('app/static/dist/files/settlement_data/signed_' +settlement_datum.support))

                settings = Setting.get()

                dbx = dropbox.Dropbox(settings.dropbox_token)

                with open(os.path.join('app/static/dist/files/settlement_data/signed_' +settlement_datum.support), 'rb') as f:
                    dbx.files_upload(f.read(), '/salary_settlements/signed_' +settlement_datum.support, mode=dropbox.files.WriteMode.overwrite)

                os.remove(os.path.join('app/static/dist/files/settlement_data/' + settlement_datum.support))

                settlement_datum = DocumentEmployeeModel.query.filter_by(id = id).first()
                settlement_datum.status_id = 4
                settlement_datum.support = 'signed_' + support
                db.session.add(settlement_datum)
                db.session.commit()

        return settlement_datum.support

    @staticmethod
    def upload_store(data, filename, original_name, id):
        detail = Helper.split(original_name, '_')
        settlement_datum  = SettlementDatumModel()
        settlement_datum.document_employee_id = id
        settlement_datum.rut = detail[3]
        settlement_datum.visual_rut = detail[3]
        settlement_datum.period = data['month'] +"-"+ data['year']
        settlement_datum.support = filename
        settlement_datum.added_date = datetime.now()
        settlement_datum.updated_date = datetime.now()

        db.session.add(settlement_datum)
        try:
            db.session.commit()

            return settlement_datum
        except Exception as e:
            return {'msg': 'Data could not be stored'}