
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
def list_users():
    from .auth_routes import users
    return jsonify(list(users.keys()))
