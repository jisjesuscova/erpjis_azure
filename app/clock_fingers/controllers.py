from flask import Blueprint, request
from app.clock_fingers.clock_finger import ClockFinger

clock_finger = Blueprint("clock_fingers", __name__)

@clock_finger.route("/clock_finger/store", methods=['GET', 'POST'])
def store():
   
   data = ClockFinger.store(request.form)

   return str(data)