from flask import request
from app.models.models import NewModel
from app import db
from datetime import datetime
import markdown
from app.helpers.helper import Helper

class New():
    @staticmethod
    def get(id = '', page = ''):
        if id == '' and page == '':
            news = NewModel.query.order_by(NewModel.added_date.desc()).all()

            return news
        else:
            if id != '':
                new = NewModel.query.filter_by(id=id).first()

                return new
            else:
                news = NewModel.query.order_by(NewModel.added_date.desc()).paginate(page=page, per_page=10, error_out=False)

                return news

    @staticmethod
    def store(data, picture):
        description = Helper.remove_from_string("#", data['description'])
        description = Helper.remove_from_string("##", description)
        description = Helper.remove_from_string("###", description)
        description = Helper.remove_from_string("####", description)
        description = Helper.remove_from_string("#####", description)
        description = Helper.remove_from_string("######", description)
        description = Helper.remove_from_string("#######", description)
        description = Helper.remove_from_string("**", description)

        new = NewModel()
        new.title = data['title']
        new.description = description
        new.markdown_description = markdown.markdown(data['description'])
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
    def delete(id):
        new = NewModel.query.filter_by(id = id).first()

        db.session.delete(new)
        if db.session.commit():
            return new
        else:
            return {'msg': 'Data could not be stored'}

