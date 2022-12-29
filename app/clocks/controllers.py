from flask import Blueprint, request
from app.clocks.clock import Clock

clock = Blueprint("clocks", __name__)

@clock.route("/clock/store", methods=['GET', 'POST'])
def store():
   
   data = Clock.store(request.form)

   return str(data)