import sys
from flask import render_template, redirect, url_for, request, abort
from models.Post import Post
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class PostController:
    def index(self, *args, **kwargs):
        pass
    def store(self, *args, **kwargs):
        pass
    def show(self, *args, **kwargs):
        pass
    def update(self, *args, **kwargs):
        pass
    def destroy(self, *args, **kwargs):
        pass