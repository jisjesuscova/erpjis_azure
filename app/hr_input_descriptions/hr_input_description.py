from sqlalchemy.sql import text
from app.models.models import HrEmployeeDayModel
from app.models.models import HrInputDescriptionModel

class HrInputDescription():
    def get(id = '', hr_input_type_id = ''):
        if id != '':
            hr_input_description = HrInputDescriptionModel.query.filter_by(id=id).order_by('hr_input_description').first()
        
            return hr_input_description

        if hr_input_type_id != '':
            hr_input_descriptions = HrInputDescriptionModel.query.filter_by(hr_input_type_id=hr_input_type_id).order_by('hr_input_description').all()
        
            return hr_input_descriptions

    def get_position(type_id = ''):
        if type_id == 1:
            hr_input_description = HrInputDescriptionModel.query.filter(HrInputDescriptionModel.header_position > 0).order_by('header_position').all()
        
            return hr_input_description

        if type_id == 2:
            hr_input_description = HrInputDescriptionModel.query.filter(HrInputDescriptionModel.positive_position >= 0).order_by('positive_position').all()
        
            return hr_input_description

        if type_id == 3:
            hr_input_description = HrInputDescriptionModel.query.filter(HrInputDescriptionModel.negative_position >= 0).order_by('negative_position').all()
        
            return hr_input_description
    
    def get_entrance_day_value(rut, period):
        hr_employee_day = HrEmployeeDayModel.query.filter_by(rut=rut, period=period).first()
        
        return hr_employee_day.entrance_days

    def get_by_settlement_name(settlement_name):
        hr_input_description = HrInputDescriptionModel.query.filter_by(settlement_name=settlement_name).first()
        
        return hr_input_description.settlement_name

    def check_if_total(settlement_name):
        hr_input_description = HrInputDescriptionModel.query.filter_by(settlement_name=settlement_name).first()
        
        return hr_input_description.total_status