from app.models.models import CommunesModel
from app import db
from datetime import datetime

class Commune():
    @staticmethod
    def get(id = ''):
        if id == '':
            communes = CommunesModel.query.order_by(CommunesModel.commune).all()

            return communes
        else:
            communes = CommunesModel.query.get(id)

            return communes

    @staticmethod
    def region(id):
        communes = CommunesModel.query.filter_by(region_id=id).order_by(CommunesModel.commune).all()

        return communes

    @staticmethod
    def store(data):
        communes = CommunesModel()
        communes.region_id = data['region_id'] 
        communes.commune = data['communes'] 
        communes.added_date = datetime.now()
        communes.updated_date = datetime.now()

        db.session.add(communes)
        db.session.commit()
        
        return communes

    @staticmethod
    def update(data, id):
        communes = CommunesModel.query.get(id)
        communes.communes = data['communes']
        communes.updated_date = datetime.now()

        db.session.add(communes)
        db.session.commit()
        
        return communes

    @staticmethod
    def delete(id):
        communes = CommunesModel.query.get(id)

        db.session.delete(communes)
        db.session.commit()
        
        return communes

