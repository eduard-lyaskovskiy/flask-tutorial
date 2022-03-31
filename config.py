import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://leskov:leskov@localhost:5432/flask-tutorial'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
#DEV Flask-SQLAlchemy 
SQLALCHEMY_ECHO = True
#Weather secret key
WEATHER_API_KEY = 'ebe025c190be480fbcc74129223103'