from app.models.models import ProgressiveVacationModel, VacationModel, DocumentEmployeeModel, EmployeeModel, OldVacationModel, OldDocumentEmployeeModel
from app.hr_final_day_months.hr_final_day_month import HrFinalDayMonth
import time
from datetime import datetime, timedelta, date
from app import db
from fitz import fitz
from dateutil.relativedelta import relativedelta
import calendar
import re
import random
import pandas as pd
import numpy as np
import markdown
from bs4 import BeautifulSoup
import re
import math
from app.hr_settings.hr_setting import HrSetting

class Helper:
    @staticmethod
    def clean_string(input_string):
        # Remover caracteres especiales y acentos
        clean_string = re.sub(r'[^\w\s]', '', input_string).strip().lower()
        clean_string = re.sub(r'[áäà]', 'a', clean_string)
        clean_string = re.sub(r'[éëè]', 'e', clean_string)
        clean_string = re.sub(r'[íïì]', 'i', clean_string)
        clean_string = re.sub(r'[óöò]', 'o', clean_string)
        clean_string = re.sub(r'[úüù]', 'u', clean_string)
        
        # Remover espacios y convertir a formato de tag
        clean_string = re.sub(r'\s+', '-', clean_string)
        clean_string = re.sub(r'[^a-zA-Z0-9-]', '', clean_string)
        
        return clean_string

    @staticmethod
    def get_documentation_main_title(description):
        html_text = markdown.markdown(description)
        soup = BeautifulSoup(html_text, 'html.parser')
        h1_tag = soup.find('h1')

        return h1_tag
    
    @staticmethod
    def remove_from_string(value_to_remove, string):
        string = string.replace(value_to_remove, "")

        return string
    
    @staticmethod
    def fix_documentation_titles(string):
        pattern = re.compile(r'<h[1-5].*?>|</h[1-5]>')

        string = pattern.sub('', string)

        return string
    
    @staticmethod
    def years_to_months(years):
        months = years * 12

        return months
    
    @staticmethod
    def months_to_years(months):
        years = int(months/12)

        return years

    @staticmethod
    def weeks_in_month(year, month):
        # Get the number of days in the month and the first day of the week
        num_days_month = calendar.monthrange(year, month)[1]
        first_weekday = calendar.weekday(year, month, 1)
        
        # Calculate the number of weeks in the month
        remaining_days = num_days_month - (7 - first_weekday)
        complete_weeks = remaining_days // 7
        if remaining_days % 7 > 0:
            complete_weeks += 1
        
        return complete_weeks + 1

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
    

    def extention_contract(date):
        # Convertir la fecha a objeto datetime
        date_dt = datetime.strptime(date, "%Y-%m-%d").date()

        # Sumar un mes
        next_month_date = date_dt + relativedelta(months=1)

        # Retornar la nueva fecha en formato "YYYY-mm-dd"
        return next_month_date.strftime("%Y-%m-%d")

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

        file_name = str(random_float) + "_" + str(rut) + "_" + str(description) + "_" + str(current_day) + "_" + str(current_month) + "_" + str(current_year)

        return file_name
    
    def get_last_day_of_month(date_str):
        # Convertimos el string en fecha
        date = datetime.strptime(date_str, '%Y-%m-%d')
        # Obtenemos el último día del mes
        last_day = calendar.monthrange(date.year, date.month)[1]
        # Creamos una nueva fecha con el último día del mes
        last_day_date = datetime(date.year, date.month, last_day)
        # Formateamos la fecha en el formato deseado
        return last_day_date.strftime('%Y-%m-%d')

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
        value = math.ceil(amount/30)

        return value

    @staticmethod
    def fix_date(value):
        value = value.split("-")

        return value[2] + "-" + value[1] + "-" + value[0]
    
    @staticmethod
    def asset_name_date(value):
        value = value.split("-")

        return "01-" + value[1] + "-" + value[0]
    
    @staticmethod
    def asset_date(value):
        value = value.split("-")

        return value[0] + "-" + value[1] + "-01"
    
    @staticmethod
    def american_date(value):
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
    def get_time_Y_m_d():
        return datetime.now().strftime('%Y-%m-%d')
    
    @staticmethod
    def days(since, until, no_valid_entered_days = 0):
        # Definir las fechas de inicio y finalización
        start_date = datetime.strptime(since, "%Y-%m-%d")
        end_date = datetime.strptime(until, "%Y-%m-%d")

        # Calcular la cantidad de días hábiles entre las dos fechas
        num_business_days = 0
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() < 5:
                num_business_days += 1
            current_date += timedelta(days=1)

        return int(num_business_days)
    
    @staticmethod
    def months(since, until):
        since_array = Helper.split(str(since), "-")
        until_array = Helper.split(str(until), "-")

        if since != None and until != None:
            if until_array[0] != '' and since_array[0] != '':
                return (int(until_array[0]) - int(since_array[0])) * 12 + int(until_array[1]) - int(since_array[1])
            else:
                return 0
        else:
            return 0

    @staticmethod
    def gratification(salary):

        return math.ceil(salary * 0.25)
    
    @staticmethod
    def get_honorary_net_value(amount):
        hr_settings = HrSetting.get()

        amount = round(int(amount) / float(hr_settings.percentage_honorary_bill))

        return amount
    
    @staticmethod
    def get_honorary_tax_value(amount):
        hr_settings = HrSetting.get()

        gross_amount = round(int(amount) / float(hr_settings.percentage_honorary_bill))

        tax = int(gross_amount) - int(amount)

        return tax

    @staticmethod
    def calculate_end_document_end_date(start_date, balance):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = start_date + timedelta(days=balance)

        return end_date
    
    def count_weekends(start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        if end_date.weekday() == 5:  # Si es viernes (0=Lunes, 6=Domingo)
            end_date += timedelta(days=2)  # Suma 2 dias
        weekend_count = 0
        delta = timedelta(days=1)
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() >= 5:  # Si es sábado o domingo
                weekend_count += 1
            current_date += delta
            
        return weekend_count

    def count_days(date1: str, date2: str) -> int:
        date_format = "%Y-%m-%d"
        d1 = datetime.strptime(str(date1), date_format)
        d2 = datetime.strptime(str(date2), date_format)
        delta = d2 - d1
        return delta.days + 1

    def add_business_days(start_date, num_days, holidays):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        current_date = start_date
        added_days = 0
        while added_days < int(num_days):
            # sumamos un día a la fecha actual
            current_date += timedelta(days=1)
            # verificamos si la fecha actual es hábil/laboral
            if calendar.weekday(current_date.year, current_date.month, current_date.day) < 5:
                added_days += 1

        # sumamos los días feriados al resultado si la lista no está vacía
        if len(holidays) > 0:
            current_date += timedelta(days=len(holidays))

        return current_date

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
        if months > 0:
            if extreme_zone_status_id == 1:
                total = math.ceil(float((months+1))*float(1.66))
            else:
                total = math.ceil((float(months+1)) * float(1.25))
        else:
            total = 0
            
        return total

    @staticmethod
    def progressive_vacation_level(years):
        total = int(years) - 13

        if total < 0:
            level = 1
        elif total == 0:
            level = 1
        elif total == 1:
            level = 2
        elif total == 2:
            level = 3
        elif total == 3:
            level = 4
        elif total == 4:
            level = 5
        elif total == 5:
            level = 6
        elif total == 6:
            level = 7
        elif total == 7:
            level = 8
        elif total == 8:
            level = 9
        elif total == 9:
            level = 10
        elif total == 10:
            level = 11
        elif total == 11:
            level = 12
        elif total == 12:
            level = 13
        elif total == 13:
            level = 14
        elif total == 14:
            level = 15
        elif total == 15:
            level = 16

        return level

    @staticmethod
    def progressive_vacation_days(years, level):
        total = 0

        if years >= 13 and (level == 1):
            total = total + 1
        
        if years >= 14 and (level == 1 or level == 2):
            total = total + 1
        
        if years >= 15 and (level == 1 or level == 2 or level == 3):
            total = total + 1
        
        if years >= 16 and (level == 1 or level == 2 or level == 3 or level == 4):
            total = total + 2
        
        if years >= 17 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5):
            total = total + 2
        
        if years >= 18 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6):
            total = total + 2
        
        if years >= 19 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7):
            total = total + 3
        
        if years >= 20 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8):
            total = total + 3
        
        if years >= 21 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8 or level == 9):
            total = total + 3
        
        if years >= 22 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8 or level == 9 or level == 10):
            total = total + 4

        if years >= 23 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8 or level == 9 or level == 10 or level == 11):
            total = total + 4

        if years >= 24 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8 or level == 9 or level == 10 or level == 11 or level == 12):
            total = total + 4

        if years >= 25 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8 or level == 9 or level == 10 or level == 11 or level == 12 or level == 13):
            total = total + 5

        if years >= 26 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8 or level == 9 or level == 10 or level == 11 or level == 12 or level == 13 or level == 14):
            total = total + 5

        if years >= 27 and (level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8 or level == 9 or level == 10 or level == 11 or level == 12 or level == 13 or level == 14 or level == 15):
            total = total + 5

        if years == 0:
            total = 0

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
    def get_last_date(start_date, days):
        # Convertir la fecha inicial a objeto datetime
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        
        # Sumar los días especificados a la fecha inicial
        end_datetime = (start_datetime + timedelta(days=days)) - timedelta(days=1)
        
        # Formatear la fecha final como una cadena 'YYYY-mm-dd'
        end_date = end_datetime.strftime('%Y-%m-%d')
        
        return end_date
    
    @staticmethod
    def validate_current_month(start_date):
        current_date = datetime.now()
        current_date = current_date + relativedelta(months=1)
        inserted_date = datetime.strptime(start_date, '%Y-%m-%d')

        if inserted_date.month == current_date.month:
            return 0
        else:
            return 1
    
    @staticmethod
    def compare_dates(start_date, end_date):
        # Convertir las fechas de cadena a objetos datetime
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Comparar las fechas y devolver 1 si start_date es mayor que end_date, de lo contrario devolver 0
        if start_date > end_date:
            return 1
        else:
            return 0
    
    def sum_times(time1, time2):
        if not time1 or time1 == '00:00:00':
            return time2
        try:
            h1, m1, s1 = map(int, time1.split(':'))
        except ValueError:
            # handle invalid format or empty string
            h1, m1, s1 = 0, 0, 0
        h2, m2, s2 = map(int, time2.split(':'))
        total_seconds = (h1 * 3600) + (m1 * 60) + s1 + (h2 * 3600) + (m2 * 60) + s2
        new_hour = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        new_minute = remaining_seconds // 60
        new_second = remaining_seconds % 60
        return f"{new_hour:02d}:{new_minute:02d}:{new_second:02d}"

    def which_week(year, month, day):
        current_date = date(year, month, day)
        first_day_month = date(year, month, 1)
        weekday_first_day_month = first_day_month.weekday()
        week = (current_date.day + weekday_first_day_month - 1) // 7 + 1
        return week
    
    @staticmethod
    def week_day(year, month, day):
        date = datetime(year, month, day)
        week_day = date.weekday()
        wee_days = [1, 2, 3, 4, 5, 6, 7]
        return wee_days[week_day]

    @staticmethod
    def calculate_total_hours(start_time: str, end_time: str) -> float:
        format = "%H:%M:%S"
        start_time = datetime.strptime(start_time, format)
        end_time = datetime.strptime(end_time, format)

        if end_time < start_time:
            end_time += timedelta(days=1)

        diference = end_time - start_time
        total_hours = diference.total_seconds() / 3600

        return total_hours

    @staticmethod
    def get_first_day_current_month(data):
        today = date.today()
        first_day = date(today.year, today.month, 1)
        return first_day.strftime("%Y-%m-%d")

    @staticmethod
    def get_seconds(data):
        time_str = data.working
        hh, mm, ss = time_str.split(':')
        return int(hh) * 3600 + int(mm) * 60 + int(ss)

    @staticmethod
    def get_total_hour_weeks(seconds, days):
        total = seconds*days
        return time.strftime('%H:%M', time.gmtime(total))

    @staticmethod
    def get_end_document_total_years(start_year, end_year):
        date1 = datetime.strptime(str(start_year), "%Y-%m-%d")
        date2 = datetime.strptime(str(end_year), "%Y-%m-%d")

        delta = date2 - date1

        years = delta.days / 365

        months = Helper.split(end_year, '-')

        if years >= 1:
            if int(months[1]) >= 6:
                years = years + 1
        else:
            years = 0
        
        return math.ceil(years)

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
        elif type == 4:
            for datum in data:
                res.append({
                    'id': datum.id,
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

    @staticmethod
    def get_period(month, year):
        return str(month) + "-" + str(year)
        
    @staticmethod
    def get_periods(since, until):
        format = "%Y-%m-%d"
        start_obj = datetime.strptime(since, format)
        end_obj = datetime.strptime(until, format)

        # Calcula la diferencia entre las dos fechas
        diference = end_obj - start_obj

        # Obtiene la cantidad de días
        days = diference.days

        # Si las fechas están en el mismo mes, no suma 1, de lo contrario, suma 1
        if start_obj.month != end_obj.month:
            days += 1

        splited_since = since.split("-")
        splited_until = until.split("-")

        if days < 30:
            if splited_since[1] == splited_until[1]:
                first_since = since
                first_until = until
                d1 = datetime.strptime(first_since, "%Y-%m-%d")
                d2 = datetime.strptime(first_until, "%Y-%m-%d")
                first_days = abs((d2 - d1).days)
                first_days = first_days + 1

                data = [[first_since, first_until, first_days]]
            else:
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