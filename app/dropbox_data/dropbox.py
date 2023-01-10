import dropbox
from PIL import Image
from dropbox.exceptions import ApiError

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

        dbx = dropbox.Dropbox('sl.BWmxlsapw_e8j2q2ikchD1qw6WDpvp3ZL7eHycHoeNEcLklx-07Bksk9hFz-U1FFxiBGtKVyRkfpeOGLqI_D4mn980Erv-uMM0ka418g7Q13cP5JxL3oxCxiXPbLQzJZj9LRzQw')
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path):
            return dropbox_file_name + "." + extesion[1]
        else:
            return 0

    @staticmethod
    def get(url, file):
        dbx = dropbox.Dropbox('sl.BWmxlsapw_e8j2q2ikchD1qw6WDpvp3ZL7eHycHoeNEcLklx-07Bksk9hFz-U1FFxiBGtKVyRkfpeOGLqI_D4mn980Erv-uMM0ka418g7Q13cP5JxL3oxCxiXPbLQzJZj9LRzQw')

        try:
            dbx.files_get_metadata(url + file)
            
            link = dbx.files_get_temporary_link(url + file)

            return link.link
        except ApiError:
            return 0

    @staticmethod
    def delete(url, file):
        dbx = dropbox.Dropbox('sl.BWmxlsapw_e8j2q2ikchD1qw6WDpvp3ZL7eHycHoeNEcLklx-07Bksk9hFz-U1FFxiBGtKVyRkfpeOGLqI_D4mn980Erv-uMM0ka418g7Q13cP5JxL3oxCxiXPbLQzJZj9LRzQw')

        try:
            dbx.files_get_metadata(url + file)
            
            dbx.files_delete(url + file)

            return 1
        except ApiError:
            return 0
        

        