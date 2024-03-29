from flask import request
from app import db
from app.models.models import UserModel, TotalMeshDatumModel
from sqlalchemy import func

class TotalMeshDatum():
    @staticmethod
    def get(rut = '', period = ''):
        if rut != '' and period != '':
            total_mesh_data = TotalMeshDatumModel.query.filter_by(rut=rut, period=period).all()
        else:
            total_mesh_data = (
                TotalMeshDatumModel.query
                .with_entities(
                    TotalMeshDatumModel.document_employee_id,
                    TotalMeshDatumModel.rut,
                    TotalMeshDatumModel.period
                )
                .group_by(
                    TotalMeshDatumModel.document_employee_id,
                    TotalMeshDatumModel.rut,
                    TotalMeshDatumModel.period
                )
                .all()
            )

        return total_mesh_data
    
    @staticmethod
    def get_by_period(period = '', page = ''):
        total_mesh_data = TotalMeshDatumModel.query.join(UserModel, TotalMeshDatumModel.rut == UserModel.rut).filter(TotalMeshDatumModel.period == period).paginate(page=page, per_page=20, error_out=False)

        return total_mesh_data
    
    @staticmethod
    def get_by_rut(rut = ''):
        total_mesh_data = db.session.query(
            TotalMeshDatumModel.rut,
            TotalMeshDatumModel.period
        ).filter_by(rut=rut).group_by(TotalMeshDatumModel.rut, TotalMeshDatumModel.period).all()

        return total_mesh_data
    
    @staticmethod
    def get_one(rut = '', period = ''):
        total_mesh_datum = TotalMeshDatumModel.query.filter_by(rut=rut, period=period).first()

        return total_mesh_datum
    
    @staticmethod
    def delete(rut, period):
        total_mesh_data = TotalMeshDatumModel.query.filter_by(rut=rut, period = period).all()

        for total_mesh_datum in total_mesh_data:
            total_mesh_datum = TotalMeshDatumModel.query.filter_by(id=total_mesh_datum.id).first()

            db.session.delete(total_mesh_datum)
            db.session.commit()
