from flask import Blueprint
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app import regular_employee_rol_need
from flask_login import login_required
from app.helpers.helper import Helper
import json


branch_office = Blueprint("branch_offices", __name__)

@branch_office.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass


@branch_office.before_request
def constructor():
   pass

@branch_office.route("/branch_offices/employees/<int:id>", methods=['GET'])
def index(id):
    employees = EmployeeLaborDatum.get_by_branch_office_id(id)
    employees = Helper.serialize(employees, 1)

    return json.dumps(employees)