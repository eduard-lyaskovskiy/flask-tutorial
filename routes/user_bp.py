from flask import Blueprint
from controllers.UserController import (
    login, 
    store, 
    show, 
    update, 
    destroy,
    logout,
    user_bp
    )

user_bp.route('/login', methods=['POST', 'GET'])(login)
user_bp.route('/register', methods=['POST', 'GET'])(store)
user_bp.route('/logout', methods=['GET'])(logout)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)