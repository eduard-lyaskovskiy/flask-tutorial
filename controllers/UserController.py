import sqlalchemy
import functools

from flask import Blueprint, render_template, redirect, url_for, request, abort, flash, session, g

from models.DbModels import User
from models.FormModel import LoginForm, RegisterForm

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()
user_bp = Blueprint('user_bp', __name__)

def login():
    form = LoginForm()
    if request.method == 'POST':
        error = None
        user_email = request.form['user_email']
        user_pass = request.form['user_pass']

        fetch_user = User.query.filter(User.user_email == user_email).one_or_none()

        if fetch_user is None:
            error =  f'Incorrect username {user_email}'
        else:
            user = fetch_user.format()
            check_pass = check_password_hash(user['user_pass'], user_pass) 

            if check_pass is False:
                error = f'Incorrect password for {user_email}'

            if error is None:
                session.clear()
                session["user_id"] = user["id"] 
                return redirect('/')
        flash(error)

    return render_template('auth/login.html.j2', form=form, title='Login')

@user_bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter(User.id == user_id).one_or_none().format()

def store():
    form = RegisterForm()
    if request.method == 'POST':
        error = None
        name = request.form['name']
        user_email = request.form['user_email']
        user_pass = request.form['user_pass']

        if not name:
            error = 'Name is required'
        elif not user_email:
            error = 'Email is required'
        if not user_pass:
            error = 'Password is required'
        else:
            user_pass_hashed = generate_password_hash(user_pass)

        user_data = {
            'name' : name,
            'user_email' : user_email,
            'user_pass' : user_pass_hashed,
        }
        
        if error is None:
            try:
                user = User(**user_data)
                user.create()
                return redirect(url_for('user_bp.login'))
            except sqlalchemy.exc.IntegrityError:
                error = f'User {user_email} already exist!'
            except:
                abort(422)
        
        flash(error)

    return render_template('auth/register.html.j2', title='Register', form=form)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("post_bp.index"))

        return view(**kwargs)

    return wrapped_view

def logout():
    session.clear()
    return redirect('/')