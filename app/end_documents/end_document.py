from flask import request
from app.employee_labor_data.employee_labor_datum import EmployeeLaborDatum
from app.helpers.helper import Helper

class EndDocument():
    @staticmethod
    def substitute_compensation(rut):
        employee_labor_datum = EmployeeLaborDatum.get(rut)

        gratification = Helper.gratification(employee_labor_datum.salary)

        result = int(employee_labor_datum.salary) + int(employee_labor_datum.collation) + int(employee_labor_datum.locomotion) + int(gratification)

        return result

    @staticmethod
    def indemnity_years_service(rut):
        employee_labor_datum = EmployeeLaborDatum.get(rut)

        return result