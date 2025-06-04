
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

application_bp = Blueprint('applications', __name__)
applications = []

@application_bp.route('/', methods=['POST'])
@jwt_required()
def apply():
    data = request.json
    applications.append(data)
    return jsonify({"msg": "Applied"}), 201

@application_bp.route('/', methods=['GET'])
@jwt_required()
def list_applications():
    return jsonify(applications)
