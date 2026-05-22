import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://data.gov.in/catalogs"

response = requests.get(url)

print("Status Code:", response.status_code)

html = response.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.find_all("h3")

dataset_list = []

for title in titles:
    dataset_list.append(title.text.strip())

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/page_001.json", "w", encoding="utf-8") as file:
    json.dump(dataset_list, file, indent=4)

print("Data saved successfully")