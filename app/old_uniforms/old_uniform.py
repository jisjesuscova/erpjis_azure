from flask import request
from app.models.models import OldUniformModel
from app import db
from datetime import datetime

class OldUniform():
    @staticmethod
    def get(rut):
        old_uniforms = OldUniformModel.query.filter_by(rut=rut).all()

        return old_uniforms