from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)  # Enough for secure hashes
    role = db.Column(db.String(20), nullable=False, default='applicant')  # 'applicant', 'employer', 'admin'

    # Relationships
    applications = db.relationship('Application', backref='user', lazy=True)
    posted_jobs = db.relationship('Job', backref='user', lazy=True)

    def set_password(self, password):
        """Hashes and stores the password using scrypt (or fallback)."""
        self.password_hash = generate_password_hash(password, method='scrypt')

    def check_password(self, password):
        """Checks if the given password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
