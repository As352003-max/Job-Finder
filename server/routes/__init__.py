from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize SQLAlchemy globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from a separate config file (e.g., config.py)
    app.config.from_object('config.Config')  # Make sure config.py exists with Config class

    # Initialize extensions
    db.init_app(app)
    CORS(app)  # Enable Cross-Origin requests

    # Import models to register them with SQLAlchemy
    from .models.user import User
    from .models.job import Job
    from .models.application import Application

    # Register blueprints if using modular routes
    # from .routes.auth import auth_bp
    # from .routes.jobs import jobs_bp
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(jobs_bp)

    return app
