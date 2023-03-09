from app.models.models import CheckModel, CheckGroupQuestionDetailModel, CheckQuestionModel
from app import db
from datetime import datetime
from app.helpers.helper import Helper

class CheckQuestion():
    @staticmethod
    def get(id = ''):
        check_questions = CheckQuestionModel.query\
                                .join(CheckModel, CheckModel.id == CheckQuestionModel.check_id)\
                                .filter(CheckQuestionModel.check_id==id)\
                                .add_columns(CheckQuestionModel.question, CheckModel.check_title, CheckQuestionModel.id).all()

        return check_questions

    @staticmethod
    def delete(id):
        check = CheckQuestionModel.query.filter_by(check_id=id).first()

        db.session.delete(check)
        try:
            db.session.commit()

            return check
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def group_questions(id, check_group_question_id):
        check_group_question_details = CheckGroupQuestionDetailModel.query.filter_by(check_group_question_id=check_group_question_id).all()

        for check_group_question_detail in check_group_question_details:
            check_question = CheckQuestionModel()
            check_question.check_id = id
            check_question.question = check_group_question_detail.question
            check_question.added_date = datetime.now()
            check_question.updated_date = datetime.now()

            db.session.add(check_question)
            db.session.commit()
        return 1