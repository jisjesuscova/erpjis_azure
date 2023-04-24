from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import app, regular_employee_rol_need
from app.news.new import New
from app.employees.employee import Employee
from datetime import datetime
from app.helpers.helper import Helper
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.vacations.vacation import Vacation
from app.documentation_titles.documentation_title import DocumentationTitle

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
   gender_totals = Employee.gender_totals()
   distribution_totals = EmployeeLaborDatum.distribution_totals()
   active_employee_total = Employee.active_employee_total()
   total_vacations = Vacation.calculate_total_vacation_days()
   documentation_titles_menu = DocumentationTitle.get()

   if current_user.rol_id == 1:
      return render_template('collaborator/home/index.html', documentation_titles_menu = documentation_titles_menu, current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 2:
      return render_template('incharge/home/index.html', documentation_titles_menu = documentation_titles_menu, current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 3:
      return render_template('supervisor/home/index.html', documentation_titles_menu = documentation_titles_menu, current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 4:
      return render_template('human_resource/home/index.html', documentation_titles_menu = documentation_titles_menu, total_vacations = total_vacations, active_employee_total = active_employee_total, distribution_totals = distribution_totals, gender_totals = gender_totals, current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 5:
      return render_template('designer/home/index.html', documentation_titles_menu = documentation_titles_menu, total_vacations = total_vacations, active_employee_total = active_employee_total, distribution_totals = distribution_totals, gender_totals = gender_totals, current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)
   elif current_user.rol_id == 6:
      return render_template('management/home/index.html', documentation_titles_menu = documentation_titles_menu, total_vacations = total_vacations, active_employee_total = active_employee_total, distribution_totals = distribution_totals, gender_totals = gender_totals, current_month = current_month, news = news, birthdays = birthdays, birthday_quantities = birthday_quantities)