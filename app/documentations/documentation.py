from flask import request
from app.models.models import OldDocumentEmployeeModel, DocumentEmployeeModel, EmployeeModel, EmployeeLaborDatumModel, BranchOfficeModel, SupervisorModel, DocumentTypeModel
from app import db
from datetime import datetime
from app.end_documents.end_document import EndDocument
from app.medical_licenses.medical_license import MedicalLicense
from app.vacations.vacation import Vacation

class Documentation():
    @staticmethod
    def get_by_rut(rut):
        documents_employees = DocumentEmployeeModel.query\
                    .join(DocumentTypeModel, DocumentTypeModel.id == DocumentEmployeeModel.document_type_id)\
                    .add_columns(DocumentEmployeeModel.id, DocumentEmployeeModel.status_id, DocumentEmployeeModel.rut, DocumentEmployeeModel.document_type_id, DocumentEmployeeModel.support, DocumentEmployeeModel.updated_date, DocumentEmployeeModel.added_date, DocumentEmployeeModel.status_id).filter(DocumentEmployeeModel.rut==rut).all()

        return documents_employees