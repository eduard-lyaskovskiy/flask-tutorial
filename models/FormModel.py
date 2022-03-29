from distutils.text_file import TextFile
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, StringField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_email = EmailField('Email', validators=[DataRequired()])
    user_pass = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    user_email = EmailField('Email', validators=[DataRequired()])
    user_pass = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body')
    submit = SubmitField('Save')