import requests

base_url = "https://capital-finder-9ll0pl14a-niles-thompsons-projects.vercel.appp"

response_chile = requests.get(f"{base_url}?country=Chile")
print(response_chile.text)

response_santiago = requests.get(f"{base_url}?capital=Santiago")
print(response_santiago.text)

response_germany_berlin = requests.get(f"{base_url}?country=Germany&capital=Berlin")
print(response_germany_berlin.text)
