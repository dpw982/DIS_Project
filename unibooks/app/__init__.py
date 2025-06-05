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
    app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
    db.init_app(app)

    bcrypt.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    register_routes(app)
    with app.app_context():
        db.create_all()

    return app
