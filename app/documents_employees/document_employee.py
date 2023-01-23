from flask import request
from app.models.models import DocumentEmployeeModel, EmployeeModel, EmployeeLaborDatumModel, BranchOfficeModel, SupervisorModel, DocumentTypeModel
from app import db
from datetime import datetime
from sqlalchemy import and_, func

class DocumentEmployee():
    @staticmethod
    def get(rut = '', type = '', page = '', group = ''):
        if group != '':
            if rut == '':
                documents_employees = DocumentEmployeeModel.query\
                    .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
                    .add_columns(DocumentEmployeeModel.id, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id).filter(DocumentTypeModel.document_group_id==group)
            else:
                documents_employees = DocumentEmployeeModel.query\
                    .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
                    .add_columns(DocumentEmployeeModel.id, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id).filter(DocumentEmployeeModel.rut==rut, DocumentTypeModel.document_group_id==group)
        elif type != '':
            documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=type).order_by(db.desc(DocumentEmployeeModel.added_date)).paginate(page=page, per_page=10, error_out=False)
        else:
            documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut).paginate(page=page, per_page=20, error_out=False)

        return documents_employees
    
    @staticmethod
    def get_by_id(id):
        document_employee = DocumentEmployeeModel.query.filter_by(id=id).first()
        return document_employee

    @staticmethod
    def get_by_type(rut = '', type = '', page = '', data = []):
        if page != '':
            if rut == '':
                if len(data) > 0:
                    search_rut = data['rut']
                    search_names = data['names']
                    search_father_lastname = data['father_lastname']
                    search_mother_lastname = data['mother_lastname']

                query = DocumentEmployeeModel.query\
                    .join(EmployeeModel, EmployeeModel.rut == DocumentEmployeeModel.rut)\
                    .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut)\
                    .join(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id)\
                    .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
                    .add_columns(DocumentEmployeeModel.id, EmployeeModel.rut, EmployeeModel.visual_rut, EmployeeModel.nickname, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id).order_by(db.desc(DocumentEmployeeModel.added_date)).filter(DocumentEmployeeModel.document_type_id==type)

                if len(data) > 0:
                    if search_rut:
                        query = query.filter(EmployeeModel.visual_rut.like(f"%{search_rut}%"))
                    if search_names:
                        query = query.filter(EmployeeModel.nickname.like(f"%{search_names}%"))
                    if search_father_lastname:
                        query = query.filter(EmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                    if search_mother_lastname:
                        query = query.filter(EmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                    
                documents_employees = query.paginate(page=page, per_page=20, error_out=False)

            else:
                documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=type).paginate(page=page, per_page=20, error_out=False)
        else:
            documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=type).all()
        
        return documents_employees

    @staticmethod
    def get_by_supervisor(rut, page, data = []):

        if len(data) > 0:
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
                    .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
                    .add_columns(DocumentEmployeeModel.id, EmployeeModel.rut, EmployeeModel.visual_rut, EmployeeModel.nickname, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id).filter(SupervisorModel.rut==rut, DocumentTypeModel.document_group_id==2,  DocumentEmployeeModel.status_id==1)

        if len(data) > 0:
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
    def get_by_administrator(rut, page, data = []):

        if len(data) > 0:
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
                    .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
                    .add_columns(DocumentEmployeeModel.id, EmployeeModel.rut, EmployeeModel.visual_rut, EmployeeModel.nickname, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id).filter(SupervisorModel.rut==rut, DocumentTypeModel.document_group_id==2)

        if len(data) > 0:
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
        else:
            query = query.filter(DocumentEmployeeModel.status_id == 2)
        
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
    def store_by_dropbox(rut, file, document_type_id, status_id, period = ''):
        document_employee = DocumentEmployeeModel()
        document_employee.status_id = status_id
        document_employee.rut = rut
        document_employee.document_type_id = document_type_id
        document_employee.support = file
        document_employee.added_date = period + ' 00:00:00'
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        db.session.commit()
        
        return document_employee.id

    @staticmethod
    def sign(id, rut, support):
        document_employee = DocumentEmployeeModel.query.filter_by(id=id).first()
        document_employee.status_id = 4
        document_employee.support = support
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        db.session.commit()
        
        return document_employee.id

    @staticmethod
    def delete(id):
        document_employee = DocumentEmployeeModel.query.filter_by(id=id).first()

        db.session.delete(document_employee)
        try:
            db.session.commit()

            return document_employee
        except Exception as e:
            return {'msg': 'Data could not be stored'}