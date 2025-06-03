from .database import db

# Define models for the Database
# These models represent the structure of the Database tables



class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  isbn = db.Column(db.String(13), unique=True, nullable=False)
  title = db.Column(db.String(200), nullable=False)
  author = db.Column(db.String(200), nullable=True)

  def to_dict(self):
    return {
      'id': self.id,
      'isbn': self.isbn,
      'title': self.title,
      'author': self.author
    }

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password_hash = db.Column(db.String(128), nullable=False)

  def to_dict(self):
    return {
      'id': self.id,
      'username': self.username,
      'email': self.email
    }

class University(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  studylines = db.relationship('Studyline', backref='university', lazy=True)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
    }

class Studyline(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'university_id': self.university_id
    }