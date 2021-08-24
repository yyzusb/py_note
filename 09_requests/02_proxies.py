import requests

url = 'https://www.baiddu.com'

proxies1 = {
    'http': 'http://115.218.0.53:9000'
}

response = requests.get(url, proxies=proxies1)
print(response.text)
