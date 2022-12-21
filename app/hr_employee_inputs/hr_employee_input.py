from flask import request
from app.models.models import HrEmployeeInputModel, EmployeeLaborDatumModel, EmployeeModel, HrInputDescriptionModel, HrEmployeeDayModel
from app.hr_employee_labor_fields.hr_employee_labor_field import HrEmployeeLaborField
from app.helpers.helper import Helper
from app.hr_input_descriptions.hr_input_description import HrInputDescription
from app.hr_employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.employees.employee import Employee
from app import db
from sqlalchemy.sql import text
from sqlalchemy import engine, func, select
from datetime import datetime
from num2words import num2words

class HrEmployeeInput():
    def update_employee_input_with_days(rut = '', period = '', code = '', value = ''):
        HrEmployeeInput.delete(rut, period, 52)

        employee_labor_datum = EmployeeLaborDatum.get(rut)

        HrEmployeeInput.simple_store(rut, period, employee_labor_datum.branch_office_id, code, value)

    def get(rut = '', period = ''):
        if rut == '':
            hr_employees = HrEmployeeInputModel.query\
                .join(EmployeeModel, EmployeeModel.rut == HrEmployeeInputModel.rut)\
                .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == HrEmployeeInputModel.rut)\
                .add_columns(EmployeeLaborDatumModel.branch_office_id, EmployeeModel.rut, EmployeeModel.names, EmployeeModel.father_lastname)\
                .filter(HrEmployeeInputModel.period==period)\
                .group_by('rut')\
                .all()

            return hr_employees
        else:
            hr_employees = HrEmployeeInputModel.query\
                .join(EmployeeModel, EmployeeModel.rut == HrEmployeeInputModel.rut)\
                .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == HrEmployeeInputModel.rut)\
                .add_columns(EmployeeLaborDatumModel.branch_office_id, EmployeeModel.rut, EmployeeModel.names, EmployeeModel.father_lastname, HrEmployeeInputModel.value, HrEmployeeInputModel.hr_input_description_id)\
                .filter(HrEmployeeInputModel.period==period, HrEmployeeInputModel.rut==rut)\
                .all()

            return hr_employees

    def get_settlement_value(rut = '', period = '', id = ''):
        hr_employee_input = HrEmployeeInputModel.query.filter_by(rut=rut, period=period, hr_input_description_id=id).first()
        hr_employee_input_quantity = HrEmployeeInputModel.query.filter_by(rut=rut, period=period, hr_input_description_id=id).count()

        if hr_employee_input_quantity > 0:
            return hr_employee_input.value
        else:
            return 0

    def delete(rut = '', period = '', hr_input_description_id = ''):
        hr_employee_input = HrEmployeeInputModel.query.filter_by(rut=rut, period=period, hr_input_description_id=hr_input_description_id).first()
        hr_employee_input_quantity = HrEmployeeInputModel.query.filter_by(rut=rut, period=period, hr_input_description_id=hr_input_description_id).count()
        
        if hr_employee_input_quantity > 0:
            db.session.delete(hr_employee_input)
            db.session.commit()

    def get_with(rut = '', period = '', hr_input_description_id = ''):
        hr_employee_input = HrEmployeeInputModel.query.filter_by(rut=rut, period=period, hr_input_description_id=hr_input_description_id).first()

        return hr_employee_input.value

    def get_with_sum(rut = '', period = '', group_id = ''):
        data = (db.session.query(HrEmployeeInputModel.id, func.sum(HrEmployeeInputModel.value).label("total"))
        .join(HrInputDescriptionModel, HrInputDescriptionModel.id == HrEmployeeInputModel.hr_input_description_id).filter(HrInputDescriptionModel.group_id==group_id, HrEmployeeInputModel.period==period).first())

        return data.total


    @staticmethod
    def open(data):
        HrEmployeeInput.value(data)
            
    def value(data):
        hr_employee_labor_fields = HrEmployeeLaborField.get(1)

        for hr_employee_labor_field in hr_employee_labor_fields:
            field = hr_employee_labor_field.field
    
            employee_labor_data = EmployeeLaborDatumModel.query\
            .add_columns(text('rut'), text('branch_office_id'), text(field))\
            .group_by('rut')\
            .all()

            for employee_labor_datum in employee_labor_data:
                    
                period = Helper.period(data['month'], data['year'])

                hr_employee_input = HrEmployeeInputModel()
                hr_employee_input.rut = employee_labor_datum[1]
                hr_employee_input.period = period
                hr_employee_input.branch_office_id = employee_labor_datum[2]
                hr_employee_input.hr_input_description_id = hr_employee_labor_field.hr_input_description_id
                hr_employee_input.value = employee_labor_datum[3]
                hr_employee_input.added_date = datetime.now()
                hr_employee_input.updated_date = datetime.now()

                db.session.add(hr_employee_input)
                db.session.commit()

    def false_store(data, period):
        employee_labor_data = EmployeeLaborDatumModel.query.all()

        for employee_labor_datum in employee_labor_data:
            hr_employee_input = HrEmployeeInputModel()
            hr_employee_input.rut = employee_labor_datum.rut
            hr_employee_input.period = period
            hr_employee_input.branch_office_id = employee_labor_datum.branch_office_id
            hr_employee_input.hr_input_description_id = data['hr_input_description_id']
            hr_employee_input.value = 0
            hr_employee_input.added_date = datetime.now()
            hr_employee_input.updated_date = datetime.now()

            db.session.add(hr_employee_input)
            db.session.commit()

    @staticmethod
    def simple_store(rut, period, branch_office_id, hr_input_description_id, value):
        hr_employee_input = HrEmployeeInputModel()
        hr_employee_input.rut = rut
        hr_employee_input.period = period
        hr_employee_input.branch_office_id = branch_office_id
        hr_employee_input.hr_input_description_id = hr_input_description_id
        hr_employee_input.value = value
        hr_employee_input.added_date = datetime.now()
        hr_employee_input.updated_date = datetime.now()

        db.session.add(hr_employee_input)
        db.session.commit()

    def store(data, period):
        value = request.form.getlist('value')
        rut = request.form.getlist('rut')
        branch_office_id = request.form.getlist('branch_office_id')

        for i in range(len(value)):
            hr_employee_input = HrEmployeeInputModel()
            hr_employee_input.rut = rut[i]
            hr_employee_input.period = period
            hr_employee_input.branch_office_id = branch_office_id[i]
            hr_employee_input.hr_input_description_id = data['hr_input_description_id']
            hr_employee_input.value = value[i]
            hr_employee_input.added_date = datetime.now()
            hr_employee_input.updated_date = datetime.now()

            db.session.add(hr_employee_input)
            db.session.commit()

    @staticmethod
    def calculation_store(rut, period, branch_office_id, hr_input_description_id, value):
        hr_employee_input = HrEmployeeInputModel()
        hr_employee_input.rut = rut
        hr_employee_input.period = period
        hr_employee_input.branch_office_id = branch_office_id
        hr_employee_input.hr_input_description_id = hr_input_description_id
        hr_employee_input.value = value
        hr_employee_input.added_date = datetime.now()
        hr_employee_input.updated_date = datetime.now()

        db.session.add(hr_employee_input)
        db.session.commit()

    @staticmethod
    def massive_store(rut, value, branch_office_id, hr_input_description_id, period):
        hr_employee_input = HrEmployeeInputModel.query.filter_by(rut=rut, period=period, hr_input_description_id=hr_input_description_id).first()
        hr_employee_input.rut = rut
        hr_employee_input.period = period
        hr_employee_input.branch_office_id = branch_office_id
        hr_employee_input.hr_input_description_id = hr_input_description_id
        hr_employee_input.value = value
        hr_employee_input.added_date = datetime.now()
        hr_employee_input.updated_date = datetime.now()

        db.session.add(hr_employee_input)
        db.session.commit()

    def store_input_days(period):
        hr_employee_labor_fields = HrEmployeeLaborField.get(2)

        for hr_employee_labor_field in hr_employee_labor_fields:
            field = hr_employee_labor_field.field
        
            hr_employee_days = HrEmployeeDayModel.query\
                            .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == HrEmployeeDayModel.rut)\
                            .add_columns(EmployeeLaborDatumModel.rut, EmployeeLaborDatumModel.branch_office_id, text(field))\
                            .filter(period==period)\
                            .all()
           
            for hr_employee_day in hr_employee_days:
                hr_employee_input = HrEmployeeInputModel()
                hr_employee_input.rut = hr_employee_day[1]
                hr_employee_input.period = period
                hr_employee_input.branch_office_id = hr_employee_day[2]
                hr_employee_input.hr_input_description_id = hr_employee_labor_field.hr_input_description_id
                hr_employee_input.value = hr_employee_day[3]
                hr_employee_input.added_date = datetime.now()
                hr_employee_input.updated_date = datetime.now()

                db.session.add(hr_employee_input)
                db.session.commit()
    
    def header_settlement(rut, period):
        hr_employee_input_data = HrEmployeeInput.get(rut, period)

        hr_employee_labor_datum = EmployeeLaborDatum.get(rut)
        employee = Employee.get(rut)
    
        data = [
                'Jis Parking SpA', 
                '76.063.822-9', 
                period, 
                'Matucana 40', 
                employee.names, 
                hr_employee_labor_datum.entrance_company,
                employee.visual_rut,
                '',
                hr_employee_labor_datum.job_position_id,
                hr_employee_labor_datum.contract_type_id,
                hr_employee_labor_datum.branch_office_id
                ]

        hr_input_description_data = HrInputDescription.get_position(1)

        for hr_input_description_datum in hr_input_description_data:
            position = hr_input_description_datum.header_position

            value = HrEmployeeInput.get_settlement_value(rut, period, hr_input_description_datum.id)

            value = Helper.convert_to_thousands(value)
            
            Helper.convert_to_array(data, value, position)

        return data

    def positive_settlement(rut, period):
        data = []

        hr_input_description_data = HrInputDescription.get_position(2)

        for hr_input_description_datum in hr_input_description_data:
            position = hr_input_description_datum.positive_position

            value = HrEmployeeInput.get_settlement_value(rut, period, hr_input_description_datum.id)

            if value != 0:
                value = Helper.convert_to_thousands(value)

            Helper.convert_to_array(data, value, position)

        data = [i for i in data if i != 0]

        return data

    def settlement_positive_name(rut, period):
        data = []

        hr_input_description_data = HrInputDescription.get_position(2)

        for hr_input_description_datum in hr_input_description_data:
            position = hr_input_description_datum.positive_position

            value = HrEmployeeInput.get_settlement_value(rut, period, hr_input_description_datum.id)

            if value > 0:
                Helper.convert_to_array(data, hr_input_description_datum.settlement_name, position)
            else:
                Helper.convert_to_array(data, 0, position)

        data = [i for i in data if i != 0]

        return data

    def negative_settlement(rut, period):
        data = []

        hr_input_description_data = HrInputDescription.get_position(3)

        for hr_input_description_datum in hr_input_description_data:
            position = hr_input_description_datum.negative_position

            value = HrEmployeeInput.get_settlement_value(rut, period, hr_input_description_datum.id)
            
            if value != 0:
                value = Helper.convert_to_thousands(value)

            Helper.convert_to_array(data, value, position)

        data = [i for i in data if i != 0]

        return data

    def settlement_negative_name(rut, period):
        data = []

        hr_input_description_data = HrInputDescription.get_position(3)

        for hr_input_description_datum in hr_input_description_data:
            position = hr_input_description_datum.negative_position

            value = HrEmployeeInput.get_settlement_value(rut, period, hr_input_description_datum.id)

            if value > 0:
                Helper.convert_to_array(data, hr_input_description_datum.settlement_name, position)
            else:
                Helper.convert_to_array(data, 0, position)

        data = [i for i in data if i != 0]

        return data

    def total_settlement(data):
        value = []
        for i in range(len(data)):
            total_status = HrInputDescription.check_if_total(data[i])
            if total_status == 1:
                Helper.convert_to_array(value, 1, i)
            else:
                Helper.convert_to_array(value, 0, i)

        return value

    
    def total_values(rut, period):
        data = []

        value = HrEmployeeInput.get_with(rut, period, 66)
        value = Helper.convert_to_thousands(value)
        Helper.convert_to_array(data, value, 0)
        value = HrEmployeeInput.get_with(rut, period, 67)
        value = Helper.convert_to_thousands(value)
        Helper.convert_to_array(data, value, 1)
        value = HrEmployeeInput.get_with(rut, period, 51)
        value = Helper.convert_to_thousands(value)
        Helper.convert_to_array(data, value, 2)
        value = HrEmployeeInput.get_with(rut, period, 51)
        value = num2words(value, lang='es')
        Helper.convert_to_array(data, value, 3)

        return data