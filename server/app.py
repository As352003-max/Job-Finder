from flask import Flask
from config import Config
from models.user import db # Import db from user.py
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Import blueprints
from routes.auth_routes import auth_bp
from routes.job_routes import job_bp
from routes.resume_routes import resume_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # example with SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize extensions
db.init_app(app) # Initialize SQLAlchemy with the app
CORS(app) # Enable CORS for all routes
jwt = JWTManager(app) # Initialize Flask-JWT-Extended

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(job_bp, url_prefix='/jobs')
app.register_blueprint(resume_bp, url_prefix='/resumes')
app.register_blueprint(admin_bp, url_prefix='/admin')

# Create database tables within the application context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)