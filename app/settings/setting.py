from app.models.models import SettingModel

class Setting():
    @staticmethod
    def get():
        settings = SettingModel.query.filter_by(id=1).first()

        return settings