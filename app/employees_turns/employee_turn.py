from app.models.models import PreEmployeeTurnModel
from app import db
from sqlalchemy import inspect
from datetime import datetime
from app.helpers.helper import Helper
from app.turns.turn import Turn

class EmployeeTurn():
    def delete_old_ones(rut):
        employees_turns = PreEmployeeTurnModel.query.filter_by(rut = rut).all()

        for employee_turn in employees_turns:
            employee_turn_detail = PreEmployeeTurnModel.query.filter_by(id = employee_turn.id).first()

            db.session.delete(employee_turn_detail)
            db.session.commit()

    def get(data):
        pre_employee_turn = PreEmployeeTurnModel.query.filter_by(turn_id = data['turn_id'], rut = data['employee_id'], start_date = data['start_date']).all()

        return pre_employee_turn

    def get_all_by_rut(rut):
        pre_employee_turns = PreEmployeeTurnModel.query.filter_by(rut = rut).all()

        return pre_employee_turns
    
    def get_quantity(rut):
        qty = PreEmployeeTurnModel.query.filter_by(rut = rut).count()

        return qty
    
    @staticmethod
    def update(data):
        turn = Turn.get(data['turn_id'])

        end_date = Helper.get_last_date(data['start_date'], turn.group_day_id)
            
        turn = PreEmployeeTurnModel.query.filter_by(id=data['id']).first()
        turn.turn_id = data['turn_id']
        turn.rut = data['employee_id']
        turn.start_date = data['start_date']
        turn.end_date = end_date
        turn.updated_date = datetime.now()
        inspection = inspect(turn)

        db.session.add(turn)
        status = inspection.pending
        db.session.commit()
        return status
        
    @staticmethod
    def pre_store(data):
        
        quantity = EmployeeTurn.get_quantity(data['employee_id'])
        turn = Turn.get(data['turn_id'])
        period = Helper.get_period(data['month'], data['year'])
        print(data['turn_id'])
        if data['turn_id'] != '0':
            end_date = Helper.get_last_date(data['start_date'], turn.group_day_id)
            validate_status_start_date = Helper.validate_current_month(data['start_date'])
            validate_status_end_date = Helper.validate_current_month(end_date)
        else:
            validate_status_start_date = Helper.validate_current_month(data['start_date'])
            validate_status_end_date = 0
        print(quantity)
        print(validate_status_start_date)
        if quantity == 0 and validate_status_start_date == 1:
            turn = Turn.get(data['turn_id'])

            end_date = Helper.get_last_date(data['start_date'], turn.group_day_id)
            start_date = Helper.split(end_date, "-")

            first_day_current_month = start_date[0] + '-' + start_date[1] + '-01'
           
            compare_date = Helper.compare_dates(first_day_current_month, end_date)

            if compare_date == 0:
                pre_employee_turn = PreEmployeeTurnModel()
                pre_employee_turn.turn_id = data['turn_id']
                pre_employee_turn.rut = data['employee_id']
                pre_employee_turn.start_date = first_day_current_month
                pre_employee_turn.end_date = end_date
                pre_employee_turn.period = period
                pre_employee_turn.added_date = datetime.now()
                pre_employee_turn.updated_date = datetime.now()
                inspection = inspect(pre_employee_turn)

                db.session.add(pre_employee_turn)
                status = inspection.pending
                db.session.commit()
                return status
            else:
                return 0
        elif quantity > 0 and validate_status_end_date == 1:
            start_date_detail = Helper.split(data['start_date'], " ")
            start_month = Helper.split(start_date_detail[0], "-")
            period_month = Helper.split(period, "-")

            if start_month[1] == period_month[0]:
                turn = Turn.get(data['turn_id'])

                end_date = Helper.get_last_day_of_month(str(data['start_date']))

                pre_employee_turn = PreEmployeeTurnModel()
                pre_employee_turn.turn_id = data['turn_id']
                pre_employee_turn.rut = data['employee_id']
                pre_employee_turn.start_date = data['start_date']
                pre_employee_turn.end_date = end_date
                pre_employee_turn.period = period
                pre_employee_turn.added_date = datetime.now()
                pre_employee_turn.updated_date = datetime.now()
                inspection = inspect(pre_employee_turn)

                db.session.add(pre_employee_turn)
                status = inspection.pending
                db.session.commit()
                return status
        else:
            start_date_detail = Helper.split(data['start_date'], " ")
            start_month = Helper.split(start_date_detail[0], "-")
            period_month = Helper.split(period, "-")

            if start_month[1] == period_month[0]:
                if data['turn_id'] == '0':
                    pre_employee_turn = PreEmployeeTurnModel()
                    pre_employee_turn.turn_id = 0
                    pre_employee_turn.rut = data['employee_id']
                    pre_employee_turn.start_date = data['start_date']
                    pre_employee_turn.end_date = data['start_date']
                    pre_employee_turn.period = period
                    pre_employee_turn.added_date = datetime.now()
                    pre_employee_turn.updated_date = datetime.now()
                    inspection = inspect(pre_employee_turn)

                    db.session.add(pre_employee_turn)
                    status = inspection.pending
                    db.session.commit()
                    return status
                else:
                    turn = Turn.get(data['turn_id'])

                    end_date = Helper.get_last_date(data['start_date'], turn.group_day_id)

                    pre_employee_turn = PreEmployeeTurnModel()
                    pre_employee_turn.turn_id = data['turn_id']
                    pre_employee_turn.rut = data['employee_id']
                    pre_employee_turn.start_date = data['start_date']
                    pre_employee_turn.end_date = end_date
                    pre_employee_turn.period = period
                    pre_employee_turn.added_date = datetime.now()
                    pre_employee_turn.updated_date = datetime.now()
                    inspection = inspect(pre_employee_turn)

                    db.session.add(pre_employee_turn)
                    status = inspection.pending
                    db.session.commit()
                    return status