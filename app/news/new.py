from flask import request
from app.models.models import NewModel
from app import db
from datetime import datetime

class New():
    @staticmethod
    def get(id = '', page = ''):
        if id == '' and page == '':
            news = NewModel.query.all()

            return news
        else:
            if id != '':
                new = NewModel.query.filter_by(id=id).first()

                return new
            else:
                news = NewModel.query.order_by('added_date').paginate(page=page, per_page=10, error_out=False)

                return news

    @staticmethod
    def store(data, picture):
        new = NewModel()
        new.title = data['title']
        new.description = data['description']
        new.picture = picture
        new.added_date = datetime.now()
        new.updated_date = datetime.now()

        db.session.add(new)
        try:
            db.session.commit()

            return new
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def update(data, id):
        numeric_rut = Helper.numeric_rut(data['rut'])
        nickname = Helper.nickname(data['names'], data['father_lastname'])

        employee = EmployeeModel.query.filter_by(rut = id).first()
        employee.rut = id
        employee.visual_rut = data['rut']
        employee.names = data['names']
        employee.father_lastname = data['father_lastname']
        employee.mother_lastname = data['mother_lastname']
        employee.nickname = nickname
        employee.gender_id = data['gender_id']
        employee.nationality_id = data['nationality_id']
        employee.cellphone = data['cellphone']
        employee.personal_email = data['personal_email']
        employee.born_date = data['born_date']
        employee.updated_date = datetime.now()

        db.session.add(employee)
        if db.session.commit():
            return employee
        else:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def delete(id):
        new = NewModel.query.filter_by(id = id).first()

        db.session.delete(new)
        if db.session.commit():
            return new
        else:
            return {'msg': 'Data could not be stored'}

