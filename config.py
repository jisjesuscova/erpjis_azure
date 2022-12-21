class BaseConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:@erpjis.mysql.database.azure.com:3306/erp_jis"

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:@erpjis.mysql.database.azure.com:3306/erp_jis"
    SECRET_KEY = '123456'

class ProConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:@erpjis.mysql.database.azure.com:3306/erp_jis"
