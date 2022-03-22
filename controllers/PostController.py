from flask import render_template, redirect, url_for, request, abort, g
from models.DbModels import Post
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def index():
    posts = {
        'id' : 1,
        'author_id' : 3,
        'title' : 'From postcontroller title 1',
        'body' : 'From postcontroller title 1',
        'created' : 1646896817
    }
    return render_template("posts/index.html.j2", posts=posts)

def create():
    if request.method == "POST":
        body = request.get_json()
        error = None

        post_title = body.get('post_title', None)
        post_body = body.get('post_body', None) 
    else:
        return render_template('posts/create.html.j2')

def update(self, *args, **kwargs):
    pass
def destroy(self, *args, **kwargs):
    pass