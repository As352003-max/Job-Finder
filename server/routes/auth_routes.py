
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

users = {}

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    users[data['email']] = data
    return jsonify({"msg": "User registered"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users.get(data['email'])
    if user and user['password'] == data['password']:
        token = create_access_token(identity=data['email'])
        return jsonify(access_token=token)
    return jsonify({"msg": "Bad credentials"}), 401
