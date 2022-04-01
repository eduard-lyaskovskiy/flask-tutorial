from flask import render_template, redirect, url_for, request, abort, g, flash, jsonify, session
from models.DbModels import Post, User
from models.FormModel import PostForm, UpdateForm
from controllers.UserController import login_required

def index():
    posts = Post.query\
    .join(User, Post.author_id == User.id)\
    .add_columns(Post.author_id, Post.title, Post.body, Post.id, Post.created, User.name)\
    .all()
    # .filter(users.id == friendships.friend_id)\
    # .filter(friendships.user_id == userID)\
    # .paginate(page, 1, False)
    return render_template("posts/index.html.j2", posts=posts)

@login_required
def store():
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
        form = PostForm()
        return render_template('posts/create.html.j2', form=form)

@login_required
def update(id):
    post = Post.query.filter(Post.id == id).one() 
    if request.method == 'POST':
        error = None
        
        title = request.form['title']
        body = request.form['body']

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)

        post_data = {
            'title' : title,
            'body': body
        }

        # try:
        post = Post(**post_data)
        post.update()
        return redirect(url_for('post_bp.get_post', id=post["id"]))
        # except:
        #     abort(422)
    else:
        form = UpdateForm()
        return render_template('posts/update.html.j2', form=form, post=post)

def get_post(id):
    post = Post.query.filter(Post.id == id).one()
    return render_template('posts/post_page.html.j2', post=post)

def destroy(self, *args, **kwargs):
    pass

# def getWeather():
#     request.