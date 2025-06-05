from .database import db
from flask_login import UserMixin

# Define models for the Database
# These models represent the structure of the Database tables


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
        }


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        from app import bcrypt  # Import bcrypt here to avoid circular import issues
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        from app import bcrypt
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

class Sales_Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(200), nullable=False)      # Add this line
    author = db.Column(db.String(200), nullable=True)      # Add this line
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_filename = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    user = db.relationship("User", backref="sales_listings", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "isbn": self.isbn,
            "title": self.title,           # Add this line
            "author": self.author,         # Add this line
            "user_id": self.user_id,
            "price": self.price,
            "image_filename": self.image_filename,
            "user": self.user.to_dict() if self.user else None,
            "description": self.description,
        }