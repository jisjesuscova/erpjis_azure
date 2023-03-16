from app.models.models import CheckModel, BranchOfficeModel, CheckGroupQuestionDetailModel, CheckQuestionModel, CheckGroupQuestionModel
from app import db
from app.helpers.helper import Helper

class Check():
    @staticmethod
    def get(id = '', page = ''):
        if id != '':
            check = CheckModel.query.filter_by(id=id).first()

            return check
        else:
            checks = CheckGroupQuestionModel.query.order_by(CheckGroupQuestionModel.added_date.desc()).paginate(page=page, per_page=20, error_out=False)

            return checks
    
    @staticmethod
    def store(data):
        date = Helper.create_date(data['month'], data['year'])

        check = CheckModel()
        check.branch_office_id = data['branch_office_id']
        check.check_title = data['check_title']
        check.added_date = date

        db.session.add(check)
        try:
            db.session.commit()

            return check
        except Exception as e:
            return {'msg': 'Data could not be stored'}
        
    @staticmethod
    def delete(id):
        check = CheckModel.query.filter_by(id=id).first()

        db.session.delete(check)
        try:
            db.session.commit()

            return check
        except Exception as e:
            return {'msg': 'Data could not be stored'}