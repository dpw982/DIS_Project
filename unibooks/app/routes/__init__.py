from .books import books_bp
from .users import users_bp
from .main import main_bp
from .api import api_bp
from .search import search_bp

# Register all the routes for the application.

def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(search_bp)
