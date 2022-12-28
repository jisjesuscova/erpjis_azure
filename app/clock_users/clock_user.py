from app.models.models import ClockUserModel
from app import db
from datetime import datetime

class ClockUser():
    def store(data):

        
        return str(data['uid']) + "_" + str(data['rut']) + "_" + str(data['full_name']) + "_" + str(data['privilege'])
 