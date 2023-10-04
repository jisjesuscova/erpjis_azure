from flask import request
from app.models.models import ContractScheduleModel

class ContractSchedule():
    @staticmethod
    def get():
            contract_schedules = ContractScheduleModel.query.all()

            return contract_schedules