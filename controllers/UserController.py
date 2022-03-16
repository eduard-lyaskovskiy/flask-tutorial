import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class UserController:

    def index():
        users = User.query.order_by(User.id).all()
        if len(users) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'users': users
        })

    def store():
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        try:
            user = User(name=name, age=age)
            user.create()
            return jsonify({
                'success': True,
                'created': user.format()
            })
        except:
            abort(422)

    def show(user_id):
        return f'{user_id}'

    def update(self, *args, **kwargs):
        pass

    def destroy(self, *args, **kwargs):
        pass