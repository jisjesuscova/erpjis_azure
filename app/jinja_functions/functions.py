import dropbox
from PIL import Image
from dropbox.exceptions import AuthError, ApiError
from app.settings.setting import Setting
from flask_login import current_user

def dropbox_get(file):
    settings = Setting.get()

    dbx = dropbox.Dropbox(settings.dropbox_token)

    try:
        dbx.files_get_metadata(url + file)
            
        link = dbx.files_get_temporary_link(url + file)

        return link.link
    except ApiError:
        return 0