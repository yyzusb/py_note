import requests

web = 'https://www.google.com'

reponse = requests.get(web)

print(reponse.text)
