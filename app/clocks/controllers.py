from flask import Blueprint, request
from app.clocks.clock import Clock

clock = Blueprint("clocks", __name__)

@clock.route("/clock/data", methods=['GET', 'POST'])
def store():
   status = Clock.check(request.form)
   
   if status == 0:
      data = Clock.store(request.form)
   else:
      data = Clock.update(request.form)

   return str(data)