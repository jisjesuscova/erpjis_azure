from app.models.models import HrFinalDayMonthModel

class HrFinalDayMonth():
    def get(month):
        hr_final_day_month = HrFinalDayMonthModel.query.filter_by(id=month).first()

        return hr_final_day_month