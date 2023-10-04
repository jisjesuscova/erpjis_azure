from app.models.models import OldMedicalLicenseModel, MedicalLicenseTypeModel, OldDocumentEmployeeModel
from app.medical_licenses.medical_license import MedicalLicense
from app import db
from sqlalchemy.sql import text

class OldMedicalLicense():
    @staticmethod
    def get(rut, fields = ''):
        if fields == '':
            medical_licenses = OldMedicalLicenseModel.query\
                .join(MedicalLicenseTypeModel, MedicalLicenseTypeModel.id == OldMedicalLicenseModel.medical_license_type_id)\
                .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == OldMedicalLicenseModel.document_employee_id)\
                .add_columns(OldDocumentEmployeeModel.status_id, OldMedicalLicenseModel.document_employee_id, MedicalLicenseTypeModel.medical_license_type, OldMedicalLicenseModel.id, OldMedicalLicenseModel.folio,  OldMedicalLicenseModel.rut, OldMedicalLicenseModel.since, OldMedicalLicenseModel.until, OldMedicalLicenseModel.added_date, OldMedicalLicenseModel.days)\
                .filter(OldMedicalLicenseModel.rut==rut)\
                .all()
            
            return medical_licenses
        else:
            medical_licenses = OldMedicalLicenseModel.query\
                .join(MedicalLicenseTypeModel, MedicalLicenseTypeModel.id == OldMedicalLicenseModel.medical_license_type_id)\
                .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == OldMedicalLicenseModel.document_employee_id)\
                .add_columns(OldDocumentEmployeeModel.status_id, OldMedicalLicenseModel.document_employee_id, MedicalLicenseTypeModel.medical_license_type, OldMedicalLicenseModel.id, OldMedicalLicenseModel.folio, OldMedicalLicenseModel.rut, OldMedicalLicenseModel.since, OldMedicalLicenseModel.until, OldMedicalLicenseModel.added_date, OldMedicalLicenseModel.days)\
                .filter(OldMedicalLicenseModel.rut==rut)\
                .group_by(text(fields))\
                .first()
            
            return medical_licenses

    @staticmethod
    def get_last_order(rut):
        medical_license = OldDocumentEmployeeModel.query.filter_by(rut=rut).order_by(OldDocumentEmployeeModel.order_id.desc()).first()

        medical_license_qty = OldDocumentEmployeeModel.query.filter_by(rut=rut).order_by(OldDocumentEmployeeModel.order_id.desc()).count()
        
        if medical_license_qty > 0:
            return int(medical_license.order_id) + 1
        else:
            return 1

    @staticmethod
    def finish(rut, order_id):
        medical_licenses = MedicalLicense.get_by_rut(rut)

        data = []

        for medical_license in medical_licenses:
            data = [
                medical_license.document_employee_id,
                medical_license.medical_license_type_id,
                medical_license.patology_type_id,
                order_id,
                medical_license.period,
                medical_license.rut,
                medical_license.folio,
                medical_license.since,
                medical_license.until,
                medical_license.days,
                medical_license.added_date,
                medical_license.updated_date
            ]

            OldMedicalLicense.store(data)

            MedicalLicense.end_document_delete(medical_license.id)

        return 1

    @staticmethod
    def store(data):
        old_medical_license = OldMedicalLicenseModel()
        old_medical_license.document_employee_id = data[0]
        old_medical_license.medical_license_type_id = data[1]
        old_medical_license.patology_type_id = data[2]
        old_medical_license.order_id = data[3]
        old_medical_license.period = data[4]
        old_medical_license.rut = data[5]
        old_medical_license.folio = data[6]
        old_medical_license.since = data[7]
        old_medical_license.until = data[8]
        old_medical_license.days = data[9]
        old_medical_license.added_date = data[10]
        old_medical_license.updated_date = data[11]

        db.session.add(old_medical_license)
        db.session.commit()

        try:
            db.session.commit()

            return old_medical_license
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    
    @staticmethod
    def update(old_id, new_id):
        old_medical_license = OldMedicalLicenseModel.query.filter_by(document_employee_id=old_id).first()
        old_medical_license.document_employee_id = new_id

        db.session.add(old_medical_license)
        db.session.commit()
        
        return old_medical_license.id