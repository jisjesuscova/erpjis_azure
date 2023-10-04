from app.models.models import CheckModel, CheckGroupQuestionDetailModel, CheckQuestionModel, CheckAnswerModel
from app import db
from datetime import datetime
from app.helpers.file import File
from app.dropbox_data.dropbox import Dropbox

class CheckQuestion():
    @staticmethod
    def get(id = ''):
        check_questions = CheckQuestionModel.query\
                                .join(CheckModel, CheckModel.id == CheckQuestionModel.check_id)\
                                .filter(CheckQuestionModel.check_id==id)\
                                .add_columns(CheckQuestionModel.status_id, CheckQuestionModel.check_id, CheckQuestionModel.question, CheckModel.check_title, CheckQuestionModel.id).all()

        return check_questions

    @staticmethod
    def status(id = ''):
        check_question = CheckQuestionModel.query.filter_by(id=id).first()

        return check_question.status_id

    @staticmethod
    def get_filter_by(id = '', check_id = ''):
        if id != '':
            check_question = CheckQuestionModel.query\
                                .join(CheckModel, CheckModel.id == CheckQuestionModel.check_id)\
                                .filter(CheckQuestionModel.id==id)\
                                .add_columns(CheckQuestionModel.check_id, CheckQuestionModel.question, CheckModel.check_title, CheckQuestionModel.id).first()
        else:
            check_question = CheckQuestionModel.query\
                                .join(CheckModel, CheckModel.id == CheckQuestionModel.check_id)\
                                .filter(CheckQuestionModel.check_id==check_id)\
                                .add_columns(CheckQuestionModel.check_id, CheckQuestionModel.question, CheckModel.check_title, CheckQuestionModel.id).first()

        return check_question
    
    @staticmethod
    def delete(id):
        check_questions = CheckQuestionModel.query.filter_by(check_id=id).all()

        for check_question in check_questions:
            check_answers = CheckAnswerModel.query.filter_by(check_question_id=check_question.id).all()

            check_question_delete = CheckQuestionModel.query.filter_by(id=check_question.id).first()
            db.session.delete(check_question_delete)
            db.session.commit()

            for check_answer in check_answers:
                check_answer_delete = CheckAnswerModel.query.filter_by(id=check_answer.id).first()
                Dropbox.delete('/checks/', check_answer_delete.support)
                File.delete("app/static/dist/files/check_data/", check_answer_delete.support)
    
                db.session.delete(check_answer_delete)
                db.session.commit()

        return 1

    @staticmethod
    def group_questions(id, check_group_question_id):
        check_group_question_details = CheckGroupQuestionDetailModel.query.filter_by(check_group_question_id=check_group_question_id).all()

        for check_group_question_detail in check_group_question_details:
            check_question = CheckQuestionModel()
            check_question.check_id = id
            check_question.status_id = 1
            check_question.question = check_group_question_detail.question
            check_question.added_date = datetime.now()
            check_question.updated_date = datetime.now()

            db.session.add(check_question)
            db.session.commit()
        return 1

    @staticmethod
    def update(id, status_id):
        check_question = CheckQuestionModel.query.filter_by(id = id).first()
        check_question.status_id = status_id
        check_question.updated_date = datetime.now()

        db.session.add(check_question)
        if db.session.commit():
            return check_question
        else:
            return {'msg': 'Data could not be stored'}