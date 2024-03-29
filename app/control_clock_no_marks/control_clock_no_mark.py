from flask import request
from app.models.models import ControlClockNoMarkModel, EmployeeLaborDatumModel, BranchOfficeModel, SupervisorModel, UserModel
from app import db
from datetime import datetime
from sqlalchemy import func
from flask_login import current_user

class ControlClockNoMark():
    @staticmethod
    def get(rut = ''):
        if rut != '':
            control_clock_no_marks = ControlClockNoMarkModel.query.filter_by(rut=rut,status_id=0).all()
        else:
            control_clock_no_marks = ControlClockNoMarkModel.query\
                                    .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == ControlClockNoMarkModel.rut)\
                                    .join(UserModel, UserModel.rut == EmployeeLaborDatumModel.rut)\
                                    .join(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id)\
                                    .join(SupervisorModel, SupervisorModel.branch_office_id == BranchOfficeModel.id)\
                                    .add_columns(UserModel.visual_rut, UserModel.nickname, ControlClockNoMarkModel.id, ControlClockNoMarkModel.punch, ControlClockNoMarkModel.added_date).filter(ControlClockNoMarkModel.status_id==1, SupervisorModel.rut == current_user.rut).all()

            return control_clock_no_marks
    
    @staticmethod
    def get_first(rut):
        control_clock_no_mark = ControlClockNoMarkModel.query.filter_by(rut=rut).first()

        return control_clock_no_mark
    
    @staticmethod
    def get_by_id(id = ''):
        control_clock_no_mark = ControlClockNoMarkModel.query.with_entities(
            func.date_format(ControlClockNoMarkModel.added_date, '%d-%m-%Y').label('added_date'),
            ControlClockNoMarkModel.rut,
            ControlClockNoMarkModel.punch,
            ControlClockNoMarkModel.mark_date,
            ControlClockNoMarkModel.id
        ).filter_by(id=id).first()

        return control_clock_no_mark
    
    @staticmethod
    def store(rut = '', punch = '', date = ''):
        control_clock_no_mark = ControlClockNoMarkModel()
        control_clock_no_mark.status_id = 0
        control_clock_no_mark.rut = rut
        control_clock_no_mark.punch = punch
        if date == '':
            control_clock_no_mark.added_date = datetime.now()
            control_clock_no_mark.updated_date = datetime.now()
        else:
            control_clock_no_mark.added_date = date
            control_clock_no_mark.updated_date = date

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
        
    
    @staticmethod
    def update_status(id, status):
        control_clock_no_mark = ControlClockNoMarkModel.query.filter_by(id=id).first()
        control_clock_no_mark.status_id = status
        db.session.add(control_clock_no_mark)
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0
        
    @staticmethod
    def delete(id):
        control_clock_no_mark = ControlClockNoMarkModel.query.filter_by(id=id).first()

        db.session.delete(control_clock_no_mark)
        try:
            db.session.commit()

            return control_clock_no_mark
        except Exception as e:
            return {'msg': 'Data could not be stored'}