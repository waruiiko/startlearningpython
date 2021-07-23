# pip3 install requests 安装requests
import requests
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print("======")
# print(response.text)
# print(type(response.text))
html = response.text

# pip3 install beautifulsoup4 安装beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print(soup.p)