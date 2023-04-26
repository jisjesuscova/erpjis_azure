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
