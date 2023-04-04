from app.models.models import MedicalLicenseModel, MedicalLicenseTypeModel, OldMedicalLicenseModel, DocumentEmployeeModel, PatologyTypeModel
from app.helpers.helper import Helper
from sqlalchemy.sql import text
from app import db
from datetime import datetime

class MedicalLicense():
    @staticmethod
    def get(rut, fields = ''):
        if fields == '':
            medical_licenses = MedicalLicenseModel.query\
                .join(MedicalLicenseTypeModel, MedicalLicenseTypeModel.id == MedicalLicenseModel.medical_license_type_id)\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == MedicalLicenseModel.document_employee_id)\
                .join(PatologyTypeModel, PatologyTypeModel.id == MedicalLicenseModel.patology_type_id)\
                .add_columns(PatologyTypeModel.patology_type, DocumentEmployeeModel.status_id, MedicalLicenseModel.document_employee_id, MedicalLicenseTypeModel.medical_license_type, MedicalLicenseModel.id, MedicalLicenseModel.folio,  MedicalLicenseModel.rut, MedicalLicenseModel.since, MedicalLicenseModel.until, MedicalLicenseModel.added_date, MedicalLicenseModel.days)\
                .order_by(MedicalLicenseModel.id.desc())\
                .filter(MedicalLicenseModel.rut==rut)\
                .all()
            
            return medical_licenses
        else:
            medical_licenses = MedicalLicenseModel.query\
                .join(MedicalLicenseTypeModel, MedicalLicenseTypeModel.id == MedicalLicenseModel.medical_license_type_id)\
                .join(PatologyTypeModel, PatologyTypeModel.id == MedicalLicenseModel.patology_type_id)\
                .join(DocumentEmployeeModel, DocumentEmployeeModel.id == MedicalLicenseModel.document_employee_id)\
                .add_columns(PatologyTypeModel.patology_type, DocumentEmployeeModel.status_id, MedicalLicenseModel.document_employee_id, MedicalLicenseTypeModel.medical_license_type, MedicalLicenseModel.id, MedicalLicenseModel.folio,  MedicalLicenseModel.rut, MedicalLicenseModel.since, MedicalLicenseModel.until, MedicalLicenseModel.added_date, MedicalLicenseModel.days)\
                .filter(MedicalLicenseModel.rut==rut)\
                .order_by(MedicalLicenseModel.id.desc())\
                .group_by(text(fields))\
                .first()
            
            return medical_licenses

    @staticmethod
    def get_by_rut(rut):
        medical_licenses = MedicalLicenseModel.query\
                .join(MedicalLicenseTypeModel, MedicalLicenseTypeModel.id == MedicalLicenseModel.medical_license_type_id)\
                .join(PatologyTypeModel, PatologyTypeModel.id == MedicalLicenseModel.patology_type_id)\
                .add_columns(PatologyTypeModel.patology_type, MedicalLicenseModel.document_employee_id, MedicalLicenseModel.updated_date, MedicalLicenseModel.period, MedicalLicenseModel.patology_type_id, MedicalLicenseTypeModel.medical_license_type, MedicalLicenseModel.medical_license_type_id, MedicalLicenseModel.id, MedicalLicenseModel.folio,  MedicalLicenseModel.rut, MedicalLicenseModel.since, MedicalLicenseModel.until, MedicalLicenseModel.added_date, MedicalLicenseModel.days)\
                .filter(MedicalLicenseModel.rut==rut)\
                .all()
            
        return medical_licenses
        
    def days(rut, period):
        medical_license = MedicalLicenseModel.query.filter_by(rut=rut, period=period).group_by(text("period")).first()

        if medical_license == 'None':
            return 0
        else:
            return medical_license.days

    @staticmethod
    def store(id, data):
        get_periods = Helper.get_periods(data['since'], data['until'])

        for i in range(len(get_periods)):
            period = Helper.split(get_periods[i][0], '-')
            period = period[1] +'-'+ period[0]

            medical_license = MedicalLicenseModel()
            medical_license.document_employee_id = id
            medical_license.medical_license_type_id = data['medical_license_type_id']
            medical_license.patology_type_id = data['patology_type_id']
            medical_license.period = period
            medical_license.rut = data['rut']
            medical_license.folio = data['folio']
            medical_license.since = get_periods[i][0]
            medical_license.until = get_periods[i][1]
            medical_license.days = get_periods[i][2]
            medical_license.added_date = datetime.now()
            medical_license.updated_date = datetime.now()

            db.session.add(medical_license)
            db.session.commit()

        return 1

    @staticmethod
    def end_document_delete(id):
        medical_license = MedicalLicenseModel.query.filter_by(id=id).first()

        db.session.delete(medical_license)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def delete(id):
        medical_license = MedicalLicenseModel.query.filter_by(document_employee_id=id).first()

        db.session.delete(medical_license)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def old_data_get_by_rut(rut, order_id):
        old_medical_licenses = OldMedicalLicenseModel.query\
                .join(MedicalLicenseTypeModel, MedicalLicenseTypeModel.id == OldMedicalLicenseModel.medical_license_type_id)\
                .add_columns(OldMedicalLicenseModel.updated_date, OldMedicalLicenseModel.document_employee_id, OldMedicalLicenseModel.period, OldMedicalLicenseModel.patology_type_id, OldMedicalLicenseModel.medical_license_type_id, MedicalLicenseTypeModel.medical_license_type, OldMedicalLicenseModel.id, OldMedicalLicenseModel.folio,  OldMedicalLicenseModel.rut, OldMedicalLicenseModel.since, OldMedicalLicenseModel.until, OldMedicalLicenseModel.added_date, OldMedicalLicenseModel.days)\
                .filter(OldMedicalLicenseModel.rut==rut, OldMedicalLicenseModel.order_id==order_id)\
                .all()
            
        return old_medical_licenses

    @staticmethod
    def restore(rut, order_id):
        old_medical_licenses = MedicalLicense.old_data_get_by_rut(rut, order_id)

        data = []

        for old_medical_license in old_medical_licenses:
            data = [
                old_medical_license.document_employee_id,
                old_medical_license.medical_license_type_id,
                old_medical_license.patology_type_id,
                old_medical_license.period,
                old_medical_license.rut,
                old_medical_license.folio,
                old_medical_license.since,
                old_medical_license.until,
                old_medical_license.days,
                old_medical_license.added_date,
                old_medical_license.updated_date
            ]

            MedicalLicense.restore_store(data)

            MedicalLicense.old_data_delete(old_medical_license.id)

        return 1

    @staticmethod
    def restore_store(data):
        medical_license = MedicalLicenseModel()
        medical_license.document_employee_id = data[0]
        medical_license.medical_license_type_id = data[1]
        medical_license.patology_type_id = data[2]
        medical_license.period = data[3]
        medical_license.rut = data[4]
        medical_license.folio = data[5]
        medical_license.since = data[6]
        medical_license.until = data[7]
        medical_license.days = data[8]
        medical_license.added_date = data[9]
        medical_license.updated_date = data[10]

        db.session.add(medical_license)
        db.session.commit()

        try:
            db.session.commit()

            return medical_license
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def old_data_delete(id):
        old_medical_license = OldMedicalLicenseModel.query.filter_by(id=id).first()

        db.session.delete(old_medical_license)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def upload(id, file):
        document_employee = DocumentEmployeeModel.query.filter_by(id=id).first()
        document_employee.support = file
        document_employee.status_id = 4
        document_employee.updated_date = datetime.now()

        db.session.add(document_employee)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def update(old_id, new_id):
        medical_license = MedicalLicenseModel.query.filter_by(document_employee_id=old_id).first()
        medical_license.document_employee_id = new_id

        db.session.add(medical_license)
        db.session.commit()
        
        return medical_license.id