from app.models.models import EmployeeTypeModel

class EmployeeType():
    @staticmethod
    def get():
        employee_types = EmployeeTypeModel.query.all()
        
        return employee_types