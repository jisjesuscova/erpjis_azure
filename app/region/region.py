from app.models.models import RegionModel
from app import db
from datetime import datetime

class Region():
    @staticmethod
    def get(id = ''):
        if id == '':
            region = RegionModel.query.all()

            return region
        else:
            region = RegionModel.query.get(id)

            return region

    @staticmethod
    def store(data):
        region = RegionModel()
        region.region = data['region'] 
        region.added_date = datetime.now()
        region.updated_date = datetime.now()

        db.session.add(region)
        db.session.commit()
        
        return region

    @staticmethod
    def update(data, id):
        region = RegionModel.query.get(id)
        region.region = data['region']
        region.updated_date = datetime.now()

        db.session.add(region)
        db.session.commit()
        
        return region

    @staticmethod
    def delete(id):
        region = RegionModel.query.get(id)

        db.session.delete(region)
        db.session.commit()
        
        return region

