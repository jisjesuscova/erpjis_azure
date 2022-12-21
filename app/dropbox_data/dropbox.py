import dropbox
import hashlib

class Dropbox():
    @staticmethod
    def upload(data, dropbox_path, computer_path):
        f = data['file']
        f.save(f.filename)

        extesion = f.filename.split('.')
        dropbox_file_name = hashlib.md5(f.filename.encode('utf-8')).hexdigest()

        dropbox_path = dropbox_path + dropbox_file_name + "." + extesion[1]
        computer_path = computer_path + f.filename

        dbx = dropbox.Dropbox('sl.BTpbl03zV9yiYj6NXljkHy-cZQw8sufuKzWfiRBetLjMzbXeb37fX4zLUFQB435rEibMlgZjAeQqQG_n_Jzs9NM_JOwwt0UbXAtth_2c4OqC8v9M0w3KlFu5PCF0gvJu74POaQ8')
        if dbx.files_upload(open(computer_path, "rb").read(), dropbox_path):
            return f.filename
        else:
            return 0