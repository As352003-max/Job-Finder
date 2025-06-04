from flask import Blueprint, request, jsonify
from models.user import db, User
from models.job import Job
from models.applications import Application
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps

admin_bp = Blueprint('admin', __name__)

# ✅ Proper admin-required decorator using wraps
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user_identity = get_jwt_identity()
        if current_user_identity.get('role') != 'admin':
            return jsonify({"message": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper

# ✅ Get all users
@admin_bp.route('/users', methods=['GET'])
@admin_required
def get_all_users():
    users = User.query.all()
    output = [{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    } for user in users]
    return jsonify(output), 200

# ✅ Delete a user
@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
@admin_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {user.username} deleted successfully"}), 200

# ✅ Get all jobs with employer info
@admin_bp.route('/jobs', methods=['GET'])
@admin_required
def get_all_jobs_admin():
    jobs = Job.query.all()
    output = [{
        'id': job.id,
        'title': job.title,
        'company': job.company,
        'location': job.location,
        'description': job.description,
        'salary': job.salary,
        'posted_date': job.posted_date.isoformat(),
        'employer_id': job.employer_id,
        'employer_username': job.employer.username if job.employer else None
    } for job in jobs]
    return jsonify(output), 200

# ✅ Get all applications
@admin_bp.route('/applications', methods=['GET'])
@admin_required
def get_all_applications_admin():
    applications = Application.query.all()
    output = [{
        'id': app.id,
        'job_id': app.job_id,
        'job_title': app.job.title if app.job else None,
        'applicant_id': app.applicant_id,
        'applicant_username': app.applicant.username if app.applicant else None,
        'resume_path': app.resume_path,
        'application_date': app.application_date.isoformat(),
        'status': app.status
    } for app in applications]
    return jsonify(output), 200
