from app.models.models import OldEmployeeLaborDatumModel
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app import db
from datetime import datetime

class OldEmployeeLaborDatum():
    def get(rut):
        employee_labor_data = OldEmployeeLaborDatumModel.query.filter_by(rut=rut).first()

        return employee_labor_data

    @staticmethod
    def get_last_order(rut):
        employee_labor_datum = OldEmployeeLaborDatumModel.query.filter_by(rut=rut).order_by(OldEmployeeLaborDatumModel.order_id.desc()).first()

        employee_labor_datum_qty = OldEmployeeLaborDatumModel.query.filter_by(rut=rut).order_by(OldEmployeeLaborDatumModel.order_id.desc()).count()
        
        if employee_labor_datum_qty > 0:
            return int(employee_labor_datum.order_id) + 1
        else:
            return 1

    @staticmethod
    def finish(rut, order_id):
        employee_labor_data = EmployeeLaborDatum.get_by_rut(rut)

        data = []

        for employee_labor_datum in employee_labor_data:
            data = [
                employee_labor_datum.rut,
                employee_labor_datum.visual_rut,
                employee_labor_datum.contract_type_id,
                employee_labor_datum.branch_office_id,
                employee_labor_datum.address,
                employee_labor_datum.region_id,
                employee_labor_datum.commune_id,
                employee_labor_datum.civil_state_id,
                employee_labor_datum.health_id,
                employee_labor_datum.pention_id,
                employee_labor_datum.job_position_id,
                employee_labor_datum.employee_type_id,
                order_id,
                employee_labor_datum.regime_id,
                employee_labor_datum.status_id,
                employee_labor_datum.entrance_pention,
                employee_labor_datum.entrance_company,
                employee_labor_datum.entrance_health,
                employee_labor_datum.salary,
                employee_labor_datum.collation,
                employee_labor_datum.locomotion,
                employee_labor_datum.company_email,
                employee_labor_datum.added_date,
                employee_labor_datum.updated_date,
                employee_labor_datum.health_payment_id,
                employee_labor_datum.extra_health_amount,
                employee_labor_datum.apv_payment_type_id,
                employee_labor_datum.apv_amount

            ]

            OldEmployeeLaborDatum.store(data)

            EmployeeLaborDatum.delete(employee_labor_datum.id)

        return 1

    @staticmethod
    def store(data):
        old_employee_labor_data = OldEmployeeLaborDatumModel()
        old_employee_labor_data.rut = data[0]
        old_employee_labor_data.visual_rut = data[1]
        old_employee_labor_data.contract_type_id = data[2]
        old_employee_labor_data.branch_office_id = data[3]
        old_employee_labor_data.address = data[4]
        old_employee_labor_data.region_id = data[5]
        old_employee_labor_data.commune_id = data[6]
        old_employee_labor_data.civil_state_id = data[7]
        old_employee_labor_data.health_id = data[8]
        old_employee_labor_data.pention_id = data[9]
        old_employee_labor_data.job_position_id = data[10]
        old_employee_labor_data.employee_type_id = data[11]
        old_employee_labor_data.order_id = data[12]
        old_employee_labor_data.regime_id = data[13]
        old_employee_labor_data.status_id = data[14]
        old_employee_labor_data.entrance_pention = data[15]
        old_employee_labor_data.entrance_company = data[16]
        old_employee_labor_data.entrance_health = data[17]
        old_employee_labor_data.salary = data[18]
        old_employee_labor_data.collation = data[19]
        old_employee_labor_data.locomotion = data[20]
        old_employee_labor_data.company_email = data[21]
        old_employee_labor_data.added_date = data[22]
        old_employee_labor_data.updated_date = data[23]
        old_employee_labor_data.health_payment_id = data[24]
        old_employee_labor_data.extra_health_amount = data[25]
        old_employee_labor_data.apv_payment_type_id = data[26]
        old_employee_labor_data.apv_amount = data[27]

        db.session.add(old_employee_labor_data)
        db.session.commit()
        
        return old_employee_labor_data


    @staticmethod
    def end(rut, exit_company, status_id):
        old_employee_labor_data = OldEmployeeLaborDatumModel.query.filter_by(rut = rut).first()
        old_employee_labor_data.status_id = status_id
        old_employee_labor_data.exit_company = exit_company
        old_employee_labor_data.updated_date = datetime.now()

        db.session.add(old_employee_labor_data)
        db.session.commit()
        
        return old_employee_labor_data