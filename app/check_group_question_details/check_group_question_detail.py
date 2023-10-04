from app.models.models import CheckGroupQuestionDetailModel, CheckAnswerModel
from app import db
from datetime import datetime

class CheckGroupQuestionDetail():
    @staticmethod
    def get(id = ''):
        if id != '':
            check_group_question_details = CheckGroupQuestionDetailModel.query.filter_by(check_group_question_id=id).all()

            return check_group_question_details
        else:
            check_group_question_details = CheckGroupQuestionDetailModel.query.all()

            return check_group_question_details

    @staticmethod
    def quantity(id = ''):
        check_group_question_detail_quantity = CheckGroupQuestionDetailModel.query.filter_by(check_group_question_id=id).count()

        return check_group_question_detail_quantity
        
    @staticmethod
    def store(data, id, support = ''):
        check_answer = CheckAnswerModel()
        check_answer.check_group_question_id = data['check_group_question_id']
        check_answer.check_group_question_detail_id = data['check_group_question_detail_id']
        check_answer.branch_office_id = data['branch_office_id']
        check_answer.answer_id = data['answer_id']
        check_answer.description = data['description']
        check_answer.support = support
        check_answer.added_date = data['added_date'] + ' 00:00:00'

        db.session.add(check_answer)
        if db.session.commit():
            return check_answer
        else:
            return {'msg': 'Data could not be stored'}