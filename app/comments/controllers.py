from flask import Blueprint, redirect, request, url_for, flash
from flask_login import login_required
from app import app, regular_employee_rol_need, db
from app.news.new import New
from app.dropbox_data.dropbox import Dropbox
from app.helpers.file import File
from app.comments.comment import Comment

comment = Blueprint("comments", __name__)

@comment.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@comment.route("/comment/store", methods=['POST'])
def store():
   Comment.store(request.form)

   flash('Se ha comentado la noticia', 'success')

   return redirect(url_for('news.show', id=request.form['new_id']))

@comment.route("/comment/delete/<int:id>/<int:new_id>", methods=['GET'])
def delete(id, new_id):
   Comment.delete(id)

   flash('Se ha borrado el comentario', 'success')

   return redirect(url_for('news.show', id=new_id))