from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need, db
from app.news.new import New
from app.dropbox_data.dropbox import Dropbox
from app.helpers.file import File
from app.helpers.whatsapp import Whatsapp
from app.whatsapp_groups.whatsapp_group import WhatsappGroup
from app.comments.comment import Comment
from markupsafe import Markup

new = Blueprint("news", __name__)

@new.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@new.route("/publicities/news", methods=['GET'])
def index(page=1):
   news = New.get('', page)

   return render_template('designer/publicities/news/news.html', news = news)

@new.route("/publicities/new/show/<int:id>", methods=['GET'])
def show(id):
   new = New.get(id)

   description = Markup(new.markdown_description)

   comments = Comment.get(id)
   
   if current_user.rol_id == 1:
      return render_template('collaborator/publicities/news/new_show.html', description = description, new = new, comments = comments)
   elif current_user.rol_id == 2:
      return render_template('incharge/publicities/news/new_show.html', description = description, new = new, comments = comments)
   elif current_user.rol_id == 3:
      return render_template('supervisor/publicities/news/new_show.html', description = description, new = new, comments = comments)
   elif current_user.rol_id == 4:
      return render_template('human_resource/publicities/news/new_show.html', description = description, new = new, comments = comments)
   elif current_user.rol_id == 5:
      return render_template('designer/publicities/news/new_show.html', description = description, new = new, comments = comments)

@new.route("/publicities/new/create", methods=['GET'])
def create():
   whatsapp_groups = WhatsappGroup.get()
   title = "Crear Noticia"
   module_name = "Publicidades"
   
   return render_template('designer/publicities/news/new_create.html', title = title, module_name = module_name, whatsapp_groups = whatsapp_groups)

@new.route("/publicities/new/store", methods=['POST'])
def store():
   picture = Dropbox.upload('nueva', '_noticia', request.files, "/blogs/", "app/static/dist/files/new_data/")
   
   new = New.store(request.form, picture)
   Whatsapp.send(new.id, request.form['send_whatsapp'], request.form['group_id'], 4)

   flash('Se ha publicado la noticia')

   return redirect(url_for('news.index'))

@new.route("/publicities/new/delete/<int:id>", methods=['GET'])
def delete(id):
   new = New.get(id)
   New.delete(id)
   Dropbox.delete('/blogs/', new.picture)
   File.delete('/app/static/dist/files/new_data/', new.picture)

   return redirect(url_for('news.index'))