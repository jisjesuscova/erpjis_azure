from app.models.models import CheckGroupQuestionModel

class CheckGroupQuestion():
    @staticmethod
    def get():
        check_group_questions = CheckGroupQuestionModel.query.all()

        return check_group_questions
