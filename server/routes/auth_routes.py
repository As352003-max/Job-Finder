from flask import Blueprint, request, jsonify
from models.user import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

# ✅ Register a new user
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'applicant')  # Default role is 'applicant'

    # Check required fields
    if not all([username, email, password]):
        return jsonify({"message": "Missing username, email, or password"}), 400

    # Ensure uniqueness
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 409
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already taken"}), 409

    # Create and save user
    new_user = User(username=username, email=email, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

# ✅ Login and generate JWT token
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({"message": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={
            'id': user.id,
            'role': user.role,
            'username': user.username
        })
        return jsonify({
            "message": "Login successful!",
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }), 200

    return jsonify({"message": "Invalid credentials"}), 401

# ✅ Protected route (example)
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_identity = get_jwt_identity()
    return jsonify(logged_in_as=current_user_identity), 200
