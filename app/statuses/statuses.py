from app.models.models import StatusesModel, statuses_groupModel
from app import db
from datetime import datetime

class Statuses():
    @staticmethod
    def get(id = ''):
        if id == '':
            statuses = StatusesModel.query\
            .join(statuses_groupModel, statuses_groupModel.statuses_group_id == StatusesModel.statuses_group_id)\
            .add_columns(StatusesModel.statuses_id, StatusesModel.statuses,  statuses_groupModel.statuses_group)\
            .all()

            return statuses
        else:
            statuses = StatusesModel.query.get(id)

            return statuses

    @staticmethod
    def store(data):
        statuses = StatusesModel()
        statuses.statuses_group_id = data['statuses_group_id'] 
        statuses.statuses = data['statuses'] 
        statuses.added_date = datetime.now()
        statuses.updated_date = datetime.now()

        db.session.add(statuses)
        db.session.commit()
        
        return statuses

    @staticmethod
    def update(data, id):
        statuses = StatusesModel.query.get(id)
        statuses.statuses = data['statuses']
        statuses.updated_date = datetime.now()

        db.session.add(statuses)
        db.session.commit()
        
        return statuses

    @staticmethod
    def delete(id):
        statuses = StatusesModel.query.get(id)

        db.session.delete(statuses)
        db.session.commit()
        
        return statuses

