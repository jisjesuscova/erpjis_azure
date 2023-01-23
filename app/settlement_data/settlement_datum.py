from flask import request
from app.models.models import SettlementDatumModel
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.employees.employee import Employee
from app import db
from datetime import datetime
from app.helpers.helper import Helper

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