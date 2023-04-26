from flask import request
from app import db
from app.models.models import MeshDatumModel, TotalMeshDatumModel

class TotalMeshDatum():
    @staticmethod
    def get():
        total_mesh_data = (
            TotalMeshDatumModel.query
            .with_entities(
                TotalMeshDatumModel.rut,
                TotalMeshDatumModel.period
            )
            .group_by(
                TotalMeshDatumModel.rut,
                TotalMeshDatumModel.period
            )
            .all()
        )

        return total_mesh_data
    
    @staticmethod
    def store(data):
        total_mesh_datum = TotalMeshDatumModel()
        total_mesh_datum.rut = rut
        total_mesh_datum.total_hours = total
        db.session.add(total_mesh_datum)
        db.session.commit()

        return 1
    
    @staticmethod
    def delete(rut, period):
        total_mesh_data = TotalMeshDatumModel.query.filter_by(rut=rut, period = period).all()

        for total_mesh_datum in total_mesh_data:
            total_mesh_datum = TotalMeshDatumModel.query.filter_by(id=total_mesh_datum.id).first()

            db.session.delete(total_mesh_datum)
            db.session.commit()
