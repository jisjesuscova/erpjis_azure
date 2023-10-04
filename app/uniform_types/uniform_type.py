from flask import request
from app.models.models import UniformTypeModel

class UniformType():
    @staticmethod
    def get():
        uniform_types = UniformTypeModel.query.order_by(UniformTypeModel.uniform_type).all()

        return uniform_types