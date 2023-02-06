from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.news.new import New

home = Blueprint("home", __name__)

@home.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@home.route("/home", methods=['GET'])
def index():
   news = New.get()

   if current_user.rol_id == 1:
      return render_template('collaborator/home/index.html')
   elif current_user.rol_id == 2:
      return render_template('incharge/home/index.html')
   elif current_user.rol_id == 3:
      return render_template('supervisor/home/index.html')
   elif current_user.rol_id == 4:
      return render_template('administrator/home/index.html', news = news)