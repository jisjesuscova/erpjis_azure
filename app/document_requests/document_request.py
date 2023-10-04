from flask import request
from app.models.models import DocumentEmployeeModel, AbandonDayDocumentModel, InformationLetterModel, PuntualityAnnexedtDocumentModel
from app import db
from datetime import datetime
from app.vacations.vacation import Vacation

class DocumentRequest():
    @staticmethod
    def store(data):
        document_employee = DocumentEmployeeModel()
        document_employee.status_id = data['status_id']
        document_employee.rut = data['rut']
        document_employee.document_type_id = data['document_type_id']
        document_employee.support = ''
        document_employee.added_date = datetime.now()
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        db.session.commit()
        
        return document_employee.id

    @staticmethod
    def status(id, data = [], status_id = ''):
        if len(data) > 0:
            Vacation.update('', id, data)

        document_employee = DocumentEmployeeModel.query.filter_by(id=id).first()
        document_employee.status_id = status_id
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        db.session.commit()
        
        return document_employee.id

    @staticmethod
    def storebytype(id, data):
        if data['document_type_id'] == '1':
            document = InformationLetterModel()
            document.letter_type_id = 1
            document.document_employee_id = id
            document.description = data['description']
            document.added_date = datetime.now()

            db.session.add(document)
            db.session.commit()

            return document

        elif data['document_type_id'] == '6':
            document = AbandonDayDocumentModel()
            document.document_employee_id = id
            document.abandon_date = data['abandon_date']
            document.added_date = datetime.now()

            db.session.add(document)
            db.session.commit()

            return document

        elif data['document_type_id'] == '11':
            document = PuntualityAnnexedtDocumentModel()
            document.document_employee_id = id
            document.asignation = data['asignation']
            document.added_date = datetime.now()

            db.session.add(document)
            db.session.commit()

            return document

        elif data['document_type_id'] == '13':
            document = LetterInformationModel()
            document.letter_type_id = id
            document.document_employee_id = 2
            document.description = data['description']
            document.added_date = datetime.now()

            db.session.add(document)
            db.session.commit()

            return document
        
        return str(1)
        
