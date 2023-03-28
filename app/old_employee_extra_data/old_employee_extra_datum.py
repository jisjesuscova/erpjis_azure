from app.models.models import OldEmployeeExtraModel
from app.employee_extra_data.employee_extra_datum import EmployeeExtraDatum
from app import db

class OldEmployeeExtraDatum():
    @staticmethod
    def get(rut = ''):
        employee_extra_data = OldEmployeeExtraModel.query.filter_by(rut=rut).first()

        return employee_extra_data

    
    @staticmethod
    def get_last_order(rut):
        employee_extra = OldEmployeeExtraModel.query.filter_by(rut=rut).order_by(OldEmployeeExtraModel.order_id.desc()).first()

        employee_extra_qty = OldEmployeeExtraModel.query.filter_by(rut=rut).order_by(OldEmployeeExtraModel.order_id.desc()).count()
        
        if employee_extra_qty > 0:
            return int(employee_extra.order_id) + 1
        else:
            return 1

    @staticmethod
    def finish(rut, order_id):
        employee_extra_data = EmployeeExtraDatum.get_by_rut(rut)

        data = []

        for employee_extra_datum in employee_extra_data:
            data = [
                employee_extra_datum.rut,
                employee_extra_datum.visual_rut,
                employee_extra_datum.extreme_zone_id,
                employee_extra_datum.employee_type_id,
                employee_extra_datum.young_job_status_id,
                employee_extra_datum.be_paid_id,
                employee_extra_datum.suplemental_health_insurance_id,
                employee_extra_datum.pensioner_id,
                employee_extra_datum.disability_id,
                order_id,
                employee_extra_datum.progressive_vacation_status_id,
                employee_extra_datum.progressive_vacation_date,
                employee_extra_datum.added_date,
                employee_extra_datum.updated_date
            ]

            OldEmployeeExtraDatum.store(data)

            EmployeeExtraDatum.delete(employee_extra_datum.id)

        return 1

    @staticmethod
    def store(data):
        old_employee_extra_datum = OldEmployeeExtraModel()
        old_employee_extra_datum.rut = data[0]
        old_employee_extra_datum.visual_rut = data[1]
        old_employee_extra_datum.extreme_zone_id = data[2]
        old_employee_extra_datum.employee_type_id = data[3]
        old_employee_extra_datum.young_job_status_id = data[4]
        old_employee_extra_datum.be_paid_id = data[5]
        old_employee_extra_datum.suplemental_health_insurance_id = data[6]
        old_employee_extra_datum.pensioner_id = data[7]
        old_employee_extra_datum.disability_id = data[8]
        old_employee_extra_datum.order_id = data[9]
        old_employee_extra_datum.progressive_vacation_status_id = data[10]
        old_employee_extra_datum.progressive_vacation_date = data[11]
        old_employee_extra_datum.added_date = data[12]
        old_employee_extra_datum.updated_date = data[13]

        db.session.add(old_employee_extra_datum)
        db.session.commit()
        
        return old_employee_extra_datum.id