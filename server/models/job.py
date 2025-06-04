from .user import db  # Make sure db is initialized in user.py or elsewhere and properly imported

class Job(db.Model):
    __tablename__ = 'jobs'  # Explicit table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.String(50))
    posted_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    employer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User table

    # One-to-many relationship: one job can have many applications
    applications = db.relationship('Application', backref='job', lazy=True)

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'
