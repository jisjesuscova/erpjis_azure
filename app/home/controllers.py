from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.news.new import New
from app.employees.employee import Employee
from datetime import datetime
from app.helpers.helper import Helper

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
   current_month = datetime.today().month
   current_month = Helper.month_name(current_month)

   if current_user.rol_id == 1:
      return render_template('collaborator/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 2:
      return render_template('incharge/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 3:
      return render_template('supervisor/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 4:
      return render_template('administrator/home/index.html', current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)