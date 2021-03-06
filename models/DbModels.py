from datetime import datetime
<<<<<<< HEAD
=======
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
>>>>>>> 9b14c557d655039ec4f87c52d873b3d1038029e3
from flask_sqlalchemy import SQLAlchemy
from flask import g

db = SQLAlchemy()

class User(db.Model):  
    __tablename__: str = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_email = db.Column(db.String, unique=True)
    user_pass = db.Column(db.String)
    posts = db.relationship('Post', backref='users', lazy='dynamic')

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.user_email = kwargs['user_email']
        self.user_pass = kwargs['user_pass']

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_email': self.user_email,
            'user_pass': self.user_pass,
        }

class Post(db.Model):
    __tablename__: str = 'posts'

    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
=======
    author_id = db.Column(db.Integer, ForeignKey('users.id'))
>>>>>>> 9b14c557d655039ec4f87c52d873b3d1038029e3
    title = db.Column(db.String)
    body = db.Column(db.String)
    created = db.Column(db.TIMESTAMP, default=datetime.now())

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.body = kwargs['body']
        self.author_id = kwargs['author_id']

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'author_id': self.author_id,
            'title': self.title,
            'body': self.body,
            'created': self.created,
        }
    
<<<<<<< HEAD
    # def _get_posts():
    #     return db.engine.execute('''
    #     SELECT p.id, title, body, created, author_id, name
    #     FROM posts p JOIN users u ON p.author_id = u.id
    #     ORDER BY created DESC''')
=======
    def _get_posts():
        return db.engine.execute('''
        SELECT p.id, title, body, created, author_id, name
        FROM posts p JOIN users u ON p.author_id = u.id
        ORDER BY created DESC''')
>>>>>>> 9b14c557d655039ec4f87c52d873b3d1038029e3
