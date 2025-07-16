import asyncio
import httpx

pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "snorlax", "gengar", "mewtwo","psyduck","jigglypuff"]


async def fetch_pokemon_data(client, name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    try:
        response = await client.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        print(f"{data['name'].title()} - ID: {data['id']}, Types: {[t['type']['name'] for t in data['types']]}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred while fetching {name}: {e.response.status_code}")
    except httpx.RequestError as e:
        print(f"Error occurred while requesting {name}: {e}")
    except KeyError:
        print(f"Error parsing data for {name}")

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch_pokemon_data(client, name) for name in pokemon_names]
        await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())