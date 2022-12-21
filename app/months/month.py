from app.models.models import MonthModel

class Month:
    def get():
        months = MonthModel.query.all()
        return months