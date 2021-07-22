import requests
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print("======")
print(response.text)
print(type(response.text))
