from app.models.models import RolModel

class Rol():
    def get(id):
        rol = RolModel.query.filter_by(id=id).first()

        return rol