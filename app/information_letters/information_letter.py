from app.models.models import InformationLetterModel
from sqlalchemy.sql import text

class InformationLetter():
    @staticmethod
    def get(id):
        print(id)
        information_letter = InformationLetterModel.query.filter_by(document_employee_id=id).first()
            
        return information_letter
