from flask import Blueprint, jsonify
from .models import Book

main = Blueprint('main', __name__)

@main.route('/books')
def get_books():
  books = Book.query.all()
  return jsonify([{"isbn": b.isbn, "title": b.title} for b in books])
