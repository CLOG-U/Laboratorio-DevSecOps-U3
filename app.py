import os
from urllib.parse import urlsplit

import requests


def fetch_data(url):
    """Obtiene JSON desde un endpoint HTTPS autorizado por la aplicación."""
    if urlsplit(url).scheme != "https":
        raise ValueError("Se requiere una URL HTTPS")
    api_key = os.environ["API_KEY"]
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=10,
        allow_redirects=False,
    )
    response.raise_for_status()
    return response.json()
