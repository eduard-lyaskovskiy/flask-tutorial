from flask import Blueprint
from controllers.PostController import PostController

post_bp = Blueprint('post_bp', __name__)
post_bp.route('/', methods=['GET'])(PostController.index)
# post_bp.route('/create', methods=['POST'])(PostController.store)
# post_bp.route('/<int:post_id>', methods=['GET'])(PostController.show)
# post_bp.route('/<int:post_id>/edit', methods=['POST'])(PostController.update)
# post_bp.route('/<int:post_id>', methods=['DELETE'])(PostController.destroy)