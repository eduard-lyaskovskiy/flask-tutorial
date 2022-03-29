from distutils.command.config import config
from flask import render_template, redirect, url_for, request, abort, g, flash, jsonify, session
from models.DbModels import Post, User
from models.FormModel import PostForm
from controllers.UserController import login_required

def index():
    posts = Post._get_posts()
    return render_template("posts/index.html.j2", posts=posts)

@login_required
def store():
    form = PostForm()
    if request.method == "POST":
        error = None
        
        title = request.form['title']
        body = request.form['body']

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)

        post_data = {
            'title' : title,
            'body': body,
            'author_id': g.user['id']
        }

        try:
            post = Post(**post_data)
            post.create()
            return redirect(url_for('post_bp.index'))
        except:
            abort(422)

    else:
        return render_template('posts/create.html.j2', form=form)

def update(id):
    if request.method == 'POST':
        pass
    else:
        post = Post.query.filter(Post.id ==id).one()
        return render_template('posts/post_page.html.j2', post=post)

def destroy(self, *args, **kwargs):
    pass