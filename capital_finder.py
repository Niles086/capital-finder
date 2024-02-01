# capital_finder.py

import requests

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

def get_response(country, capital):
    if country and capital:
        return f"{capital} is the capital of {country}."
    elif country:
        return f"The capital of {country} is {get_capital_by_country(country)}."
    elif capital:
        country = get_country_by_capital(capital)
        if country:
            return f"{capital} is the capital of {country}."
    return "Invalid input. Please provide a valid country or capital."

# Vercel Serverless Function
def handler(request, response):
    country = request.query.get("country", "").strip()
    capital = request.query.get("capital", "").strip()

    result = get_response(country, capital)

    response.status(200).text(result)
