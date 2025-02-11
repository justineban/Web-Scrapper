import requests
from bs4 import BeautifulSoup

url = input("Ingresa la URL: ")
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

print("H1:", len(soup.find_all("h1")))
print("H2:", len(soup.find_all("h2")))
print("H3:", len(soup.find_all("h3")))