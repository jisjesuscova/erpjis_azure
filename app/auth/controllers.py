from flask import Blueprint, render_template, redirect, url_for, request
from app.models.models import UserModel, EmployeeModel
from app.auth.forms import RegisterForm, LoginForm
from app.users.user import User
from app import db, login_manager
from flask_login import login_user, logout_user
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "Probando"