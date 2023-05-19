from app.models.models import EmployeeLaborDatumModel
from app.helpers.helper import Helper
from app.hr_final_day_months.hr_final_day_month import HrFinalDayMonth
from app.models.models import EmployeeModel, UserModel, OldEmployeeLaborDatumModel
from datetime import datetime
from app import db

class EmployeeLaborDatum():
    def get(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()

        return employee_labor_data

    def get_by_rut(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).all()

        return employee_labor_data
    
    def get_detail_by_rut(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()

        return employee_labor_data
    
    @staticmethod
    def distribution_totals():
        # Consulta para obtener el total de hombres y mujeres
        full_time_total = EmployeeLaborDatumModel.query.filter_by(employee_type_id=1).count()
        part_time_total = EmployeeLaborDatumModel.query.filter_by(employee_type_id=2).count()

        totals = [
            {'schedule': 'Men', 'total': full_time_total},
            {'schedule': 'Women', 'total': part_time_total}
        ]
    
        return totals

    @staticmethod
    def get_by_branch_office_id(id):
        employee_labor_data = EmployeeLaborDatumModel.query\
            .join(EmployeeModel, EmployeeModel.rut == EmployeeLaborDatumModel.rut)\
            .join(UserModel, UserModel.rut == EmployeeLaborDatumModel.rut)\
            .add_columns(UserModel.rut, UserModel.nickname, EmployeeModel.father_lastname, EmployeeLaborDatumModel.employee_type_id, EmployeeLaborDatumModel.branch_office_id)\
            .filter(EmployeeLaborDatumModel.branch_office_id==id)\
            .all()

        return employee_labor_data
    
    def entrance(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()
        data = Helper.split(str(employee_labor_data.entrance_company), '-')
        start_month = str(data[0]) + '-' + data[1] +'-01'
        end_month = employee_labor_data.entrance_company

        d1 = datetime.strptime(str(start_month), "%Y-%m-%d")
        d2 = datetime.strptime(str(end_month), "%Y-%m-%d")
        days = abs((d2 - d1 ).days)

        return days
    
    def exit(rut):
        employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=rut).first()
        if employee_labor_data.exit_company != '' and employee_labor_data.exit_company != None:
            data = Helper.split(str(employee_labor_data.exit_company), '-')
        
            final_day_month = HrFinalDayMonth.get(data[1])
            final_day_month = final_day_month.end_day
            
            start_month = employee_labor_data.exit_company
            end_month = str(data[0]) + '-' + data[1] +'-' + str(final_day_month)
        
            d1 = datetime.strptime(str(start_month), "%Y-%m-%d")
            d2 = datetime.strptime(str(end_month), "%Y-%m-%d")
            days = abs((d2 - d1 ).days)
        else:
            days = 0

        return days

    def old_data_get_by_rut(rut, order_id):
        old_employee_labor_data = OldEmployeeLaborDatumModel.query.filter_by(rut=rut, order_id=order_id).all()

        return old_employee_labor_data

    @staticmethod
    def restore(rut, order_id):
        old_employee_labor_data = EmployeeLaborDatum.old_data_get_by_rut(rut, order_id)

        data = []

        for old_employee_labor_datum in old_employee_labor_data:
            data = [
                old_employee_labor_datum.rut,
                old_employee_labor_datum.visual_rut,
                old_employee_labor_datum.contract_type_id,
                old_employee_labor_datum.branch_office_id,
                old_employee_labor_datum.address,
                old_employee_labor_datum.region_id,
                old_employee_labor_datum.commune_id,
                old_employee_labor_datum.civil_state_id,
                old_employee_labor_datum.health_id,
                old_employee_labor_datum.pention_id,
                old_employee_labor_datum.job_position_id,
                old_employee_labor_datum.extreme_zone_id,
                old_employee_labor_datum.employee_type_id,
                old_employee_labor_datum.regime_id,
                old_employee_labor_datum.status_id,
                old_employee_labor_datum.health_payment_id,
                old_employee_labor_datum.entrance_pention,
                old_employee_labor_datum.entrance_company,
                old_employee_labor_datum.entrance_health,
                old_employee_labor_datum.salary,
                old_employee_labor_datum.collation,
                old_employee_labor_datum.locomotion,
                old_employee_labor_datum.company_email,
                old_employee_labor_datum.extra_health_amount,
                old_employee_labor_datum.apv_payment_type_id,
                old_employee_labor_datum.apv_amount,
                old_employee_labor_datum.added_date,
                old_employee_labor_datum.updated_date
            ]

            EmployeeLaborDatum.restore_store(data)

            EmployeeLaborDatum.old_data_delete(old_employee_labor_datum.id)

        return 1

    @staticmethod
    def restore_store(data):
        employee_labor_data = EmployeeLaborDatumModel()
        employee_labor_data.rut = data[0]
        employee_labor_data.visual_rut = data[1]
        employee_labor_data.contract_type_id = data[2]
        employee_labor_data.branch_office_id = data[3]
        employee_labor_data.address = data[4]
        employee_labor_data.region_id = data[5]
        employee_labor_data.commune_id = data[6]
        employee_labor_data.civil_state_id = data[7]
        employee_labor_data.health_id = data[8]
        employee_labor_data.pention_id = data[9]
        employee_labor_data.job_position_id = data[10]
        employee_labor_data.extreme_zone_id = data[11]
        employee_labor_data.employee_type_id = data[12]
        employee_labor_data.regime_id = data[13]
        employee_labor_data.status_id = data[14]
        employee_labor_data.health_payment_id = data[15]
        employee_labor_data.entrance_pention = data[16]
        employee_labor_data.entrance_company = data[17]
        employee_labor_data.entrance_health = data[18]
        employee_labor_data.salary = data[19]
        employee_labor_data.collation = data[20]
        employee_labor_data.locomotion = data[21]
        employee_labor_data.company_email = data[22]
        employee_labor_data.extra_health_amount = data[23]
        employee_labor_data.apv_payment_type_id = data[24]
        employee_labor_data.apv_amount = data[25]
        employee_labor_data.added_date = data[26]
        employee_labor_data.updated_date = data[27]

        db.session.add(employee_labor_data)
        db.session.commit()
        
        return employee_labor_data

    @staticmethod
    def old_data_delete(id):
        old_employee_labor_datum = OldEmployeeLaborDatumModel.query.filter_by(id=id).first()

        db.session.delete(old_employee_labor_datum)
        try:
            db.session.commit()

            return old_employee_labor_datum
        except Exception as e:
            return {'msg': 'Data could not be stored'}


    @staticmethod
    def delete(id):
        employee_labor_datum = EmployeeLaborDatumModel.query.filter_by(id=id).first()

        db.session.delete(employee_labor_datum)
        try:
            db.session.commit()

            return employee_labor_datum
        except Exception as e:
            return {'msg': 'Data could not be stored'}
