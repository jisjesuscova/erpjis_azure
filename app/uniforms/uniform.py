from flask import request
from app.models.models import UniformModel, UniformTypeModel
from app import db
from datetime import datetime

class Uniform():
    @staticmethod
    def get(rut):
        uniforms = UniformModel.query\
                            .join(UniformTypeModel, UniformTypeModel.id == UniformModel.uniform_type_id)\
                            .add_columns(UniformModel.delivered_date, UniformModel.id, UniformTypeModel.uniform_type).filter(UniformModel.rut==rut).all()

        return uniforms

    @staticmethod
    def store(data):
        uniform = UniformModel()
        uniform.uniform_type_id = data['uniform_type_id']
        uniform.rut = data['rut']
        uniform.delivered_date = data['delivered_date']
        uniform.added_date = datetime.now()

        db.session.add(uniform)
        
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0
    
    @staticmethod
    def delete(id):
        uniform = UniformModel.query.filter_by(id=id).first()

        db.session.delete(uniform)
        try:
            db.session.commit()

            return uniform
        except Exception as e:
            return {'msg': 'Data could not be stored'}