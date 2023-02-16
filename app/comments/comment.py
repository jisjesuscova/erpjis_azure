from flask import request
from flask_login import current_user
from app.models.models import CommentModel, EmployeeModel
from app import db
from datetime import datetime

class Comment():
    @staticmethod
    def get(new_id):
        comments = CommentModel.query\
                            .join(EmployeeModel, EmployeeModel.rut == CommentModel.rut)\
                            .filter(CommentModel.new_id==new_id)\
                            .order_by(CommentModel.added_date)\
                            .add_columns(CommentModel.added_date, CommentModel.comment, CommentModel.new_id, CommentModel.id, EmployeeModel.picture).all()

        return comments

    @staticmethod
    def store(data):
        comment = CommentModel()
        comment.new_id = data['new_id']
        comment.rut = current_user.rut
        comment.comment = data['comment']
        comment.added_date = datetime.now()
        comment.updated_date = datetime.now()

        db.session.add(comment)
        try:
            db.session.commit()

            return comment
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def delete(id):
        comment = CommentModel.query.filter_by(id=id).first()

        db.session.delete(comment)
        try:
            db.session.commit()

            return comment
        except Exception as e:
            return {'msg': 'Data could not be stored'}