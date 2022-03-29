from flask import Flask, render_template, g, session, redirect, url_for
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from models.DbModels import db
from routes.user_bp import user_bp
from routes.post_bp import post_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(post_bp, url_prefix='/')
Bootstrap(app)

if __name__ == '__main__':
    app.debug = True
    app.run()