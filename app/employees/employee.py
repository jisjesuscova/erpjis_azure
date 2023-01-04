from flask import request
from app.models.models import EmployeeModel
from app.helpers.helper import Helper
from app import db
from datetime import datetime

class Employee():
    @staticmethod
    def get(rut = ''):
        if rut == '':
            employees = EmployeeModel.query.order_by('names').all()

            return employees
        else:
            employee = EmployeeModel.query.filter_by(rut = rut).first()

            return employee

    @staticmethod
    def upload(rut, file):
        employee = EmployeeModel.query.filter_by(rut=rut).first()
        employee.picture = file
        employee.updated_date = datetime.now()

        db.session.add(employee)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def store(data):
        numeric_rut = Helper.numeric_rut(data['rut'])
        nickname = Helper.nickname(data['names'], data['father_lastname'])

        employee = EmployeeModel()
        employee.rut = numeric_rut
        employee.visual_rut = data['rut']
        employee.names = data['names']
        employee.father_lastname = data['father_lastname']
        employee.mother_lastname = data['mother_lastname']
        employee.nickname = nickname
        employee.gender_id = data['gender_id']
        employee.nationality_id = data['nationality_id']
        employee.cellphone = data['cellphone']
        employee.born_date = data['born_date']
        employee.added_date = datetime.now()

        db.session.add(employee)
        try:
            db.session.commit()

            return employee
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def update(data, id):
        numeric_rut = Helper.numeric_rut(data['rut'])
        nickname = Helper.nickname(data['names'], data['father_lastname'])

        employee = EmployeeModel.query.filter_by(rut = id).first()
        employee.rut = numeric_rut
        employee.visual_rut = data['rut']
        employee.names = data['names']
        employee.father_lastname = data['father_lastname']
        employee.mother_lastname = data['mother_lastname']
        employee.nickname = nickname
        employee.gender_id = data['gender_id']
        employee.nationality_id = data['nationality_id']
        employee.cellphone = data['cellphone']
        employee.born_date = data['born_date']
        employee.updated_date = datetime.now()

        db.session.add(employee)
        if db.session.commit():
            return employee
        else:
            return {'msg': 'Data could not be stored'}
