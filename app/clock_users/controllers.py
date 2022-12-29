from flask import Blueprint, request
from app.clock_users.clock_user import ClockUser
from app.helpers.helper import Helper
from flask import jsonify
import json

clock_user = Blueprint("clock_users", __name__)

@clock_user.route("/clock_user/store", methods=['GET', 'POST'])
def store():
   
   data = ClockUser.store(request.form)

   return str(data)

@clock_user.route("/clock_user", methods=['GET'])
def index():
   
   data = ClockUser.get()

   res = ClockUser.to_json(data)

   return json.dumps(res)