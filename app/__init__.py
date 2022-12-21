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

@app.route("/")
def hello():
    return "Hello, World! 2"
