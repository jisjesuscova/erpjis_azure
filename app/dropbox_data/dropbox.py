import dropbox
from PIL import Image
from dropbox.exceptions import AuthError, ApiError
from app.settings.setting import Setting
from flask_login import current_user

class Dropbox():
    @staticmethod
    def upload(name = '', description = '', data = '', dropbox_path = '', computer_path = '', resize = 0):
        settings = Setting.get()

        f = data['file']
        if resize  == 1:
            image = Image.open(f)
            image = image.resize((200, 200))
            image.save(f.filename)
        else:
            f.save(f.filename)

        extesion = f.filename.split('.')
        dropbox_file_name = str(name) + str(description)

        dropbox_path = dropbox_path + dropbox_file_name + "." + extesion[1]
        computer_path = computer_path + f.filename

        dbx = dropbox.Dropbox(settings.dropbox_token)
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path):
            return dropbox_file_name + "." + extesion[1]
        else:
            return 0

    @staticmethod
    def born_document(name = '', description = '', data = '', dropbox_path = '', computer_path = '', resize = 0):
        settings = Setting.get()

        f = data['file']
        f.save(f.filename)

        extesion = f.filename.split('.')
        dropbox_file_name = str(name) + str(description)

        dropbox_path = dropbox_path + dropbox_file_name + "." + extesion[1]
        computer_path = computer_path + f.filename

        dbx = dropbox.Dropbox(settings.dropbox_token)
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path,  mode=dropbox.files.WriteMode('overwrite')):
            return dropbox_file_name + "." + extesion[1]
        else:
            return 0

    @staticmethod
    def sign(name = '', description = '', data = '', dropbox_path = '', computer_path = ''):
        settings = Setting.get()

        f = data['file']
        f.save(f.filename)

        extesion = f.filename.split('.')
        dropbox_file_name = str(name) + str(description)

        dropbox_path = dropbox_path + dropbox_file_name + "." + extesion[1]
        computer_path = computer_path + f.filename

        dbx = dropbox.Dropbox(settings.dropbox_token)
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path,  mode=dropbox.files.WriteMode('overwrite')):
            return dropbox_file_name + "." + extesion[1]
        else:
            return 0

    @staticmethod
    def signature(file = ''):
        settings = Setting.get()

        dbx = dropbox.Dropbox(settings.dropbox_token)
        file_name = '/signature/'+ str(current_user.rut) +'.png'
        if dbx.files_upload(file, file_name, mode=dropbox.files.WriteMode('overwrite')):
            return  str(current_user.rut) +'.png'
        else:
            return 0

    @staticmethod
    def get(url, file):
        settings = Setting.get()

        dbx = dropbox.Dropbox(settings.dropbox_token)

        try:
            dbx.files_get_metadata(url + file)
            
            link = dbx.files_get_temporary_link(url + file)

            return link.link
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
        settings = Setting.get()

        dbx = dropbox.Dropbox(settings.dropbox_token)

        try:
            dbx.files_get_metadata(url + file)
            
            return 1
        except ApiError:
            return 0
        

        