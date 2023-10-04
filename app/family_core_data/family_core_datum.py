from flask import request
from app.models.models import FamilyCoreDatumModel, FamilyTypeModel
from app.helpers.helper import Helper
from flask_sqlalchemy import get_debug_queries
from app import db
from datetime import datetime

class FamilyCoreDatum():
    @staticmethod
    def get(id = '', rut = ''):
        if id != '':
            family_core_datum = FamilyCoreDatumModel.query.filter_by(id=id).first()

            return family_core_datum
        else:
            family_core_data = FamilyCoreDatumModel.query\
            .join(FamilyTypeModel, FamilyTypeModel.id == FamilyCoreDatumModel.family_type_id)\
            .add_columns(FamilyCoreDatumModel.id, FamilyCoreDatumModel.rut_user, FamilyCoreDatumModel.rut, FamilyCoreDatumModel.names, FamilyCoreDatumModel.born_date, FamilyTypeModel.family_type, FamilyCoreDatumModel.support)\
            .filter(FamilyCoreDatumModel.rut_user==rut)\
            .all()
        
            return family_core_data

    @staticmethod
    def store(data, support):
        numeric_rut = Helper.numeric_rut(data['rut'])

        family_core_data = FamilyCoreDatumModel()
        family_core_data.family_type_id = data['family_type_id']
        family_core_data.rut_user = numeric_rut
        family_core_data.gender_id = data['gender_id']
        family_core_data.rut = data['family_rut']
        family_core_data.names = data['names']
        family_core_data.father_lastname = data['father_lastname']
        family_core_data.mother_lastname = data['mother_lastname']
        family_core_data.born_date = data['born_date']
        family_core_data.support = support
        family_core_data.added_date = datetime.now()

        db.session.add(family_core_data)
        
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def update(id, data, support = ''):
        numeric_rut = Helper.numeric_rut(data['rut'])

        family_core_data = FamilyCoreDatumModel.query.filter_by(id=id).first()
        family_core_data.family_type_id = data['family_type_id']
        family_core_data.rut_user = numeric_rut
        family_core_data.gender_id = data['gender_id']
        family_core_data.rut = data['family_rut']
        family_core_data.names = data['names']
        family_core_data.father_lastname = data['father_lastname']
        family_core_data.mother_lastname = data['mother_lastname']
        family_core_data.born_date = data['born_date']
        family_core_data.support = support
        family_core_data.updated_date = datetime.now()

        db.session.add(family_core_data)
        
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def delete(id):
        family_core_data = FamilyCoreDatumModel.query.filter_by(id=id).first()

        db.session.delete(family_core_data)
        try:
            db.session.commit()

            return family_core_data
        except Exception as e:
            return {'msg': 'Data could not be stored'}
