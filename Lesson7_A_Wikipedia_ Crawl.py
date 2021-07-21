import requests as requests
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print(response.text)
print(type(response.text))