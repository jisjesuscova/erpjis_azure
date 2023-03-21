from flask import Blueprint, request
from app.clock_fingers.clock_finger import ClockFinger
import json

clock_finger = Blueprint("clock_fingers", __name__)

@clock_finger.route("/clock_finger/data", methods=['GET', 'POST'])
def data():
   status = ClockFinger.check(request.form)
   
   if status == 0:
      data = ClockFinger.store(request.form)
   else:
      data = ClockFinger.update(request.form)
   
   return str(data)

@clock_finger.route("/clock_finger", methods=['GET'])
def index():
   
   data = ClockFinger.get()

   res = ClockFinger.to_json(data)

   return json.dumps(res)