
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

job_bp = Blueprint('jobs', __name__)
jobs = []

@job_bp.route('/', methods=['POST'])
@jwt_required()
def post_job():
    data = request.json
    jobs.append(data)
    return jsonify({"msg": "Job posted"}), 201

@job_bp.route('/', methods=['GET'])
def get_jobs():
    return jsonify(jobs)
