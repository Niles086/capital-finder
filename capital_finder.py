# capital_finder.py

import requests
from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        def get_country_by_name(country_name):
            url = f"https://restcountries.com/v2/name/{country_name}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data[0]
            return None

        def get_capital_by_country(country_name):
            country_data = get_country_by_name(country_name)
            if country_data:
                return country_data.get('capital')
            return None

        def get_country_by_capital(capital_name):
            url = f"https://restcountries.com/v2/capital/{capital_name}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data[0]
            return None

        country = dic.get('country')
        capital = dic.get('capital')

        if country and capital:
            result = f"{capital} is the capital of {country}."
        elif country:
            result = f"The capital of {country} is {get_capital_by_country(country)}."
        elif capital:
            country = get_country_by_capital(capital)
            if country:
                result = f"{capital} is the capital of {country}."
            else:
                result = "Invalid input. Please provide a valid country or capital."
        else:
            result = "Invalid input. Please provide a valid country or capital."

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(result.encode())
