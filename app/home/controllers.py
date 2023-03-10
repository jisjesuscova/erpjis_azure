from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.news.new import New
from app.employees.employee import Employee
from datetime import datetime
import locale

home = Blueprint("home", __name__)

@home.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@home.route("/home", methods=['GET'])
def index():
   news = New.get()
   birthdays = Employee.get_birthdays()
   birthday_quantities = Employee.get_birthday_quantities()
   locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
   current_month = datetime.today().month
   current_month = datetime(2000, current_month, 1).strftime('%B').capitalize()

   if current_user.rol_id == 1:
      return render_template('collaborator/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 2:
      return render_template('incharge/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 3:
      return render_template('supervisor/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 4:
      return render_template('administrator/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)