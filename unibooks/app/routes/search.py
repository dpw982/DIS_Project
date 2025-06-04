from flask import Blueprint, request, jsonify
import requests

search_bp = Blueprint('search', __name__)

@search_bp.route('/search_books')
def search_books():
    query = request.args.get('q')
    if not query:
      return jsonify({"error": "Missing query"}), 400
    
    url = 'https://openlibrary.org/search.json'
    params = {'title': query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Open Library API error'}), 502