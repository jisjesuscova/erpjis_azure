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

from app.auth.controllers import auth
from app.civil_states.controllers import civil_state
from app.contract_data.controllers import contract_datum
from app.contract_types.controllers import contract_type
from app.documental_management_data.controllers import documental_management_datum
from app.document_requests.controllers import document_request
from app.employees.controllers import employee
from app.genders.controllers import gender
from app.personal_data.controllers import personal_datum
from app.nationalities.controllers import nationality
from app.abandon_days.controllers import abandon_day
from app.family_core_data.controllers import family_core_datum
from app.kardex_data.controllers import kardex_datum
from app.medical_licenses.controllers import medical_license
from app.zones.controllers import zone
from app.principal.controllers import principal
from app.segment.controllers import segment
from app.healths.controllers import health
from app.pention.controllers import pention
from app.region.controllers import region
from app.communes.controllers import communes
from app.statuses_group.controllers import statuses_group
from app.statuses.controllers import statuses
from app.vacations.controllers import vacation
from app.hr_employees.controllers import hr_employee
from app.hr_days.controllers import hr_day
from app.absence_days.controllers import absence_day


app.register_blueprint(employee)
app.register_blueprint(auth)
app.register_blueprint(personal_datum)
app.register_blueprint(contract_datum)
app.register_blueprint(nationality)
app.register_blueprint(contract_type)
app.register_blueprint(gender)
app.register_blueprint(zone)
app.register_blueprint(principal)
app.register_blueprint(segment)
app.register_blueprint(health)
app.register_blueprint(pention)
app.register_blueprint(region)
app.register_blueprint(communes)
app.register_blueprint(statuses_group)
app.register_blueprint(statuses)
app.register_blueprint(civil_state)
app.register_blueprint(documental_management_datum)
app.register_blueprint(document_request)
app.register_blueprint(abandon_day)
app.register_blueprint(family_core_datum)
app.register_blueprint(kardex_datum)
app.register_blueprint(medical_license)
app.register_blueprint(vacation)
app.register_blueprint(hr_employee)
app.register_blueprint(hr_day)
app.register_blueprint(absence_day)

@app.route("/")
def hello():
    return "Hello, World! 2"
