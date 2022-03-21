import functools
import imp

from flask import render_template, redirect, url_for, request, abort, g
from models.models import Post
# from UserController import UserController
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class PostController():
    def index():
        return render_template('base.html.j2')

    # @UserController.login_required
    # def store(self):
    #     body = request.get_json()
    #     error = None

    #     post_title = body.get('post_title', None)
    #     post_body = body.get('post_body', None) 


    def show(self, *args, **kwargs):
        pass
    def update(self, *args, **kwargs):
        pass
    def destroy(self, *args, **kwargs):
        pass