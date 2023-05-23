from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.clocks.clock import Clock
from app.control_clock_no_marks.control_clock_no_mark import ControlClockNoMark
from app.helpers.helper import Helper

clock = Blueprint("clocks", __name__)

@clock.route("/clock_data", methods=['GET'])
def index(page = 1):
   clock_data = Clock.get(page)

   title = 'Relojes'

   module_name = 'Gestión Tiempo'

   return render_template('human_resource/clocks/clock_data.html', clock_data = clock_data, title = title, module_name = module_name)

@clock.route("/clock/data", methods=['GET', 'POST'])
def store():
   status = Clock.check(request.form)
   
   if status == 0:
      data = Clock.store(request.form)
   else:
      data = Clock.update(request.form)

   return str(data)

@clock.route("/clock/delete/<int:id>", methods=['GET'])
def delete(id):
   Clock.delete(id)

   flash("El reloj ha sido borrado con éxito.", "success")

   return redirect(url_for('clocks.index'))

@clock.route("/clock_data/create/<int:id>", methods=['GET'])
def create(id):
   clock_no_mark = ControlClockNoMark.get_by_id(id)

   return render_template('collaborator/clocks/create_mark_data.html', clock_no_mark = clock_no_mark)

@clock.route("/clock_data/review/<int:id>", methods=['GET'])
def review(id):
   clock_no_mark = ControlClockNoMark.get_by_id(id)

   date = Helper.split(str(clock_no_mark.mark_date), ' ')

   time = date[1]

   return render_template('human_resource/clocks/review_mark_data.html', clock_no_mark = clock_no_mark, time = time)
