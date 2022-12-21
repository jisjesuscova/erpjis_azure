from app.models.models import PentionModel
from app import db
from datetime import datetime

class Pention():
    @staticmethod
    def get(id = ''):
        if id == '':
            pention = PentionModel.query.all()

            return pention
        else:
            pention = PentionModel.query.get(id)

            return pention

    @staticmethod
    def store(data):
        pention = PentionModel()
        pention.pention = data['pention'] 
        pention.added_date = datetime.now()
        pention.updated_date = datetime.now()

        db.session.add(pention)
        db.session.commit()
        
        return pention

    @staticmethod
    def update(data, id):
        pention = PentionModel.query.get(id)
        pention.pention = data['pention']
        pention.updated_date = datetime.now()

        db.session.add(pention)
        db.session.commit()
        
        return pention

    @staticmethod
    def delete(id):
        pention = PentionModel.query.get(id)

        db.session.delete(pention)
        db.session.commit()
        
        return pention

