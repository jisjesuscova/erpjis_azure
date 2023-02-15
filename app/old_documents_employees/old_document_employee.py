from app.models.models import OldDocumentEmployeeModel, DocumentTypeModel, OldEmployeeModel, OldEmployeeLaborDatumModel, BranchOfficeModel
from app.documents_employees.document_employee import DocumentEmployee
from app import db
from app.end_documents.end_document import EndDocument
from app.old_medical_licenses.old_medical_license import OldMedicalLicense
from app.old_vacations.old_vacation import OldVacation

class OldDocumentEmployee():
    @staticmethod
    def get(rut = '', type = '', page = '', group = ''):
        if group != '':
            if rut == '':
                documents_employees = OldDocumentEmployeeModel.query\
                    .join(DocumentTypeModel, DocumentTypeModel.id == OldDocumentEmployeeModel.document_type_id)\
                    .add_columns(OldDocumentEmployeeModel.id, DocumentTypeModel.document_type, OldDocumentEmployeeModel.added_date, OldDocumentEmployeeModel.status_id).filter(DocumentTypeModel.document_group_id==group)
            else:
                documents_employees = OldDocumentEmployeeModel.query\
                    .join(DocumentTypeModel, DocumentTypeModel.id == OldDocumentEmployeeModel.document_type_id)\
                    .add_columns(OldDocumentEmployeeModel.id, DocumentTypeModel.document_type, OldDocumentEmployeeModel.added_date, OldDocumentEmployeeModel.status_id).filter(OldDocumentEmployeeModel.rut==rut, DocumentTypeModel.document_group_id==group)
        elif type != '':
            documents_employees = OldDocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=type).order_by(db.desc(OldDocumentEmployeeModel.added_date)).paginate(page=page, per_page=10, error_out=False)
        else:
            documents_employees = OldDocumentEmployeeModel.query.filter_by(rut=rut).paginate(page=page, per_page=20, error_out=False)

        return documents_employees

    @staticmethod
    def get_last_order(rut):
        document_employee = OldDocumentEmployeeModel.query.filter_by(rut=rut).order_by(OldDocumentEmployeeModel.order_id.desc()).first()
        
        document_employee_qty = OldDocumentEmployeeModel.query.filter_by(rut=rut).order_by(OldDocumentEmployeeModel.order_id.desc()).count()

        if document_employee_qty > 0:
            return int(document_employee.order_id) + 1
        else:
            return 1

    @staticmethod
    def end_document_delete(rut):
        old_document_employees = OldDocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=22).all()

        for old_document_employee in old_document_employees:
            old_document_employee_to_delete = OldDocumentEmployeeModel.query.filter_by(id=old_document_employee.id).first()

            db.session.delete(old_document_employee_to_delete)

            db.session.commit()
        
        return 1

    @staticmethod
    def finish(rut, order_id):
        documents_employees = DocumentEmployee.get_by_rut(rut)

        data = []

        for document_employee in documents_employees:
            status_id = document_employee['status_id']
            rut = document_employee['rut']
            document_type_id = document_employee['document_type_id']
            support = document_employee['support']
            added_date = document_employee['added_date']
            updated_date = document_employee['updated_date']

            data = [
                status_id,
                rut,
                document_type_id,
                order_id,
                support,
                added_date,
                updated_date
            ]

            id = OldDocumentEmployee.store(data)

            if document_employee['document_type_id'] == 6:
                OldVacation.update(document_employee['id'], id)

            if document_employee['document_type_id'] == 22:
                EndDocument.update(document_employee['id'], id)

            if document_employee['document_type_id'] == 35:
                OldMedicalLicense.update(document_employee['id'], id)

            DocumentEmployee.delete(document_employee.id)

        return 1

    @staticmethod
    def store(data):
        old_document_employee = OldDocumentEmployeeModel()
        old_document_employee.status_id = data[0]
        old_document_employee.rut = data[1]
        old_document_employee.document_type_id = data[2]
        old_document_employee.order_id = data[3]
        old_document_employee.support = data[4]
        old_document_employee.added_date = data[5]
        old_document_employee.updated_date = data[6]

        db.session.add(old_document_employee)
        db.session.commit()
        
        return old_document_employee.id

    @staticmethod
    def get_by_id(id):
        old_document_employee = OldDocumentEmployeeModel.query.filter_by(id=id).first()
        return old_document_employee
    
    @staticmethod
    def get_by_type(rut = '', type = '', page = '', data = [], status_id = ''):
        if page != '':
            if rut == '':
                if len(data) > 0:
                    search_rut = data['rut']
                    search_names = data['names']
                    search_father_lastname = data['father_lastname']
                    search_mother_lastname = data['mother_lastname']
                
                query = OldDocumentEmployeeModel.query\
                    .join(OldEmployeeModel, OldEmployeeModel.rut == OldDocumentEmployeeModel.rut)\
                    .join(OldEmployeeLaborDatumModel, OldEmployeeLaborDatumModel.rut == OldEmployeeModel.rut)\
                    .join(BranchOfficeModel, BranchOfficeModel.id == OldEmployeeLaborDatumModel.branch_office_id)\
                    .join(DocumentTypeModel, DocumentTypeModel.id == OldDocumentEmployeeModel.document_type_id)\
                    .add_columns(OldDocumentEmployeeModel.support, OldDocumentEmployeeModel.id, OldEmployeeModel.rut, OldEmployeeModel.visual_rut, OldEmployeeModel.nickname, DocumentTypeModel.document_type, OldDocumentEmployeeModel.added_date, OldDocumentEmployeeModel.status_id).order_by(db.desc(OldDocumentEmployeeModel.added_date)).filter(OldDocumentEmployeeModel.document_type_id==type)

                if status_id != '':
                    query = query.filter(OldDocumentEmployeeModel.status_id.like(f"%{status_id}%"))

                if len(data) > 0:
                    if search_rut:
                        query = query.filter(OldEmployeeModel.visual_rut.like(f"%{search_rut}%"))
                    if search_names:
                        query = query.filter(OldEmployeeModel.nickname.like(f"%{search_names}%"))
                    if search_father_lastname:
                        query = query.filter(OldEmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                    if search_mother_lastname:
                        query = query.filter(OldEmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                    
                documents_employees = query.paginate(page=page, per_page=20, error_out=False)

            else:
                documents_employees = OldDocumentEmployeeModel.query\
                    .join(OldEmployeeModel, OldEmployeeModel.rut == OldDocumentEmployeeModel.rut)\
                    .join(OldEmployeeLaborDatumModel, OldEmployeeLaborDatumModel.rut == OldEmployeeModel.rut)\
                    .join(BranchOfficeModel, BranchOfficeModel.id == OldEmployeeLaborDatumModel.branch_office_id)\
                    .join(DocumentTypeModel, DocumentTypeModel.id == OldDocumentEmployeeModel.document_type_id)\
                    .add_columns(OldDocumentEmployeeModel.support, OldDocumentEmployeeModel.id, OldEmployeeModel.rut, OldEmployeeModel.visual_rut, OldEmployeeModel.nickname, DocumentTypeModel.document_type, OldDocumentEmployeeModel.added_date, OldDocumentEmployeeModel.status_id).order_by(db.desc(OldDocumentEmployeeModel.added_date)).filter(OldDocumentEmployeeModel.rut==rut, DocumentTypeModel.id==type).paginate(page=page, per_page=20, error_out=False)     
        else:
            documents_employees = OldDocumentEmployeeModel.query.filter_by(rut=rut, document_type_id=type).all()
        
        return documents_employees