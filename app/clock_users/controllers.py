from flask import Blueprint, request
from app.clock_users.clock_user import ClockUser
from app.helpers.helper import Helper
from app.employees.employee import Employee
from flask import jsonify
import json

from app.models.models import ClockUserModel
from app import db
from datetime import datetime

clock_user = Blueprint("clock_users", __name__)

@clock_user.route("/clock_user/data", methods=['GET', 'POST'])
def data():
   status = ClockUser.check(request.form)
   
   if status == 0:
      data = ClockUser.store(request.form)
   else:
      data = ClockUser.update(request.form)

   return str(data)

@clock_user.route("/clock_user", methods=['GET'])
def index():
   
   data = ClockUser.get()

   res = ClockUser.to_json(data)

   return json.dumps(res)

@clock_user.route("/clock_user/load", methods=['GET'])
def load():
   employees = Employee.get()
   i = 1

   for employee in employees:
      
         print(employee.rut)

         clock_user = ClockUserModel()
         clock_user.uid = i
         clock_user.rut = employee.rut
         print(employee.mother_lastname.upper())
         clock_user.full_name = str(employee.names.upper()) +" "+ str(employee.father_lastname.upper()) +" "+ str(employee.mother_lastname.upper())
         if employee.rut != '27141399' and employee.rut != '15538007' and employee.rut != '17927553' and employee.rut != '10033721' and employee.rut != '10790603' and employee.rut != '16281232' and employee.rut != '16787383':
            clock_user.privilege = 0
         else:
            clock_user.privilege = 14
         clock_user.added_date = datetime.now()
         clock_user.updated_date = datetime.now()

         db.session.add(clock_user)
         db.session.commit()

         i = i + 1

   return str(1)