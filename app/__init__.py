from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from config import DevConfig
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, logout_user
from functools import wraps
from babel.dates import format_datetime

app = Flask(__name__)
app.config.from_object(DevConfig)
mail = Mail(app)
csrf_protect = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"
app.jinja_env.filters['datetime'] = format_datetime

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
        if current_user.rol_id != 1 and current_user.rol_id != 2 and current_user.rol_id != 3 and current_user.rol_id != 4 and current_user.rol_id != 5 and current_user.rol_id != 6:
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
from app.communes.controllers import commune
from app.statuses_group.controllers import statuses_group
from app.statuses.controllers import statuses
from app.vacations.controllers import vacation
from app.hr_employees.controllers import hr_employee
from app.hr_days.controllers import hr_day
from app.absence_days.controllers import absence_day
from app.hr_employee_inputs.controllers import hr_employee_input
from app.calculation_values.controllers import calculation_value
from app.settlement_data.controllers import settlement_datum
from app.mesh_data.controllers import mesh_datum
from app.branch_offices.controllers import branch_office
from app.turns.controllers import turn
from app.employees_turns.controllers import employee_turn
from app.iclock.controllers import iclock
from app.clock_attendances.controllers import clock_attendance
from app.clock_users.controllers import clock_user
from app.clock_fingers.controllers import clock_finger
from app.clocks.controllers import clock
from app.home.controllers import home
from app.employee_extra_data.controllers import employee_extra_datum
from app.signatures.controllers import signature
from app.end_documents.controllers import end_document
from app.news.controllers import new
from app.progressive_vacations.controllers import progressive_vacation
from app.comments.controllers import comment
from app.uniforms.controllers import uniform
from app.checks.controllers import check
from app.check_answers.controllers import check_answer
from app.check_group_questions.controllers import check_group_question
from app.honoraries.controllers import honorary
from app.documentations.controllers import documentation
from app.employee_bank_accounts.controllers import employee_bank_account

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
app.register_blueprint(commune)
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
app.register_blueprint(hr_employee_input)
app.register_blueprint(calculation_value)
app.register_blueprint(settlement_datum)
app.register_blueprint(mesh_datum)
app.register_blueprint(branch_office)
app.register_blueprint(turn)
app.register_blueprint(employee_turn)
app.register_blueprint(iclock)
app.register_blueprint(clock_attendance)
app.register_blueprint(clock_user)
app.register_blueprint(clock_finger)
app.register_blueprint(clock)
app.register_blueprint(home)
app.register_blueprint(employee_extra_datum)
app.register_blueprint(signature)
app.register_blueprint(end_document)
app.register_blueprint(new)
app.register_blueprint(progressive_vacation)
app.register_blueprint(comment)
app.register_blueprint(uniform)
app.register_blueprint(check)
app.register_blueprint(check_answer)
app.register_blueprint(honorary)
app.register_blueprint(check_group_question)
app.register_blueprint(documentation)
app.register_blueprint(employee_bank_account)

@app.route("/")
def index():
    return redirect(url_for('auth.login'))
