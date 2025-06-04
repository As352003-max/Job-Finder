from .user import db  # Ensure db is correctly initialized and imported

class Application(db.Model):
    __tablename__ = 'applications'  # Explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    resume_path = db.Column(db.String(255), nullable=False)  # Path to resume file
    application_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50), default='pending')  # e.g., 'pending', 'reviewed', 'accepted', 'rejected'

    def __repr__(self):
        return f'<Application for Job {self.job_id} by User {self.applicant_id}>'
