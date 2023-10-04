from app.models.models import InformationLetterModel
from sqlalchemy.sql import text

class InformationLetter():
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