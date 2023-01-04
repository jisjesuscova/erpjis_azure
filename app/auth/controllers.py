from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models.models import UserModel
from app.auth.forms import RegisterForm, LoginForm, RecoverForm
from app.users.user import User
from app import login_manager, mail
from flask_login import login_user, logout_user
from flask_mail import Message

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

@auth.route('/password/<id>/<api_token>', methods=['GET'])
def password(id, api_token):
    qty = User.check_user_exists_by_token(api_token)

    if qty > 0:
        user = User.get_by_id(id)

        login_user(user)

        session['rut'] = user.rut
        session['visual_rut'] = user.visual_rut
        session['nickname'] = user.nickname

        return redirect(url_for("employees.index"))
    else:
        flash('No se ha encontrado el usuario.', 'error')

        return redirect(url_for("auth.login"))

@auth.route('/recover', methods=['GET', 'POST'])
def recover():
    form = RecoverForm(meta={ 'crsf':True })

    if form.validate_on_submit():

        qty = User.check_user_exists(form.rut.data)

        if qty > 0:
            user = User.get_by_rut(form.rut.data)
            msg = Message('Recuperar Contraseña', recipients = [form.email.data])
            logo = 'https://erpjis.azurewebsites.net/static/dist/img/logo.png'
            url = 'https://erpjis.azurewebsites.net/password/' + str(user.id) + '/' + str(user.api_token)
            msg.html = render_template('emails/recover.html', logo=logo, full_name=user.nickname, url=url)
            mail.send(msg)

            flash('Dirigete a tu casilla de correo para hacer el cambio de tu contraseña.', 'success')

            return redirect(url_for("auth.login"))
        else:
            flash('No se ha encontrado el usuario.', 'error')

            return redirect(url_for("auth.recover"))

    return render_template('recover.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={ 'crsf':True })
    
    if form.validate_on_submit():
        
        user = UserModel.query.filter_by(visual_rut=form.rut.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)

            session['rut'] = user.rut
            session['visual_rut'] = user.visual_rut
            session['nickname'] = user.nickname

            next = request.form['next']

            return redirect(next or url_for("employees.index"))
        else:
            flash('El RUT o Contraseña es incorrecto.', 'error')

            return redirect(url_for('auth.login'))

    if form.errors:
        print(form.errors)

    return render_template('login.html', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
