import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)

data = response.json()

print(f"Name: {data['name']}")
print(f"ID: {data['id']}")
print(f"Height: {data['height']}")
print(f"Weight: {data['weight']}")
print(f"Types: {[t["type"]["name"] for t in data['types']]}")  