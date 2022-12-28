from flask import Blueprint, request
from app.clock_users.clock_user import ClockUser

clock_user = Blueprint("clock_users", __name__)

@clock_user.route("/clock_user/store", methods=['GET', 'POST'])
def store():
   
   data = ClockUser.store(request.form)

   return str(data)