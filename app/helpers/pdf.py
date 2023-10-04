from flask import Blueprint, render_template, redirect, request, url_for, make_response
import pdfkit
from app.hr_single_taxes.hr_single_tax import HrSingleTax
from werkzeug.utils import secure_filename

import os

class Pdf:
    @staticmethod
    def create_pdf(file_name, data):

        path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
        
        config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

        template_path = 'pdfs/' + str(file_name) + '.html'

        rendered = render_template(template_path, data = data, root = 'http://localhost:5000/')

        pdf = pdfkit.from_string(rendered, options={
                                                    "enable-local-file-access": "",
                                                    'page-size': 'letter',
                                                    'margin-top': '0.7in',
                                                    'margin-right': '0.5in',
                                                    'margin-bottom': '0.5in',
                                                    'margin-left': '0.5in',
                                                    'dpi': '400',
                                                    'zoom': '1'
                                                    }, configuration = config)

        return pdf
    
    @staticmethod
    def create_pdf2(file_name, data):
        path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

        template_path = 'pdfs/' + str(file_name) + '.html'

        rendered = render_template(template_path, data = data, root = 'http://localhost:5000/')

        pdf = pdfkit.from_string(rendered, options={"enable-local-file-access": ""}, configuration = config)

        return pdf

    @staticmethod
    def create_business_hours_pdf(file_name, data, multiple_data = '', total_data = ''):
        path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

        template_path = 'pdfs/' + str(file_name) + '.html'

        logo = os.path.join('app/static/dist/img/logo.png')

        rendered = render_template(template_path, data = data, root = 'https://127.0.0.1:5000/', multiple_data = multiple_data, logo = logo, total_data = total_data)

        pdf = pdfkit.from_string(rendered, options={
                                                    "enable-local-file-access": "",
                                                    'page-size': 'letter',
                                                    'margin-top': '0.7in',
                                                    'margin-right': '0.5in',
                                                    'margin-bottom': '0.5in',
                                                    'margin-left': '0.5in'
                                                    }, configuration = config)
        
        return pdf
    
    @staticmethod
    def create_vacation_pdf(file_name, data, multiple_data = '', total_data = ''):
        path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

        template_path = 'pdfs/' + str(file_name) + '.html'

        logo = os.path.join('app/static/dist/img/logo.png')

        rendered = render_template(template_path, data = data, root = 'https://127.0.0.1:5000/', multiple_data = multiple_data, total_data = total_data, logo = logo)

        pdf = pdfkit.from_string(rendered, options={
                                                    "enable-local-file-access": "",
                                                    'page-size': 'letter',
                                                    'margin-top': '0.7in',
                                                    'margin-right': '0.5in',
                                                    'margin-bottom': '0.5in',
                                                    'margin-left': '0.5in'
                                                    }, configuration = config)
        
        return pdf

    @staticmethod
    def create_settlement(file_name, header_data, positive_data, settlement_positive_name, negative_data, settlement_negative_name, total_positive_data, total_negative_data, total_values):
        path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

        template_path = 'pdfs/' + str(file_name) + '.html'

        factor = HrSingleTax.factor(positive_data[0])
        factor = factor * 100
 
        rendered = render_template(template_path, factor = factor, header_data = header_data, positive_data = positive_data, settlement_positive_name = settlement_positive_name, negative_data = negative_data, settlement_negative_name = settlement_negative_name, total_positive_data = total_positive_data, total_negative_data = total_negative_data, root = 'http://localhost:5000/', total_values = total_values)
        pdf = pdfkit.from_string(rendered, False, configuration = config)
        
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=document.pdf'

        return response