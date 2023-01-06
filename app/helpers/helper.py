from datetime import datetime
from app.models.models import VacationModel
from app.hr_final_day_months.hr_final_day_month import HrFinalDayMonth
import time
from datetime import datetime
import requests
import json

class Helper:
    @staticmethod
    def numeric_rut(rut):
        rut = rut.split('-')

        return rut[0]
    
    @staticmethod
    def split(value, separator):
        value = value.split(separator)

        return value

    @staticmethod
    def convert_to_thousands(value):
        value = f'{value:,}'

        value = value.replace(',', '.')

        return value

    @staticmethod
    def convert_to_array(array, value, position):
        array.insert(position, value)
        
        return array
    
    @staticmethod
    def check_negative_days(value):
        if value < 0:
            return 0
        else:
            return value

    @staticmethod
    def nickname(name, lastname):
        nickname = str(name) + ' ' + str(lastname) 

        return nickname
    
    @staticmethod
    def days(since, until, no_valid_days):
        d1 = datetime.strptime(since, "%Y-%m-%d")
        d2 = datetime.strptime(until, "%Y-%m-%d")
        subtotal = abs((d2 - d1 ).days)
        subtotal = abs(subtotal) + abs(1)
        total = abs(subtotal) + abs(int(no_valid_days))
        return total
    
    @staticmethod
    def months(since, until):

        return (until.year - since.year) * 12 + until.month - since.month
    
    @staticmethod
    def vacation_days(months, extreme_zone_status_id):
        if extreme_zone_status_id == 1:
            total = round(months*1.65)
        else:
            total = round(months*1.25)

        return total
    
    @staticmethod
    def get_taken_days(rut):
        vacations = VacationModel.query.filter_by(rut=rut).all()
        taken_days = 0

        for vacation in vacations:
            taken_days = taken_days + vacation.days

        return taken_days
    
    @staticmethod
    def normal_gratifcation(salary, locomotion, collation):
        return (salary + locomotion + collation) * 0.25
    
    @staticmethod
    def proportional_gratifcation():
        vacations = VacationModel.query.filter_by(rut=rut).all()
        taken_days = 0

        for vacation in vacations:
            taken_days = taken_days + vacation.days

        return taken_days
    
    @staticmethod
    def period(month, year):
        return month +'-'+year

    @staticmethod
    def calculate_work_hours(data):
        
        return data.working

    @staticmethod
    def get_last_date(start_date, add_days):
        s = start_date
        date = datetime.strptime(s, "%Y/%m/%d")
        
        return pd.to_datetime(start_date) + pd.DateOffset(days=add_days)

    def get_seconds(data):
        time_str = data.working
        hh, mm, ss = time_str.split(':')
        return int(hh) * 3600 + int(mm) * 60 + int(ss)

    def get_total_hour_weeks(seconds, days):
        total = seconds*days
        return time.strftime('%H:%M', time.gmtime(total))

    @staticmethod
    def serialize(data, type):
        res = []
        if type == 1:
            for datum in data:
                res.append({
                    'rut': datum.rut,
                    'nickname': datum.nickname,
                    'father_lastname': datum.father_lastname,
                    'employee_type_id': datum.employee_type_id,
                    'branch_office_id': datum.branch_office_id,
                })
        elif type == 2:
            for datum in data:
                res.append({
                    'id': datum.id,
                    'group_id': datum.group_id,
                    'group_day_id': datum.group_day_id,
                    'free_day_group_id': datum.free_day_group_id,
                    'turn': datum.turn,
                    'working': datum.working,
                    'breaking': datum.breaking,
                    'start': datum.start,
                    'end': datum.end,
                    'break_in': datum.break_in,
                    'break_out': datum.break_out,
                })
        elif type == 3:
            for datum in data:
                res.append({
                    'days': datum.free_day_group_id,
                })

        return res
    
    @staticmethod
    def get_periods(since, until):
        d1 = datetime.strptime(since, "%Y-%m-%d")
        d2 = datetime.strptime(until, "%Y-%m-%d")
        days = abs((d2 - d1).days)

        splited_since = since.split("-")
        splited_until = until.split("-")

        if days < 60:
            final_day = HrFinalDayMonth.get(splited_since[1])
            final_day = final_day.end_day
            first_since = since
            first_until = splited_since[0] +'-'+ splited_since[1] + '-' + str(final_day)
            d1 = datetime.strptime(first_since, "%Y-%m-%d")
            d2 = datetime.strptime(first_until, "%Y-%m-%d")
            first_days = abs((d2 - d1).days)
            first_days = first_days + 1

            second_since = splited_until[0] +'-'+ splited_until[1] + '-01'
            second_until = until
            d1 = datetime.strptime(second_since, "%Y-%m-%d")
            d2 = datetime.strptime(second_until, "%Y-%m-%d")
            second_days = abs((d2 - d1).days)
            second_days = second_days + 1

            data = [[first_since, first_until, first_days], [second_since, second_until, second_days]]
        else:
            final_day = HrFinalDayMonth.get(splited_since[1])
            final_day = final_day.end_day
            first_since = since
            first_until = splited_since[0] +'-'+ splited_since[1] + '-' + str(final_day)
            d1 = datetime.strptime(first_since, "%Y-%m-%d")
            d2 = datetime.strptime(first_until, "%Y-%m-%d")
            first_days = abs((d2 - d1).days)
            first_days = first_days + 1
            
            middle_month = splited_since[1] + 1
            final_day = HrFinalDayMonth.get(middle_month)
            final_day = final_day.end_day
            second_since = splited_until[0] +'-'+ middle_month + '-01'
            second_until = splited_until[0] +'-'+ middle_month + '-' + str(final_day)
            d1 = datetime.strptime(second_since, "%Y-%m-%d")
            d2 = datetime.strptime(second_until, "%Y-%m-%d")
            second_days = abs((d2 - d1).days)
            second_days = second_days + 1

            third_since = splited_until[0] +'-'+ splited_since[1] + '-01'
            third_until = until
            d1 = datetime.strptime(third_since, "%Y-%m-%d")
            d2 = datetime.strptime(third_until, "%Y-%m-%d")
            third_days = abs((d2 - d1).days)
            third_days = third_days + 1

            data = [[first_since, first_until, first_days], [second_since, second_until, second_days], [third_since, third_until, third_days]]

        return data