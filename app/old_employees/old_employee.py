from app.models.models import OldEmployeeModel
from app.employees.employee import Employee
from app import db

class OldEmployee():
    @staticmethod
    def finish(rut, order_id):
        employees = Employee.get_by_rut(rut)

        data = []

        for employee in employees:
            data = [
                employee.rut,
                employee.visual_rut,
                employee.names,
                employee.father_lastname,
                employee.mother_lastname,
                employee.nickname,
                order_id,
                employee.gender_id,
                employee.nationality_id,
                employee.cellphone,
                employee.personal_email,
                employee.born_date,
                employee.added_date,
                employee.updated_date
            ]

            old_employee = OldEmployee.store(data)

            Employee.delete(employee.id)

        return old_employee.id

    @staticmethod
    def store(data):
        old_employee = OldEmployeeModel()
        old_employee.rut = data[0]
        old_employee.visual_rut = data[1]
        old_employee.names = data[2]
        old_employee.father_lastname = data[3]
        old_employee.mother_lastname = data[4]
        old_employee.nickname = data[5]
        old_employee.order_id = data[6]
        old_employee.gender_id = data[7]
        old_employee.nationality_id = data[8]
        old_employee.cellphone = data[9]
        old_employee.personal_email = data[10]
        old_employee.born_date = data[11]
        old_employee.added_date = data[12]
        old_employee.updated_date = data[13]

        db.session.add(old_employee)

        try:
            db.session.commit()

            return old_employee
        except Exception as e:
            return {'msg': 'Data could not be stored'}

    @staticmethod
    def get(rut = '', page = ''):
        if page != '':
            employees = OldEmployeeModel.query.order_by('rut').paginate(page=page, per_page=20, error_out=False)

            return employees
        else:
            if rut == '':
                employees = OldEmployeeModel.query.order_by('nickname').all()

                return employees
            else:
                employee = OldEmployeeModel.query.filter_by(rut = rut).first()

                return employee
    
    @staticmethod
    def get_last_order(rut):
        employee = OldEmployeeModel.query.filter_by(rut=rut).order_by(OldEmployeeModel.order_id.desc()).first()

        employee_qty = OldEmployeeModel.query.filter_by(rut=rut).order_by(OldEmployeeModel.order_id.desc()).count()
        
        if employee_qty > 0:
            return int(employee.order_id) + 1
        else:
            return 1