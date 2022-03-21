import sqlalchemy
import functools
# from routes.user_bp import user_bp
from flask import Blueprint, render_template, redirect, url_for, request, abort, jsonify, flash, session, g

from models.models import User

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class UserController:

    def login():
        if request.method == 'POST':

            """
                TODO 
                * add flash errors
            """
            error = None

            user_email = request.form['user_email']
            user_pass = request.form['user_pass']

            fetch_user = User.query.filter(User.user_email == user_email).one_or_none()

            try:
                user = fetch_user.format()
            except AttributeError:
                error =  f'Incorrect username {user_email}'
                

            check_pass = check_password_hash(user['user_pass'], user_pass) 

            if check_pass is False:
                error = f'Incorrect password for {user_email}'

            if error is None:
                session.clear()
                session["user_id"] = user["id"]
                print(session)
                return redirect('/')

            flash(error, 'error')

        return render_template('auth/login.html.j2')

    def store():
        """
            TODO 
            * check id insert in DB
        """
        if request.method == 'POST':
            body = request.get_json()
            error = None
            name = body.get('name', None)
            user_email = body.get('user_email', None)
            user_pass = body.get('user_pass', None)

            if not name:
                error = 'Name is required'
            elif not user_email:
                error = 'Email is required'
            if not user_pass:
                error = 'Password is required'
            else:
                user_pass_hashed = generate_password_hash(user_pass)

            user = {
                'name' : name,
                'user_email' : user_email,
                'user_pass' : user_pass_hashed,
            }
            
            if error is None:
                try:
                    user = User(**user)
                    user.create()
                    return redirect(url_for('self.login'))
                except sqlalchemy.exc.IntegrityError:
                    error = f'User {user_email}  already exist!'
                except:
                    abort(422)
            else:
                return flash(error, 'error')

            flash(error, 'error')

        return render_template('auth/register.html.j2')

    def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return redirect(url_for("self.index"))

            return view(**kwargs)

        return wrapped_view

    @Blueprint.before_app_request('load_logged_in_user')
    def load_logged_in_user():
        """If a user id is stored in the session, load the user object from
        the database into ``g.user``."""
        user_id = session.get("user_id")

        if user_id is None:
            g.user = None
        else:
            g.user = (
                # get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
                User.query.filter(User.id == user_id).one_or_none()
            )

    def show(user_id):
        return f'{user_id}'

    def update(self, *args, **kwargs):
        pass

    def destroy(self, *args, **kwargs):
        pass