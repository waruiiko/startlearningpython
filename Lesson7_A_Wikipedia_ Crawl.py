import requests
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print("======")
# print(response.text)
# print(type(response.text))
html = response.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print(soup.p)