from flask import Blueprint, request, jsonify
from models.user import db, User
from models.job import Job
from models.applications import Application
from flask_jwt_extended import jwt_required, get_jwt_identity
import os
from werkzeug.utils import secure_filename

job_bp = Blueprint('job', __name__)

# Define allowed extensions for resume uploads
UPLOAD_FOLDER = 'uploads/resumes'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@job_bp.route('/', methods=['GET'])
def get_all_jobs():
    """Fetches all available job listings."""
    jobs = Job.query.all()
    output = []
    for job in jobs:
        output.append({
            'id': job.id,
            'title': job.title,
            'company': job.company,
            'location': job.location,
            'description': job.description,
            'salary': job.salary,
            'posted_date': job.posted_date.isoformat(),
            'employer_id': job.employer_id
        })
    return jsonify(output), 200

@job_bp.route('/<int:job_id>', methods=['GET'])
def get_job_by_id(job_id):
    """Fetches a single job listing by ID."""
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"message": "Job not found"}), 404
    return jsonify({
        'id': job.id,
        'title': job.title,
        'company': job.company,
        'location': job.location,
        'description': job.description,
        'salary': job.salary,
        'posted_date': job.posted_date.isoformat(),
        'employer_id': job.employer_id
    }), 200

@job_bp.route('/', methods=['POST'])
@jwt_required()
def post_job():
    """Allows an employer to post a new job."""
    current_user_identity = get_jwt_identity()
    user_id = current_user_identity['id']
    user_role = current_user_identity['role']

    if user_role != 'employer':
        return jsonify({"message": "Unauthorized: Only employers can post jobs"}), 403

    data = request.get_json()
    title = data.get('title')
    company = data.get('company')
    location = data.get('location')
    description = data.get('description')
    salary = data.get('salary')

    if not all([title, company, location, description]):
        return jsonify({"message": "Missing required job fields"}), 400

    new_job = Job(
        title=title,
        company=company,
        location=location,
        description=description,
        salary=salary,
        employer_id=user_id
    )
    db.session.add(new_job)
    db.session.commit()

    return jsonify({"message": "Job posted successfully!", "job_id": new_job.id}), 201

@job_bp.route('/<int:job_id>/apply', methods=['POST'])
@jwt_required()
def apply_for_job(job_id):
    """Allows an applicant to apply for a job with a resume upload."""
    current_user_identity = get_jwt_identity()
    applicant_id = current_user_identity['id']
    user_role = current_user_identity['role']

    if user_role != 'applicant':
        return jsonify({"message": "Unauthorized: Only applicants can apply for jobs"}), 403

    job = Job.query.get(job_id)
    if not job:
        return jsonify({"message": "Job not found"}), 404

    # Check if the user has already applied for this job
    existing_application = Application.query.filter_by(
        job_id=job_id, applicant_id=applicant_id
    ).first()
    if existing_application:
        return jsonify({"message": "You have already applied for this job"}), 409

    if 'resume' not in request.files:
        return jsonify({"message": "No resume file part"}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Create a user-specific folder for resumes
        user_resume_folder = os.path.join(UPLOAD_FOLDER, str(applicant_id))
        os.makedirs(user_resume_folder, exist_ok=True)

        resume_path = os.path.join(user_resume_folder, filename)
        file.save(resume_path)

        new_application = Application(
            job_id=job_id,
            applicant_id=applicant_id,
            resume_path=resume_path,
            status='pending'
        )
        db.session.add(new_application)
        db.session.commit()

        return jsonify({"message": "Application submitted successfully!", "application_id": new_application.id}), 201
    else:
        return jsonify({"message": "Invalid file type. Allowed types: pdf, docx"}), 400
