from flask import Flask
from .database import db
from .routes import register_routes
from config import Config



def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    db.init_app(app)
    
    register_routes(app)  # Register the routes

    with app.app_context():
        db.create_all()   # Create database tables if they don't exist

    return app