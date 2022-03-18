import sqlalchemy
from flask import render_template, redirect, url_for, request, abort, jsonify, flash, session
from models.User import User
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class UserController:

    def index():
        users = User.query.order_by(User.id).all()
        print(users)
        if len(users) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'users': f'{users}'
        })

    def login():
        body = request.get_json()

        """
            TODO 
            * add flash errors
        """
        error = None

        user_email = body.get('user_email', None)
        user_pass = body.get('user_pass', None)

        fetch_user = User.query.filter(User.user_email == user_email).one_or_none()

        try:
            user = fetch_user.format()
        except AttributeError:
            return jsonify({
                'error': f'Incorrect username {user_email}'
            })

        check_pass = check_password_hash(user['user_pass'], user_pass) 

        if check_pass:
            return jsonify({
                'answer': 'good'
            })
        else:
            return jsonify({
                'error': f'Incorrect password for {user_email}'
            })

    def store():
        """
            TODO 
            * check id insert in DB
        """
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
                return jsonify({
                    'success': True,
                    'created': user.format()
                })
            except sqlalchemy.exc.IntegrityError:
                error = f'User {user_email}  already exist!'
                return jsonify({
                    'success': False,
                    'error': error
                })
            except:
                abort(422)
        else:
            return jsonify({
                    'success': False,
                    'error': error
                })

        # flash(error, 'error')

    def show(user_id):
        return f'{user_id}'

    def update(self, *args, **kwargs):
        pass

    def destroy(self, *args, **kwargs):
        pass