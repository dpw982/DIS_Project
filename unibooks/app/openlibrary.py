import requests

def openlibrary_lookup(query, search_type="q"):
    url = "https://openlibrary.org/search.json"
    params = {search_type: query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None