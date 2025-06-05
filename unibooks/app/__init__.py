from flask import Flask
from .database import db
from .routes import register_routes
from config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv() 
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')  # Use environment variable or default for development
    db.init_app(app)

    bcrypt.init_app(app)  # Initialize Flask-Bcrypt for password hashing
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Redirect to login page if not authenticated
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Load user by ID for Flask-Login


    register_routes(app)  # Register the routes
    with app.app_context():
        db.create_all()   # Create database tables if they don't exist

    return app