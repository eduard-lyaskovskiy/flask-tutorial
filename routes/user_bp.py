from flask import Blueprint
from controllers.UserController import UserController

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(UserController.index)
user_bp.route('/create', methods=['POST'])(UserController.store)
user_bp.route('/<int:user_id>', methods=['GET'])(UserController.show)
user_bp.route('/<int:user_id>/edit', methods=['POST'])(UserController.update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(UserController.destroy)