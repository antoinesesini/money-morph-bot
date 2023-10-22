import logging
import requests


private_api_key = "XXXXXXXXXXXXXXXXXXXXXXXX"


def convert(amount, from_currency, to_currency):
    api_url = f"https://v6.exchangerate-api.com/v6/{private_api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["conversion_result"]
    else:
        logging.error(f"Error: {response.status_code}")
        return None
