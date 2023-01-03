from flask import Blueprint, render_template, redirect, url_for, request
from app.models.models import UserModel
from app.auth.forms import RegisterForm, LoginForm, RecoverForm
from app.users.user import User
from app import login_manager
from flask_login import login_user, logout_user

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

@auth.route('/recover', methods=['GET', 'POST'])
def recover():
    form = RecoverForm(meta={ 'crsf':True })

    if form.validate_on_submit():
        qty = User.check_user_exists(form.rut.data)

        if qty > 0:
            status = User.send_email(form.email.data)

            print(status)
            return redirect(url_for('auth.login'))

    return render_template('recover.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={ 'crsf':True })
    
    if form.validate_on_submit():
        
        user = UserModel.query.filter_by(rut=form.rut.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)

            next = request.form['next']
            print(next)
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.

            return redirect(next or url_for("employees.index"))
        else:
            return redirect(url_for('auth.login'))

    if form.errors:
        print(form.errors)
    
    return render_template('login.html', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
