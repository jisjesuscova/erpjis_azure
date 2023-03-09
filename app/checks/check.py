from app.models.models import CheckModel, BranchOfficeModel, CheckGroupQuestionDetailModel, CheckQuestionModel
from app import db
from app.helpers.helper import Helper

class Check():
    @staticmethod
    def get(id = '', page = ''):
        if id != '':
            check = CheckModel.query.filter_by(id=id).first()

            return check
        else:
            checks = CheckModel.query\
                                .join(BranchOfficeModel, BranchOfficeModel.id == CheckModel.branch_office_id)\
                                .add_columns(CheckModel.added_date, CheckModel.check_title, CheckModel.id, BranchOfficeModel.branch_office).order_by(CheckModel.added_date.desc()).paginate(page=page, per_page=20, error_out=False)

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