import dropbox
from PIL import Image
from dropbox.exceptions import ApiError

class Dropbox():
    @staticmethod
    def upload(name = '', description = '', data = '', dropbox_path = '', computer_path = ''):
        f = data['file']
        image = Image.open(f)
        image = image.resize((400, 400))
        image.save(f.filename)

        extesion = f.filename.split('.')
        dropbox_file_name = str(name) + str(description)

        dropbox_path = dropbox_path + dropbox_file_name + "." + extesion[1]
        computer_path = computer_path + f.filename

        dbx = dropbox.Dropbox('sl.BWUJSwI7XnDa2s5JSEWbC0MSEy_137SlkuTMpndgx8C6wiIcj5t-_G7hPlYlBC5ngovxONdGXyGNIQT3B06kIRs7ILLgMHZzea7ipR_Es0LCYoECsh4ce45l5U3JkakMiEybuUg')
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path):
            return dropbox_file_name + "." + extesion[1]
        else:
            return 0

    @staticmethod
    def get(url, file):
        dbx = dropbox.Dropbox('sl.BWUJSwI7XnDa2s5JSEWbC0MSEy_137SlkuTMpndgx8C6wiIcj5t-_G7hPlYlBC5ngovxONdGXyGNIQT3B06kIRs7ILLgMHZzea7ipR_Es0LCYoECsh4ce45l5U3JkakMiEybuUg')

        try:
            dbx.files_get_metadata(url + file)
            
            link = dbx.files_get_temporary_link(url + file)

            return link.link
        except ApiError:
            return 0

    @staticmethod
    def delete(url, file):
        dbx = dropbox.Dropbox('sl.BWUJSwI7XnDa2s5JSEWbC0MSEy_137SlkuTMpndgx8C6wiIcj5t-_G7hPlYlBC5ngovxONdGXyGNIQT3B06kIRs7ILLgMHZzea7ipR_Es0LCYoECsh4ce45l5U3JkakMiEybuUg')

        try:
            dbx.files_get_metadata(url + file)
            
            dbx.files_delete(url + file)

            return 1
        except ApiError:
            return 0
        

        