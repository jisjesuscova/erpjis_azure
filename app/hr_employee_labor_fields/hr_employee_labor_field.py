from app.models.models import HrEmployeeLaborFieldModel

class HrEmployeeLaborField():
    def get(id):
        hr_employee_labor_fields = HrEmployeeLaborFieldModel.query.filter_by(hr_input_description_group_id=id).all()

        return hr_employee_labor_fields