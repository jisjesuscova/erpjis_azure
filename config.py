class BaseConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"
    SECRET_KEY = 'NoResponder2024'
    MAIL_SERVER = 'mail.jisparking.com'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'no-responder@jisparking.com'
    MAIL_PASSWORD = 'no-responder'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'no-responder@jisparking.com'
    UPLOAD_FOLDER = 'files/'
    REMEMBER_COOKIE_DURATION = 2592000

class ProConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"
    MAIL_SERVER = 'mail.jisparking.com'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'no-responder@jisparking.com'
    MAIL_PASSWORD = 'no-responder'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'no-responder@jisparking.com'
    UPLOAD_FOLDER = 'files/'
    REMEMBER_COOKIE_DURATION = 2592000
