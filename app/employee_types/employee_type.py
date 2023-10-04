from app.models.models import EmployeeTypeModel

class EmployeeType():
    @staticmethod
    def get(id = ''):
        if id != '':
            employee_type = EmployeeTypeModel.query.get(id)
            
            return employee_type
        else:
            employee_types = EmployeeTypeModel.query.all()
        
            return employee_types