from flask import request
from app.models.models import SegmentModel
from app import db
from datetime import datetime

class Segment():
    @staticmethod
    def get(id = ''):
        if id == '':
            principal = SegmentModel.query.all()

            return segment
        else:
            principal = SegmentModel.query.get(id)

            return segment

    @staticmethod
    def store(data):
        segment = SegmentModel()
        segment.segment = data['segment'] 
        segment.added_date = datetime.now()
        segment.updated_date = datetime.now()

        db.session.add(segment)
        db.session.commit()
        
        return principal

    @staticmethod
    def update(data, id):
        segment = SegmentModel.query.get(id)
        segment.segment = data['segment']
        segment.updated_date = datetime.now()

        db.session.add(segment)
        db.session.commit()
        
        return principal

    @staticmethod
    def delete(id):
        segment = SegmentModel.query.get(id)

        db.session.delete(segment)
        db.session.commit()
        
        return principal

