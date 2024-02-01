# capital_finder.py

import requests 
from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)

        # Extracting query parameters
        query_params = parse.parse_qs(url_components.query)
        print(f"Received request with query parameters: {query_params}")


        # Check if 'country' or 'capital' is present in the query parameters
        if 'country' in query_params:
            country_name = query_params['country'][0]
            capital = self.get_capital_by_country(country_name)
            response = f'The capital of {country_name} is {capital}.'
        elif 'capital' in query_params:
            capital_name = query_params['capital'][0]
            country = self.get_country_by_capital(capital_name)
            response = f'{capital_name} is the capital of {country}.'
        else:
            response = 'Invalid request. Please provide either "country" or "capital" parameter.'

        # Sending the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode())

    def get_capital_by_country(self, country_name):
        # Using REST Countries API to get capital by country name
        url = f'https://restcountries.com/v3.1/name/{country_name}?fields=capital'
        response = requests.get(url)
        data = response.json()
        capital = data[0]['capital'][0] if data else 'Unknown'
        return capital

    def get_country_by_capital(self, capital_name):
        # Using REST Countries API to get country by capital name
        url = f'https://restcountries.com/v3.1/capital/{capital_name}?fields=name'
        response = requests.get(url)
        data = response.json()
        country = data[0]['name']['common'] if data else 'Unknown'
        return country
