from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String(120))
    address = db.Column(db.String(120))
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address
        }