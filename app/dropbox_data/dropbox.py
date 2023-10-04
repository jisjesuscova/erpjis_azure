import dropbox
from PIL import Image
from dropbox.exceptions import AuthError, ApiError
from app.settings.setting import Setting
from app.helpers.helper import Helper
from flask_login import current_user
from datetime import datetime
import os

class Dropbox():
    @staticmethod
    def upload(name = '', description = '', data = '', dropbox_path = '', computer_path = '', resize = 0):
        settings = Setting.get()
        f = data['file']

        extesion = os.path.splitext(f.filename)[1]
        dropbox_file_name = Helper.file_name(str(name), str(description))

        dropbox_path = dropbox_path + dropbox_file_name + extesion
        computer_path = computer_path + dropbox_file_name + extesion

        if resize  == 1:
            image = Image.open(f)
            image = image.resize((200, 200))
            image.save(os.path.join(computer_path))
        else:
            f.save(os.path.join(computer_path))

        dbx = dropbox.Dropbox(settings.dropbox_token)
        if dbx.files_upload(open(os.path.join(computer_path), "rb").read(), dropbox_path):
            return dropbox_file_name + extesion
        else:
            return 0
        
    @staticmethod
    def upload_signed_files(pdf_bytes, file_path):
        settings = Setting.get()
        file_path = '/business_hours/horario.pdf'
        dbx = dropbox.Dropbox(settings.dropbox_token)
        dbx.files_upload(pdf_bytes, file_path, mode=dropbox.files.WriteMode.overwrite)

        return 1

    def upload_local_cloud(name = '', description = '', data = '', dropbox_path = '', computer_path = '', resize = 0):
        settings = Setting.get()

        f = data['file']

        extesion = os.path.splitext(f.filename)[1]
        dropbox_file_name = str(name) + "_" + str(description)
        now = datetime.now()
        formatted_date = now.strftime("%Y_%m_%d_%H_%M_%S")
        dropbox_file_name = dropbox_file_name + "_" + str(formatted_date) + extesion

        if resize  == 1:
            image = Image.open(f)
            image = image.resize((200, 200))
            image.save(os.path.join(f.filename))
        else:
            f.save(os.path.join(computer_path + dropbox_file_name))

        dropbox_path = dropbox_path + dropbox_file_name
        computer_path = computer_path + dropbox_file_name

        dbx = dropbox.Dropbox(settings.dropbox_token)
        if dbx.files_upload(open(os.path.join(computer_path), "rb").read(), dropbox_path):
            return dropbox_file_name
        else:
            return 0

    @staticmethod
    def born_document(name = '', description = '', data = '', dropbox_path = '', computer_path = '', resize = 0):
        settings = Setting.get()

        f = data['file']
        extesion = os.path.splitext(f.filename)[1]
        dropbox_file_name = Helper.file_name(str(name), str(description))

        dropbox_path = dropbox_path + dropbox_file_name + extesion
        computer_path = computer_path + dropbox_file_name + extesion
        dropbox_file_name = dropbox_file_name + extesion
        f.save(os.path.join(computer_path))

        dbx = dropbox.Dropbox(settings.dropbox_token)
        if dbx.files_upload(open(os.path.join(computer_path), "rb").read(), dropbox_path):
            return dropbox_file_name
        else:
            return 0

    @staticmethod
    def sign(name = '', description = '', data = '', dropbox_path = '', computer_path = ''):
        settings = Setting.get()

        f = data['file']
        
        extesion = os.path.splitext(f.filename)[1]
        dropbox_file_name = Helper.file_name(str(name), str(description))

        dropbox_path = dropbox_path + dropbox_file_name + extesion
        computer_path = computer_path + dropbox_file_name + extesion

        f.save(os.path.join(computer_path))

        dbx = dropbox.Dropbox(settings.dropbox_token)
        if dbx.files_upload(open(os.path.join(computer_path), "rb").read(), dropbox_path,  mode=dropbox.files.WriteMode('overwrite')):
            return dropbox_file_name + extesion
        else:
            return 0

    @staticmethod
    def signature(file = ''):
       
        settings = Setting.get()

        dbx = dropbox.Dropbox(settings.dropbox_token)
        file_name = '/signature/'+ str(current_user.rut) +'.png'
 
        with open(os.path.join( 'app/static/dist/files/signature_data/' + str(current_user.rut) +'.png'), "wb") as f:
            f.write(file)

        if dbx.files_upload(file, file_name, mode=dropbox.files.WriteMode('overwrite')):
            return  str(current_user.rut) +'.png'
        else:
            return 0

    @staticmethod
    def get(url, file):
        settings = Setting.get()

        dbx = dropbox.Dropbox(settings.dropbox_token)

        try:
            exist = Dropbox.exist(url, file)

            if exist == 1:
                dbx.files_get_metadata(url + file)
            
                link = dbx.files_get_temporary_link(url + file)

                return link.link
            else:
                return ''
        except ApiError:
            return 0

    @staticmethod
    def download(url, file):
        settings = Setting.get()

        dbx = dropbox.Dropbox(settings.dropbox_token)

        try:
            file_metadata, file_binary = dbx.files_download(url + file)
            return file_binary
            
        except ApiError as err:
            if err.user_message_text:
                print(err.user_message_text)
            else:
                print(err)
            return 'Error al descargar archivo', 400, None

    @staticmethod
    def delete(url, file):
        settings = Setting.get()

        dbx = dropbox.Dropbox(settings.dropbox_token)

        try:
            dbx.files_get_metadata(url + file)
            
            dbx.files_delete(url + file)

            return 1
        except ApiError:
            return 0
    

    @staticmethod
    def exist(url, file):
        if file == None:
            return 0
        else:
            settings = Setting.get()

            dbx = dropbox.Dropbox(settings.dropbox_token)

            try:
                dbx.files_get_metadata(url + file)
                
                return 1
            except ApiError:
                return 0
        

        