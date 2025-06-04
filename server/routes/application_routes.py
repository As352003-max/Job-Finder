
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import db, User
from models.job import Job
from models.application import Application

application_bp = Blueprint('applications', __name__)

@application_bp.route('/', methods=['POST'])
@jwt_required()
def apply():
    data = request.get_json()
    job_id = data.get('job_id')
    resume_path = data.get('resume_path')  # Assuming file upload handled separately

    # Validate input
    if not job_id or not resume_path:
        return jsonify({"msg": "Missing job_id or resume_path"}), 400

    # Get user identity
    current_user = get_jwt_identity()
    applicant_id = current_user['id']

    # Check if job exists
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"msg": "Job not found"}), 404

    # Optional: check if user already applied
    existing_application = Application.query.filter_by(job_id=job_id, applicant_id=applicant_id).first()
    if existing_application:
        return jsonify({"msg": "Already applied to this job"}), 409

    # Create application
    new_app = Application(
        job_id=job_id,
        applicant_id=applicant_id,
        resume_path=resume_path
    )
    db.session.add(new_app)
    db.session.commit()

    return jsonify({"msg": "Application submitted successfully"}), 201

@application_bp.route('/', methods=['GET'])
@jwt_required()
def list_applications():
    current_user = get_jwt_identity()
    user_id = current_user['id']

    # Get applications submitted by this user
    applications = Application.query.filter_by(applicant_id=user_id).all()
    result = [{
        'id': app.id,
        'job_id': app.job_id,
        'job_title': app.job.title if app.job else None,
        'resume_path': app.resume_path,
        'application_date': app.application_date.isoformat(),
        'status': app.status
    } for app in applications]

    return jsonify(result), 200
