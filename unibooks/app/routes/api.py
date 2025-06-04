from flask import Blueprint, request, jsonify
from app.models import Studyline

api_bp = Blueprint('api', __name__)

# Get all studylines
@api_bp.route('/get_studylines')
def get_studylines():
  pass

# Get all years for a specific studyline
@api_bp.route('/get_years')
def get_years():
  pass

# Get all books for a specific studyline and year
@api_bp.route('/get_books')
def get_books():
  pass