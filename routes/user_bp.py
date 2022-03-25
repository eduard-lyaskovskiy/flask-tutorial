from flask import Blueprint
from controllers.UserController import (
    login, 
    store, 
    logout,
    user_bp
    )

user_bp.route('/login', methods=['POST', 'GET'])(login)
user_bp.route('/register', methods=['POST', 'GET'])(store)
user_bp.route('/logout', methods=['GET'])(logout)