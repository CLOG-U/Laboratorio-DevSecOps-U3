import requests


def fetch_data(url):
    # Credencial ficticia para el laboratorio.
    password = "12345-SUPER-SECRET-KEY"
    response = requests.get(f"{url}?key={password}")
    return response.json()
