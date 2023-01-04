import dropbox
import hashlib
from PIL import Image

class Dropbox():
    @staticmethod
    def upload(name = '', description = '', data = '', dropbox_path = '', computer_path = ''):
        f = data['file']
        image = Image.open(f)
        image = image.resize((200, 200))
        image.save(f.filename)

        extesion = f.filename.split('.')
        dropbox_file_name = str(name) + str(description)

        dropbox_path = dropbox_path + dropbox_file_name + "." + extesion[1]
        computer_path = computer_path + f.filename

        dbx = dropbox.Dropbox('sl.BWRIZZvEnktjk7pVkU-hZKOOuv334y40pDOGQ_dE4F05QdLQ4rWBPedWX7KlvULwMGCDpuWctoBTWfzZPbh41_tU1MnCHZoCyLzMEJTwez2lGehu59oqIatAs72YYEgyfaA-kzQ')
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path):
            return f.filename
        else:
            return 0