from flask import Blueprint, request, jsonify
import requests
import re
from app.models import Sales_Listing

search_bp = Blueprint("search", __name__)


@search_bp.route("/search_titles")
def search_titles():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"intitle:{query}", "maxResults": 10}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return jsonify({"error": "Google Books API error"}), 502

    data = response.json()
    results = []
    for item in data.get("items", []):
        volume = item.get("volumeInfo", {})
        results.append(
            {
                "title": volume.get("title"),
                "author_name": volume.get("authors", []),
                "isbn": [
                    id["identifier"]
                    for id in volume.get("industryIdentifiers", [])
                    if id["type"].startswith("ISBN")
                ],
                "cover_url": volume.get("imageLinks", {}).get("thumbnail"),
            }
        )
    return jsonify({"docs": results})


@search_bp.route("/search_authors")
def search_authors():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"inauthor:{query}", "maxResults": 10}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return jsonify({"error": "Google Books API error"}), 502

    data = response.json()
    results = []
    for item in data.get("items", []):
        volume = item.get("volumeInfo", {})
        results.append(
            {
                "title": volume.get("title"),
                "author_name": volume.get("authors", []),
                "isbn": [
                    id["identifier"]
                    for id in volume.get("industryIdentifiers", [])
                    if id["type"].startswith("ISBN")
                ],
            }
        )
    return jsonify({"docs": results})


@search_bp.route("/search_isbn")
def search_isbn():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    # If the query is all digits and 10 or 13 chars, use isbn: for exact match
    if query.isdigit() and len(query) in (10, 13):
        q_param = f"isbn:{query}"
    else:
        q_param = query  # general search for partial ISBN

    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": q_param,
        "maxResults": 10,
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return jsonify({"error": "Google Books API error"}), 502

    data = response.json()
    results = []
    for item in data.get("items", []):
        volume = item.get("volumeInfo", {})
        results.append(
            {
                "title": volume.get("title"),
                "author_name": volume.get("authors", []),
                "isbn": [
                    id["identifier"]
                    for id in volume.get("industryIdentifiers", [])
                    if id["type"].startswith("ISBN")
                ],
                "cover_url": volume.get("imageLinks", {}).get("thumbnail"),
            }
        )
    return jsonify({"docs": results})

@search_bp.route("/search_listings")
def search_open_listings():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    pattern = re.compile(query, re.IGNORECASE)
    all_listings = Sales_Listing.query.all()
    results = []
    for sale in all_listings:
        if (
            pattern.search(sale.book.title or "")
            or pattern.search(sale.book.isbn or "")
            or pattern.search(sale.book.author or "")
        ):
            results.append({
                "id": sale.id,
                "title": sale.book.title,
                "author": sale.book.author,
                "isbn": sale.book.isbn,
                "price": sale.price,
                "description": sale.description,
            })
    return jsonify({"docs": results})