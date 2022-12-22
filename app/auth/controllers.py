from flask import Blueprint, render_template, redirect, url_for, request
from app.models.models import UserModel, EmployeeModel
from app.auth.forms import RegisterForm, LoginForm
from app.users.user import User
from app import db, login_manager
from flask_login import login_user, logout_user
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(meta={ 'crsf':True })

    if form.validate_on_submit():
        
        user = UserModel.query.filter_by(rut=form.rut.data).first()
        if user and user.check_password(form.password.data):
            print('Usuario Duplicado')
        else:
            user = User.store(request.form)

            login_user(user, remember=True)

            return redirect(next or url_for("employees.index"))
    if form.errors:
        print(form.errors)

    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    user = UserModel.query.filter_by(rut='18456789').first()
    
    rut = user.rut

    return str(rut)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
