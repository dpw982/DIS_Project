from flask import Blueprint, jsonify
from ..models import Book

# This file defines the routes for the books API

books_bp = Blueprint('books', __name__)

@books_bp.route('/books')
def get_books():
  books = Book.query.all()
  return jsonify([Book.to_dict(book) for book in books])
