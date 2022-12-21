from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import DevConfig
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, logout_user
from functools import wraps

app = Flask(__name__)
app.config.from_object(DevConfig)
csrf_protect = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"

def rol_admin_need(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if current_user.rol_id != 2:
            logout_user()
            return redirect(url_for('auth.login'))
            ## print('rol:' + str(current_user.rol_id))
            ## login_manager.unauthorized()
        return f(*args, **kwds)
    return wrapper

def regular_employee_rol_need(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if current_user.rol_id != 1:
            logout_user()
            return redirect(url_for('auth.login'))
            ## print('rol:' + str(current_user.rol_id))
            ## login_manager.unauthorized()
        return f(*args, **kwds)
    return wrapper

def human_resource_rol_need(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if current_user.rol_id != 3:
            logout_user()
            return redirect(url_for('auth.login'))
            ## print('rol:' + str(current_user.rol_id))
            ## login_manager.unauthorized()
        return f(*args, **kwds)
    return wrapper

from app.civil_states.controllers import civil_state

app.register_blueprint(civil_state)

@app.route("/")
def hello():
    return "Hello, World! 2"
