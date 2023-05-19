from flask import request
from app.models.models import ControlClockNoMarkModel
from app import db
from datetime import datetime
from sqlalchemy import func

class ControlClockNoMark():
    @staticmethod
    def get(rut = ''):
        control_clock_no_marks = ControlClockNoMarkModel.query.filter_by(rut=rut,status_id=0).all()

        return control_clock_no_marks
    
    @staticmethod
    def get_by_id(id = ''):
        control_clock_no_mark = ControlClockNoMarkModel.query.with_entities(
            func.date_format(ControlClockNoMarkModel.added_date, '%d-%m-%Y').label('added_date'),
            ControlClockNoMarkModel.rut,
            ControlClockNoMarkModel.punch,
            ControlClockNoMarkModel.id
        ).filter_by(id=id).first()

        return control_clock_no_mark
    
    @staticmethod
    def store(rut, punch):
        control_clock_no_mark = ControlClockNoMarkModel()
        control_clock_no_mark.status_id = 0
        control_clock_no_mark.rut = rut
        control_clock_no_mark.punch = punch
        control_clock_no_mark.added_date = datetime.now()
        control_clock_no_mark.updated_date = datetime.now()

        db.session.add(control_clock_no_mark)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0


    @staticmethod
    def update(id, mark_date):
        control_clock_no_mark = ControlClockNoMarkModel.query.filter_by(id=id).first()
        control_clock_no_mark.status_id = 1
        control_clock_no_mark.mark_date = mark_date

        db.session.add(control_clock_no_mark)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0