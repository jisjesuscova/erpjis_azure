from app.models.models import CheckGroupQuestionModel

class CheckGroupQuestion():
    @staticmethod
    def get(id = ''):
        if id != '':
            check_group_questions = CheckGroupQuestionModel.query.all()

            return check_group_questions
        else:
            check_group_questions = CheckGroupQuestionModel.query.all()

            return check_group_questions
