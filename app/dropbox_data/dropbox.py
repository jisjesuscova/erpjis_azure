import dropbox
from PIL import Image
from dropbox.exceptions import ApiError
from werkzeug.utils import secure_filename

class Dropbox():
    @staticmethod
    def upload(name = '', description = '', data = '', dropbox_path = '', computer_path = '', resize = 0):
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

        dbx = dropbox.Dropbox('sl.BWuKiiI2Mnd7xq_mna8kAcoU6OlSefGoYxmJGMznjmWLOibE595o_KIZgG4AtQx1wwnPU5hA253suv7_8IigxoIrSVFcAPyuWIRs3YYKieD0Y-_uZw5ZzRTIk2K6qZCcVpNSxEg')
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path):
            return dropbox_file_name + "." + extesion[1]
        else:
            return 0

    @staticmethod
    def get(url, file):
        dbx = dropbox.Dropbox('sl.BWuKiiI2Mnd7xq_mna8kAcoU6OlSefGoYxmJGMznjmWLOibE595o_KIZgG4AtQx1wwnPU5hA253suv7_8IigxoIrSVFcAPyuWIRs3YYKieD0Y-_uZw5ZzRTIk2K6qZCcVpNSxEg')

        try:
            dbx.files_get_metadata(url + file)
            
            link = dbx.files_get_temporary_link(url + file)

            return link.link
        except ApiError:
            return 0

    @staticmethod
    def download(url, file):
        dbx = dropbox.Dropbox('sl.BWuKiiI2Mnd7xq_mna8kAcoU6OlSefGoYxmJGMznjmWLOibE595o_KIZgG4AtQx1wwnPU5hA253suv7_8IigxoIrSVFcAPyuWIRs3YYKieD0Y-_uZw5ZzRTIk2K6qZCcVpNSxEg')

        try:
            file, metadata = dbx.files_download(url + file)
            
            file_name = metadata.name
            file_name = secure_filename(file_name)

            return file_name
        except ApiError:
            return 0

    @staticmethod
    def delete(url, file):
        dbx = dropbox.Dropbox('sl.BWuKiiI2Mnd7xq_mna8kAcoU6OlSefGoYxmJGMznjmWLOibE595o_KIZgG4AtQx1wwnPU5hA253suv7_8IigxoIrSVFcAPyuWIRs3YYKieD0Y-_uZw5ZzRTIk2K6qZCcVpNSxEg')

        try:
            dbx.files_get_metadata(url + file)
            
            dbx.files_delete(url + file)

            return 1
        except ApiError:
            return 0
        

        