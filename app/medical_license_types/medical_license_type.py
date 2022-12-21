from flask import request
from app.models.models import MedicalLicenseTypeModel
from app import db

class MedicalLicenseType():
    @staticmethod
    def get():
        medical_license_types = MedicalLicenseTypeModel.query.all()

        return medical_license_types
