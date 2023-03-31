from app.models.models import HrSettingsModel

class HrSetting():
    def get():
        hr_setting = HrSettingsModel.query.first()

        return hr_setting