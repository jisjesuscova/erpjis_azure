class BaseConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"
    SECRET_KEY = '123456'
    MAIL_SERVER = 'mail.jisparking.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'jesuscova@jisparking.com'
    MAIL_PASSWORD = 'Jgames88'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class ProConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"
    MAIL_SERVER = 'mail.jisparking.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'jesuscova@jisparking.com'
    MAIL_PASSWORD = 'Jgames88'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

