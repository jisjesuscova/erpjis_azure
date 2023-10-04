from flask import request
from app.models.models import statuses_groupModel
from app import db
from datetime import datetime

class Statuses_group():
    @staticmethod
    def get(id = ''):
        if id == '':
            statuses_group = statuses_groupModel.query.all()

            return statuses_group
        else:
            statuses_group = statuses_groupModel.query.get(id)

            return statuses_group

    @staticmethod
    def store(data):
        statuses_group = statuses_groupModel()
        statuses_group.statuses_group = data['statuses_group'] 
        statuses_group.added_date = datetime.now()
        statuses_group.updated_date = datetime.now()

        db.session.add(statuses_group)
        db.session.commit()
        
        return statuses_group

    @staticmethod
    def update(data, id):
        statuses_group = statuses_groupModel.query.get(id)
        statuses_group.statuses_group = data['statuses_group']
        statuses_group.updated_date = datetime.now()

        db.session.add(statuses_group)
        db.session.commit()
        
        return statuses_group

    @staticmethod
    def delete(id):
        statuses_group = statuses_groupModel.query.get(id)

        db.session.delete(statuses_group)
        db.session.commit()
        
        return statuses_group

