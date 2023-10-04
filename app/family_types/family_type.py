from flask import request
from app.models.models import FamilyTypeModel

class FamilyType():
    @staticmethod
    def get():
        family_types = FamilyTypeModel.query.all()

        return family_types
