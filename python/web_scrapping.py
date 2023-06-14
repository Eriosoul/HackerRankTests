import requests

url = 'https://pokeapi.co/api/v2/pokemon-species/2/'
r = requests.get(url)

content = r.json()
# print(content)
info = content.get("name")
# decript = content.get("description")
print(info)