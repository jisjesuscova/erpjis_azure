from app.models.models import YearModel

class Year:
    def get():
        years = YearModel.query.all()
        return years