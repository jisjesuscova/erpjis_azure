from app.models.models import ClockModel, BranchOfficeModel
from app import db
from datetime import datetime
from sqlalchemy import cast, DateTime

class Clock():
    @staticmethod
    def get(page):
        clock_data = db.session.query(ClockModel.id, ClockModel.sn, BranchOfficeModel.branch_office, ClockModel.ip, ClockModel.updated_date)\
                        .join(BranchOfficeModel, ClockModel.branch_office_id == BranchOfficeModel.id)\
                        .paginate(page=page, per_page=20, error_out=False)

        return clock_data

    @staticmethod
    def delete(id):
        clock = ClockModel.query.filter_by(id=id).first()

        db.session.delete(clock)
        try:
            db.session.commit()

            return clock
        except Exception as e:
            return {'msg': 'Data could not be stored'}
        
    @staticmethod
    def check(data):
        quantity = ClockModel.query.filter_by(sn=data['sn']).count()

        return quantity

    @staticmethod
    def update(data):
        clock = ClockModel.query.filter_by(sn = data['sn']).first()
        clock.branch_office_id = data['branch_office_id']
        clock.ip = data['ip']
        clock.sn = data['sn']
        clock.updated_date = datetime.now()

        db.session.add(clock)
        db.session.commit()

        return str(data['uid']) + "_" + str(data['rut']) + "_" + str(data['full_name']) + "_" + str(data['privilege'])

    def store(data):
        clock = ClockModel()
        clock.branch_office_id = data['branch_office_id']
        clock.ip = data['ip']
        clock.sn = data['sn']
        clock.added_date = datetime.now()
        clock.updated_date = datetime.now()

        db.session.add(clock)
        db.session.commit()
        
        return str(data['branch_office_id']) + "_" + str(data['ip']) + "_" + str(data['sn'])
 