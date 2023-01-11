from flask import request
from app.models.models import DocumentEmployeeModel, EmployeeModel, EmployeeLaborDatumModel, BranchOfficeModel, SupervisorModel, DocumentTypeModel
from app import db
from datetime import datetime
from sqlalchemy import and_

class DocumentEmployee():
    @staticmethod
    def get(rut, page = ''):
        documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut).paginate(page=page, per_page=20, error_out=False)
        
        return documents_employees
    
    @staticmethod
    def get_by_id(id):
        document_employee = DocumentEmployeeModel.query.filter_by(id=id).first()
        return document_employee

    @staticmethod
    def get_by_type(rut, type):
        documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=type).all()
        
        return documents_employees

    @staticmethod
    def get_by_supervisor(rut, page, data = []):

        if len(data) == 0:
            return ''
        else:
            search_rut = data['rut']
            search_names = data['names']
            search_father_lastname = data['father_lastname']
            search_mother_lastname = data['mother_lastname']
            search_status_id = data['status_id']
            search_branch_office_id = data['branch_office_id']

            query = DocumentEmployeeModel.query\
                    .join(EmployeeModel, EmployeeModel.rut == DocumentEmployeeModel.rut)\
                    .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut)\
                    .join(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id)\
                    .join(SupervisorModel, SupervisorModel.rut == EmployeeModel.rut)\
                    .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
                    .add_columns(DocumentEmployeeModel.id, EmployeeModel.rut, EmployeeModel.visual_rut, EmployeeModel.nickname, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id).filter(SupervisorModel.rut==rut, DocumentTypeModel.document_group_id==2)

            if search_rut:
                query = query.filter(EmployeeModel.visual_rut.like(f"%{search_rut}%"))
            if search_names:
                query = query.filter(EmployeeModel.nickname.like(f"%{search_names}%"))
            if search_father_lastname:
                query = query.filter(EmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
            if search_mother_lastname:
                query = query.filter(EmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
            if search_status_id:
                query = query.filter(DocumentEmployeeModel.status_id == search_status_id)
            if search_branch_office_id:
                query = query.filter(EmployeeLaborDatumModel.branch_office_id == search_branch_office_id)

            documents_employees = query.paginate(page=page, per_page=20, error_out=False)

            return documents_employees

    @staticmethod
    def store(data):
        document_employee = DocumentEmployeeModel()
        document_employee.status_id = data['status_id']
        document_employee.rut = data['rut']
        document_employee.document_type_id = data['document_type_id']
        document_employee.added_date = datetime.now()
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        db.session.commit()
        
        return document_employee.id

    
    @staticmethod
    def store_by_dropbox(rut, document_type_id, status_id):
        document_employee = DocumentEmployeeModel()
        document_employee.status_id = status_id
        document_employee.rut = rut
        document_employee.document_type_id = document_type_id
        document_employee.added_date = datetime.now()
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        db.session.commit()
        
        return document_employee.id
