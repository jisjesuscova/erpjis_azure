from datetime import datetime
from app.models.models import ProgressiveVacationModel, VacationModel, DocumentEmployeeModel, EmployeeModel, OldVacationModel, OldDocumentEmployeeModel
from app.hr_final_day_months.hr_final_day_month import HrFinalDayMonth
import time
from datetime import datetime, timedelta
from app import db
from fitz import fitz
from dateutil.relativedelta import relativedelta
import calendar
import re
import random

class Helper:
    @staticmethod
    def document_date(date):
        object_date = datetime.strptime(date, "%Y-%m-%d")

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        month_name = months[object_date.month - 1]
        fixed_date = f"{object_date.day} de {month_name} del {object_date.year}"

        return fixed_date

    @staticmethod
    def fix_entrance_date(date):
        if date != '':
            return date
        else:
            date = None

            return date

    @staticmethod
    def numeric_rut(rut):
        rut = rut.split('-')

        return rut[0]

    @staticmethod
    def extention_contract(date):
        result = date + relativedelta(months=+1)

        return result

    @staticmethod
    def add_zero(number):
        if number < 10:
            result = "0" + str(number)
        else:
            result = number

        return result

    @staticmethod
    def get_last_order_id_to_restore(number):
        number = int(number) - 1

        if 0 == number:
            result = 1
        else:
            result = number

        return result

    @staticmethod
    def upper_string(string):
        result = string.upper()

        return result

    @staticmethod
    def remove_special_characters(string):
        pattern = '[^A-Za-z0-9]+'

        result = re.sub(pattern, '', string)

        return result

    @staticmethod
    def fix_thousands(number):
        result = "{:,}".format(number).replace(",", ".")

        return result

    @staticmethod
    def file_name(rut, description):
        now = datetime.now()

        current_year = now.year
        current_month = now.month
        current_day = now.day

        current_month = Helper.add_zero(current_month)

        random_float = random.randint(1, 9999999999999999)

        file_name = str(random_float) + "_" + str(rut) + str(description) + "_" + str(current_day) + "_" + str(current_month) + "_" + str(current_year)

        return file_name

    @staticmethod
    def get_last_day(date):
        date = Helper.split(str(date), "-")
        year, month = int(date[0]), int(date[1])
        result = calendar.monthrange(year, month)[1]
        month = Helper.add_zero(month)

        return str(result) + "-" + str(month) + "-" + str(year)
    
    @staticmethod
    def split(value, separator):
        value = value.split(separator)

        return value

    @staticmethod
    def is_active(rut):
        employee = EmployeeModel.query.filter_by(rut=rut).count()

        return employee

    @staticmethod
    def vacation_day_value(amount):
        value = round(amount/30)

        return value

    @staticmethod
    def fix_date(value):
        value = value.split("-")

        return value[2] + "-" + value[1] + "-" + value[0]

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
        total = abs(subtotal) - abs(int(no_valid_days))
        return total
    
    @staticmethod
    def months(since, until):
        if since != None and until != None:
            return (until.year - since.year) * 12 + until.month - since.month
        else:
            return 0

    @staticmethod
    def gratification(salary):

        return round(salary * 0.25)

    @staticmethod
    def calculate_end_document_end_date(start_date, balance):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = start_date + timedelta(days=balance)

        return end_date

    @staticmethod
    def weekends_between_dates(start_date, end_date):
        start_date = str(start_date)
        end_date = str(end_date)
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        delta = end_date - start_date
        return (delta.days + 1 + (start_date.weekday() > 4) + (end_date.weekday() > 4)) // 7
    
    @staticmethod
    def vacation_days(months, extreme_zone_status_id):
        if extreme_zone_status_id == 1:
            total = round(months*1.65)
        else:
            total = round(months*1.25)

        return total

    @staticmethod
    def progressive_vacation_days(months, extreme_zone_status_id = ''):
        total = 0

        if months >= 36:
            total = total + 1
        
        if months >= 48:
            total = total + 1
        
        if months >= 60:
            total = total + 1
        
        if months >= 72:
            total = total + 2
        
        if months >= 84:
            total = total + 2
        
        if months >= 96:
            total = total + 2
        
        if months >= 108:
            total = total + 3
        
        if months >= 120:
            total = total + 3
        
        if months >= 132:
            total = total + 3
        
        if months >= 144:
            total = total + 4

        if months >= 156:
            total = total + 4

        if months >= 168:
            total = total + 4

        if months >= 180:
            total = total + 5

        if months >= 192:
            total = total + 5

        if months >= 204:
            total = total + 5


        return total
    
    @staticmethod
    def get_taken_days(rut):
        status_id = Helper.is_active(rut)

        if status_id == 1:
            vacations = VacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == VacationModel.document_employee_id)\
                        .add_columns(VacationModel.no_valid_days, VacationModel.id, VacationModel.rut, VacationModel.since, VacationModel.until, VacationModel.days, DocumentEmployeeModel.status_id)\
                        .filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==6, db.or_(DocumentEmployeeModel.status_id==4, DocumentEmployeeModel.status_id==3)) \
                        .order_by(db.desc(DocumentEmployeeModel.added_date))

            taken_days = 0

            for vacation in vacations:
                taken_days = taken_days + vacation.days - vacation.no_valid_days
        else:
            vacations = OldVacationModel.query\
                        .join(OldDocumentEmployeeModel, OldDocumentEmployeeModel.id == OldVacationModel.document_employee_id)\
                        .add_columns(OldVacationModel.no_valid_days, OldVacationModel.id, OldVacationModel.rut, OldVacationModel.since, OldVacationModel.until, OldVacationModel.days, OldDocumentEmployeeModel.status_id)\
                        .filter(OldDocumentEmployeeModel.rut==rut, OldDocumentEmployeeModel.document_type_id==6, db.or_(OldDocumentEmployeeModel.status_id==4, OldDocumentEmployeeModel.status_id==3)) \
                        .order_by(db.desc(OldDocumentEmployeeModel.added_date))

            taken_days = 0

            for vacation in vacations:
                taken_days = taken_days + vacation.days - vacation.no_valid_days

        return taken_days

    @staticmethod
    def get_taken_progressive_days(rut):

        vacations = ProgressiveVacationModel.query\
                        .join(DocumentEmployeeModel, DocumentEmployeeModel.id == ProgressiveVacationModel.document_employee_id)\
                        .add_columns(ProgressiveVacationModel.no_valid_days, ProgressiveVacationModel.id, ProgressiveVacationModel.rut, ProgressiveVacationModel.since, ProgressiveVacationModel.until, ProgressiveVacationModel.days, DocumentEmployeeModel.status_id)\
                        .filter(DocumentEmployeeModel.rut==rut, DocumentEmployeeModel.document_type_id==36, db.or_(DocumentEmployeeModel.status_id==4, DocumentEmployeeModel.status_id==3)) \
                        .order_by(db.desc(DocumentEmployeeModel.added_date))

        taken_days = 0

        for vacation in vacations:
            taken_days = taken_days + vacation.days - vacation.no_valid_days

        return taken_days
    
    @staticmethod
    def normal_gratifcation(salary, locomotion, collation):
        return (salary + locomotion + collation) * 0.25

    @staticmethod
    def add_footer(pdf, w, h, x1, x2, site="right", skip_pages = 1):
        
        # Define which image should be inserted
        img = open("logo.png", "rb").read()

        
        if site == "right":
            rect = fitz.Rect(w * x1, h * x2, w, h)
        else:
            rect = fitz.Rect(w * x1 * -1 * 0.94, h * x2, w, h)

        for i in range(0, pdf.pageCount):
            if i < pdf.pageCount - skip_pages:
                page = pdf[0]
                if not page.is_wrapped:
                    page.wrap_contents()
                page.insertImage(rect, stream=img)
    
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
    def create_date(month, year):
        return str(year) +"-"+ str(month) +"-01 00:00:00"

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

    def get_end_document_total_years(start_year, end_year):
        date1 = datetime.strptime(str(start_year), "%Y-%m-%d")
        date2 = datetime.strptime(str(end_year), "%Y-%m-%d")

        delta = date2 - date1

        years = delta.days / 365.2425

        months = Helper.split(end_year, '-')

        if years >= 1:
            if int(months[1]) >= 6:
                years = years + 1
        else:
            years = 0
        
        return round(years)

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
    def add_months(dt, months):
        month = dt.month - 1 + months
        year = dt.year + month // 12
        month = month % 12 + 1
        day = min(dt.day, calendar.monthrange(year, month)[1])
        return dt.replace(year=year, month=month, day=day)

    @staticmethod
    def month_name(month):

        MONTH_NAMES_ES = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'
        }

        return MONTH_NAMES_ES[month]

    staticmethod
    def get_periods(since, until):
        d1 = datetime.strptime(since, "%Y-%m-%d")
        d2 = datetime.strptime(until, "%Y-%m-%d")
        days = abs((d2 - d1).days)

        splited_since = since.split("-")
        splited_until = until.split("-")

        if days < 30:
            first_since = since
            first_until = until
            d1 = datetime.strptime(first_since, "%Y-%m-%d")
            d2 = datetime.strptime(first_until, "%Y-%m-%d")
            first_days = abs((d2 - d1).days)
            first_days = first_days + 1

            data = [[first_since, first_until, first_days]]
        else:
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
                
                middle_month = int(splited_since[1]) + 1
                final_day = HrFinalDayMonth.get(middle_month)
                final_day = final_day.end_day
                second_since = str(splited_until[0]) +'-'+ str(middle_month) + '-01'
                second_until = str(splited_until[0]) +'-'+ str(middle_month) + '-' + str(final_day)
                d1 = datetime.strptime(second_since, "%Y-%m-%d")
                d2 = datetime.strptime(second_until, "%Y-%m-%d")
                second_days = abs((d2 - d1).days)
                second_days = second_days + 1

                splited_since = second_since.split("-")
                splited_until = second_until.split("-")

                middle_month = int(splited_since[1]) + 1
                third_since = splited_until[0] +'-'+ str(middle_month) + '-01'
                third_until = until
                d1 = datetime.strptime(third_since, "%Y-%m-%d")
                d2 = datetime.strptime(third_until, "%Y-%m-%d")
                third_days = abs((d2 - d1).days)
                third_days = third_days + 1

                data = [[first_since, first_until, first_days], [second_since, second_until, second_days], [third_since, third_until, third_days]]

        return data