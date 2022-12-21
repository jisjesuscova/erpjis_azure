from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import ProConfig
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, logout_user
from functools import wraps

app = Flask(__name__)
