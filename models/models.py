from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):  
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_email = Column(String, unique=True)
    user_pass = Column(String)

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
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(String)
    created = Column(TIMESTAMP)

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