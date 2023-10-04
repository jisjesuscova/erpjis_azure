from flask import request
from app.models.models import HealthModel
from app import db
from datetime import datetime

class Health():
    @staticmethod
    def get(id = ''):
        if id == '':
            health = HealthModel.query.all()

            return health
        else:
            health = HealthModel.query.get(id)

            return health

    @staticmethod
    def store(data):
        health = HealthModel()
        health.health = data['health'] 
        health.added_date = datetime.now()
        health.updated_date = datetime.now()

        db.session.add(health)
        db.session.commit()
        
        return health

    @staticmethod
    def update(data, id):
        health = HealthModel.query.get(id)
        health.health = data['health']
        health.updated_date = datetime.now()

        db.session.add(health)
        db.session.commit()
        
        return health

    @staticmethod
    def delete(id):
        health = HealthModel.query.get(id)

        db.session.delete(health)
        db.session.commit()
        
        return health

