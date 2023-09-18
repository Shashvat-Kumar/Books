import requests

def search_books(query):
    base_url = "https://openlibrary.org/search.json"
    params = {
        "q": query,
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()

            # Extract book titles from the API response
            book_titles = []
            for doc in data.get("docs", []):
                title = doc.get("title", "Unknown Title")
                book_titles.append(title)

            return book_titles

        else:
            return "Unable to fetch book recommendations."

    except Exception as e:
        return str(e)
