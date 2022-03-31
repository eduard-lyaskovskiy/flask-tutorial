from flask import Blueprint
from controllers.PostController import (
    index,
    store,
    update,
    get_post,
    destroy
)
post_bp = Blueprint('post_bp', __name__)
post_bp.route('/', methods=['GET'])(index)
post_bp.route('/create', methods=['POST', 'GET'])(store)
post_bp.route('/post/<int:id>', methods=('GET', 'POST'))(get_post)
post_bp.route('/post/<int:id>/update', methods=('GET', 'POST'))(update)
# post_bp.route('/<int:post_id>/edit', methods=['POST'])(update)
# post_bp.route('/<int:post_id>', methods=['DELETE'])(destroy)