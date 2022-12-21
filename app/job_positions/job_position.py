from flask import request
from app.models.models import JobPositionModel
from app import db
from datetime import datetime

class JobPosition():
    @staticmethod
    def get(id = ''):
        if id == '':
            job_positions = JobPositionModel.query.order_by('job_position').all()

            return job_positions
        else:
            job_position = JobPositionModel.query.get(id)

            return job_position

        
