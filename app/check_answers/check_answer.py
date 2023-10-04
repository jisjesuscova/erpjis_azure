from app.models.models import CheckAnswerModel
from app import db
from datetime import datetime

class CheckAnswer():
    @staticmethod
    def get(check_question_id):
        check_answer = CheckAnswerModel.query.filter_by(check_question_id=check_question_id).first()

        return check_answer
        
    @staticmethod
    def store(data, support):
        check_answer = CheckAnswerModel()
        check_answer.check_id = data['check_id']
        check_answer.check_question_id = data['check_question_id']
        check_answer.answer_id = data['answer_id']
        check_answer.description = data['description']
        check_answer.support = support
        check_answer.added_date = datetime.now()

        db.session.add(check_answer)
        try:
            db.session.commit()

            return check_answer
        except Exception as e:
            return {'msg': 'Data could not be stored'}
        
    @staticmethod
    def update(data, support):
        check_answer = CheckAnswerModel.query.filter_by(check_question_id=data['check_question_id']).first()
        check_answer.check_id = data['check_id']
        check_answer.check_question_id = data['check_question_id']
        check_answer.answer_id = data['answer_id']
        check_answer.description = data['description']
        check_answer.support = support
        check_answer.updated_date = datetime.now()

        db.session.add(check_answer)
        try:
            db.session.commit()

            return check_answer
        except Exception as e:
            return {'msg': 'Data could not be stored'}