import dropbox
from PIL import Image
from dropbox.exceptions import ApiError

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

        dbx = dropbox.Dropbox('sl.BWVFurcA3Rj9OfdhdoK_Sv2feZu6yPCo0LPWHg6URtePNW41n09Z4-wJ-VbFX9jTgSEZ6HVgS2N6KpR8pq0F5IL8ivi3bcOYaVT2Kkm6rcm1R2YzMl9glbgNd-67FcaYN5JSolY')
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path):
            return dropbox_file_name + "." + extesion[1]
        else:
            return 0

    @staticmethod
    def get(url, file):
        dbx = dropbox.Dropbox('sl.BWVlDF0Jp6hnCOmV5H02Tj5xTtafRVzjC7Gg5OR0JVGaZGowwLFoClvRhkYpb-CNrvC6JTim3Xw3ctdnA--Gy58n23iP2fPA9Na2mkSTpDN8wGmRjXMQ5dEfvENFsmliw00qTog')

        try:
            dbx.files_get_metadata(url + file)
            
            link = dbx.files_get_temporary_link(url + file)

            return link.link
        except ApiError:
            return 0

    @staticmethod
    def delete(url, file):
        dbx = dropbox.Dropbox('sl.BWVlDF0Jp6hnCOmV5H02Tj5xTtafRVzjC7Gg5OR0JVGaZGowwLFoClvRhkYpb-CNrvC6JTim3Xw3ctdnA--Gy58n23iP2fPA9Na2mkSTpDN8wGmRjXMQ5dEfvENFsmliw00qTog')

        try:
            dbx.files_get_metadata(url + file)
            
            dbx.files_delete(url + file)

            return 1
        except ApiError:
            return 0
        

        