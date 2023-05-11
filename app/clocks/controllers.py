from flask import Blueprint, request, render_template, redirect, url_for, flash, session, jsonify
from app.clocks.clock import Clock

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