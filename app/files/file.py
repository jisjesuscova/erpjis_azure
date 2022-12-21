import pandas as pd
from app.helpers.helper import Helper
from app.hr_employee_inputs.hr_employee_input import HrEmployeeInput
from app.models.models import EmployeeLaborDatumModel

class File():
    @staticmethod
    def upload_csv(data, computer_path, period, hr_input_description_id):
        f = data['file']
        f.save(f.filename)

        col_names = ['value']
        csvData = pd.read_csv(computer_path + '/massive.csv', names = col_names, header=None)
        for i,row in csvData.iterrows():
            value = row['value']
            values = Helper.split(value, ';')

            employee_labor_data = EmployeeLaborDatumModel.query.filter_by(rut=values[0]).first()
            branch_office_id = employee_labor_data.branch_office_id

            HrEmployeeInput.massive_store(values[0], values[1], branch_office_id, hr_input_description_id, period)
            
        return 1