from app.models.models import HrEmployeeDayModel

class HrEmployeeDay():
    def get(period):
        hr_employee_days = HrEmployeeDayModel.query.filter_by(period=period).order_by('rut').all()

        return hr_employee_days