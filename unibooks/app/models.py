from . import db

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  isbn = db.Column(db.String(13), unique=True, nullable=False)
  title = db.Column(db.String(200), nullable=False)
  author = db.Column(db.String(200), nullable=True)