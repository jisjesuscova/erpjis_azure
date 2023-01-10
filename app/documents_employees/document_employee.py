from flask import request
from app.models.models import DocumentEmployeeModel, EmployeeModel, EmployeeLaborDatumModel, BranchOfficeModel, SupervisorModel, DocumentTypeModel
from app import db
from datetime import datetime

class DocumentEmployee():
    @staticmethod
    def get(rut, page):
        documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut).paginate(page=page, per_page=20, error_out=False)
        
        return documents_employees

    @staticmethod
    def get_by_type(rut, type):
        documents_employees = DocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=type).all()
        
        return documents_employees

    @staticmethod
    def get_by_supervisor(rut, page):
        documents_employees = DocumentEmployeeModel.query\
            .join(EmployeeModel, EmployeeModel.rut == DocumentEmployeeModel.rut)\
            .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut)\
            .join(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id)\
            .join(SupervisorModel, SupervisorModel.rut == EmployeeModel.rut)\
            .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
            .add_columns(DocumentEmployeeModel.id, EmployeeModel.visual_rut, EmployeeModel.rut, EmployeeModel.nickname, DocumentTypeModel.document_type, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id)\
            .filter(SupervisorModel.rut==rut, DocumentEmployeeModel.status_id==1, DocumentTypeModel.document_group_id==2)\
            .paginate(page=page, per_page=20, error_out=False)
        
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