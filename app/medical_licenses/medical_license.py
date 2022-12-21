from app.models.models import MedicalLicenseModel, MedicalLicenseTypeModel
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
                .add_columns(MedicalLicenseTypeModel.medical_license_type, MedicalLicenseModel.id, MedicalLicenseModel.folio,  MedicalLicenseModel.rut, MedicalLicenseModel.since, MedicalLicenseModel.until, MedicalLicenseModel.added_date, MedicalLicenseModel.days)\
                .filter(MedicalLicenseModel.rut==rut)\
                .all()
            
            return medical_licenses
        else:
            medical_licenses = MedicalLicenseModel.query\
                .join(MedicalLicenseTypeModel, MedicalLicenseTypeModel.id == MedicalLicenseModel.medical_license_type_id)\
                .add_columns(MedicalLicenseTypeModel.medical_license_type, MedicalLicenseModel.id, MedicalLicenseModel.folio,  MedicalLicenseModel.rut, MedicalLicenseModel.since, MedicalLicenseModel.until, MedicalLicenseModel.added_date, MedicalLicenseModel.days)\
                .filter(MedicalLicenseModel.rut==rut)\
                .group_by(text(fields))\
                .first()
            
            return medical_licenses
        
    def days(rut, period):
        medical_license = MedicalLicenseModel.query.filter_by(rut=rut, period=period).group_by(text("period")).first()

        if medical_license == 'None':
            return 0
        else:
            return medical_license.days

    @staticmethod
    def store(data):
        get_periods = Helper.get_periods(data['since'], data['until'])

        for i in range(len(get_periods)):
            period = Helper.split(get_periods[i][0], '-')
            period = period[1] +'-'+ period[0]

            medical_license = MedicalLicenseModel()
            medical_license.document_employee_id = 35
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
    def delete(id):
        medical_license = MedicalLicenseModel.query.filter_by(id=id).first()

        db.session.delete(medical_license)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0