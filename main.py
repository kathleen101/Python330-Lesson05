import requests

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged=django&site=stackoverflow")
response.content
results = response.json()
keys = response.json().keys()
items = response.json()['items']
items_sample = items[0]['owner']

response = requests.get('https://stackoverflow.com/users/15204034/kevin-alfito')
response = requests.get('https://api.stackexchange.com/2.3/users/15204034?order=desc&sort=reputation&site=stackoverflow')
print(response.json())