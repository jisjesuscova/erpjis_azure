from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.models import UserModel
from app.auth.forms import RegisterForm, LoginForm, RecoverForm, PasswordForm
from app.users.user import User
from app import login_manager, mail
from flask_login import login_user, logout_user, current_user
from flask_mail import Message
from app.rols.rol import Rol
from app.helpers.whatsapp import Whatsapp
from werkzeug.security import generate_password_hash

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
@auth.route('/password', methods=['POST'])
def password(id = '', api_token = ''):
    form = PasswordForm(meta={ 'crsf':True })

    if form.validate_on_submit():
        
        User.special_update(form.rut.data, form.password.data)

        flash('Se ha actualizado la contraseña con éxito.', 'success')
        print(form.rut.data)
        Whatsapp.send(form.rut.data, 1, 1, 17)

        return redirect(url_for("auth.login"))
    else:
        qty = User.check_user_exists_by_token(api_token)

        if qty > 0:
            user = User.get_by_id(id)

            return render_template("password.html", form=form, rut=user.visual_rut)
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
            logo = 'https://jiserp.com/static/dist/img/logo.png'
            url = 'https://jiserp.com/password/' + str(user.id) + '/' + str(user.api_token)
            msg.html = render_template('emails/recover.html', logo=logo, full_name=user.nickname, url=url)
            mail.send(msg)

            flash('Dirigete a tu casilla de correo para hacer el cambio de tu contraseña.', 'success')

            return redirect(url_for("auth.login"))
        else:
            flash('No se ha encontrado el usuario.', 'error')

            return redirect(url_for("auth.recover"))

    return render_template('recover.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
@auth.route('/login/<api_token>', methods=['GET'])
def login(api_token = ''):
    form = LoginForm(meta={ 'crsf':True })
    
    if form.validate_on_submit():
        user = UserModel.query.filter_by(visual_rut=form.rut.data).first() 

        if user and user.check_password(form.password.data):
            if user.status_id == 0:
                return redirect(url_for("auth.refresh_status", id=user.id))
            else:
                login_user(user)

                next = request.form['next']

                if current_user.rol_id == 4:
                    return redirect(next or url_for("home.index"))
                else:
                    return redirect(next or url_for("personal_data.show", rut=user.rut))
        else:
            flash('El RUT o Contraseña es incorrecto.', 'error')

            return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)

@auth.route('/refresh_status/<int:id>', methods=['GET', 'POST'])
def refresh_status(id):
    form = PasswordForm(meta={ 'crsf':True })

    user = User.get_by_id(id)

    return render_template("refresh_status.html", form=form, rut=user.visual_rut)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
