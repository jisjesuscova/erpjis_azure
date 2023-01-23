from flask import request
from app.models.models import EmployeeModel, EmployeeLaborDatumModel, OldEmployeeModel, OldEmployeeLaborDatumModel
from app.helpers.helper import Helper
from app import db
from datetime import datetime

class Employee():
    @staticmethod
    def get(rut = '', page = ''):
        if page != '':
            employees = EmployeeModel.query.order_by('rut').paginate(page=page, per_page=20, error_out=False)

            return employees
        else:
            if rut == '':
                employees = EmployeeModel.query.order_by('rut').all()

                return employees
            else:
                employee = EmployeeModel.query.filter_by(rut = rut).first()

                return employee


    @staticmethod
    def search(data, page = ''):
        if len(data) > 0:
            search_rut = data['rut']
            search_names = data['names']
            search_father_lastname = data['father_lastname']
            search_mother_lastname = data['mother_lastname']
            search_status_id = data['status_id']
            search_branch_office_id = data['branch_office_id']

        if search_status_id == '2':
            query = OldEmployeeModel.query\
                        .join(OldEmployeeLaborDatumModel, OldEmployeeLaborDatumModel.rut == OldEmployeeModel.rut)\
                        .add_columns(OldEmployeeModel.id, OldEmployeeModel.rut, OldEmployeeModel.visual_rut, OldEmployeeModel.nickname).order_by('rut')

            query = query.filter(OldEmployeeLaborDatumModel.status_id.like(f"%{search_status_id}%"))

            if len(data) > 0:
                if search_rut:
                    query = query.filter(OldEmployeeModel.visual_rut.like(f"%{search_rut}%"))
                if search_names:
                    query = query.filter(OldEmployeeModel.nickname.like(f"%{search_names}%"))
                if search_father_lastname:
                    query = query.filter(OldEmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                if search_mother_lastname:
                    query = query.filter(OldEmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                if search_branch_office_id:
                    query = query.filter(OldEmployeeLaborDatumModel.branch_office_id == search_branch_office_id)
            
            employees = query.paginate(page=page, per_page=20, error_out=False)
        elif search_status_id == '3':
            query = OldEmployeeModel.query\
                        .join(OldEmployeeLaborDatumModel, OldEmployeeLaborDatumModel.rut == OldEmployeeModel.rut)\
                        .add_columns(OldEmployeeModel.id, OldEmployeeModel.rut, OldEmployeeModel.visual_rut, OldEmployeeModel.nickname).order_by('rut')

            query = query.filter(OldEmployeeLaborDatumModel.status_id.like(f"%{search_status_id}%"))

            if len(data) > 0:
                if search_rut:
                    query = query.filter(OldEmployeeModel.visual_rut.like(f"%{search_rut}%"))
                if search_names:
                    query = query.filter(OldEmployeeModel.nickname.like(f"%{search_names}%"))
                if search_father_lastname:
                    query = query.filter(OldEmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                if search_mother_lastname:
                    query = query.filter(OldEmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                if search_branch_office_id:
                    query = query.filter(OldEmployeeLaborDatumModel.branch_office_id == search_branch_office_id)
            
            employees = query.paginate(page=page, per_page=20, error_out=False)
        else:
            query = EmployeeModel.query\
                        .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut)\
                        .add_columns(EmployeeModel.id, EmployeeModel.rut, EmployeeModel.visual_rut, EmployeeModel.nickname).order_by('rut')

            if len(data) > 0:
                if search_rut:
                    query = query.filter(EmployeeModel.visual_rut.like(f"%{search_rut}%"))
                if search_names:
                    query = query.filter(EmployeeModel.nickname.like(f"%{search_names}%"))
                if search_father_lastname:
                    query = query.filter(EmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                if search_mother_lastname:
                    query = query.filter(EmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                if search_branch_office_id:
                    query = query.filter(EmployeeLaborDatumModel.branch_office_id == search_branch_office_id)
            
            employees = query.paginate(page=page, per_page=20, error_out=False)

        return employees

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
        employee.rut = id
        employee.visual_rut = data['rut']
        employee.names = data['names']
        employee.father_lastname = data['father_lastname']
        employee.mother_lastname = data['mother_lastname']
        employee.nickname = nickname
        employee.gender_id = data['gender_id']
        employee.nationality_id = data['nationality_id']
        employee.cellphone = data['cellphone']
        employee.personal_email = data['personal_email']
        employee.born_date = data['born_date']
        employee.updated_date = datetime.now()

        db.session.add(employee)
        if db.session.commit():
            return employee
        else:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def update_signature(signature, id):
        employee = EmployeeModel.query.filter_by(rut = id).first()
        employee.signature = signature
        employee.updated_date = datetime.now()

        db.session.add(employee)
        if db.session.commit():
            return employee
        else:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def delete_picture(rut):
        employee = EmployeeModel.query.filter_by(rut = rut).first()
        employee.picture = ''
        employee.updated_date = datetime.now()

        db.session.add(employee)
        if db.session.commit():
            return employee
        else:
            return {'msg': 'Data could not be stored'}

