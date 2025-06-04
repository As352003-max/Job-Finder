from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import db, User
from models.applications import Application
from utils.resume_parser import parse_resume
import os

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/parse/<int:application_id>', methods=['GET'])
@jwt_required()
def get_parsed_resume(application_id):
    """
    Allows an employer or admin to parse and view a resume from an application.
    Employers can only access applications for their own jobs.
    """
    current_user = get_jwt_identity()
    user_id = current_user['id']
    user_role = current_user['role']

    # Role check
    if user_role not in ['employer', 'admin']:
        return jsonify({"message": "Unauthorized: Only employers or admins can parse resumes"}), 403

    # Fetch application with related job
    application = Application.query.get(application_id)
    if not application:
        return jsonify({"message": "Application not found"}), 404

    job = getattr(application, 'job', None)  # Ensure relationship is available
    if not job:
        return jsonify({"message": "Associated job not found"}), 404

    # Employers can only view resumes for jobs they posted
    if user_role == 'employer' and job.employer_id != user_id:
        return jsonify({"message": "Forbidden: You do not own this job's application"}), 403

    resume_file_path = application.resume_path
    if not os.path.exists(resume_file_path):
        return jsonify({"message": "Resume file not found on server"}), 404

    # Parse resume using utility
    try:
        parsed_data = parse_resume(resume_file_path)
    except Exception as e:
        return jsonify({"message": "Failed to parse resume", "error": str(e)}), 500

    return jsonify({
        "application_id": application.id,
        "applicant_id": application.applicant_id,
        "job_id": application.job_id,
        "parsed_resume_data": parsed_data
    }), 200
