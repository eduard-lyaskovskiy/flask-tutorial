from flask import Flask, render_template
from flask_migrate import Migrate

from models.models import db
from routes.user_bp import user_bp
from routes.post_bp import post_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(post_bp, url_prefix='/')

# @app.route('/')
# def index():
#     return render_template('base.html.j2')
    
if __name__ == '__main__':
    app.debug = True
    app.run()