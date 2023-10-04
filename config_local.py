class BaseConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/erp_jis"

class DevConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/erp_jis"
    SECRET_KEY = '123456'
    MAIL_SERVER = 'mail.jisparking.com'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'no-responder@jisparking.com'
    MAIL_PASSWORD = 'no-responder'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'no-responder@jisparking.com'
    UPLOAD_FOLDER = 'files/'

class ProConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/erp_jis"
    MAIL_SERVER = 'mail.jisparking.com'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'no-responder@jisparking.com'
    MAIL_PASSWORD = 'no-responder'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'no-responder@jisparking.com'
    UPLOAD_FOLDER = 'files/'
