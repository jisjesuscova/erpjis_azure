from flask import request
from app.models.models import AlertModel
from app import db
from datetime import datetime
from sqlalchemy import func

class Alert():
    @staticmethod
    def store(rut, alert_type_id):
        alert = AlertModel()
        alert.rut = rut
        alert.alert_type_id = alert_type_id
        alert.status_id = 0
        alert.added_date = datetime.now()
        alert.updated_date = datetime.now()

        db.session.add(alert)
        
        try:
            db.session.commit()

            return 1
        except Exception as e:
            return 0
        
    @staticmethod
    def check_alert(rut, date, alert_type_id):
        alert = AlertModel.query.filter_by(rut=rut,alert_type_id=alert_type_id)\
        .filter(func.DATE(AlertModel.added_date) == date).count()

        if alert > 0:
            return 1
        else:
            return 0
        