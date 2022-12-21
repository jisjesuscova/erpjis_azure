from flask import request
from app.models.models import ZoneModel
from app import db
from datetime import datetime

class Zone():
    @staticmethod
    def get(id = ''):
        if id == '':
            zones = ZoneModel.query.all()

            return zones
        else:
            zone = ZoneModel.query.get(id)

            return zone

    @staticmethod
    def store(data):
        zone = ZoneModel()
        zone.zone = data['zone'] 
        zone.added_date = datetime.now()
        zone.updated_date = datetime.now()

        db.session.add(zone)
        db.session.commit()
        
        return zone

    @staticmethod
    def update(data, id):
        zone = ZoneModel.query.get(id)
        zone.zone = data['zone']
        zone.updated_date = datetime.now()

        db.session.add(zone)
        db.session.commit()
        
        return zone

    @staticmethod
    def delete(id):
        zone = ZoneModel.query.get(id)

        db.session.delete(zone)
        db.session.commit()
        
        return zone

