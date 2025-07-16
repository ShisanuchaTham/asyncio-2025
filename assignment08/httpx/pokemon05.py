import asyncio
import httpx

pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "snorlax", "gengar", "mewtwo","psyduck","jigglypuff"]


async def fetch_pokemon_data(client, name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    try:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "name": data["name"].title(),
            "id": data["id"],
            "base_xp": data["base_experience"]
        }
    except (httpx.HTTPStatusError, httpx.RequestError, KeyError) as e:
        print(f"Error fetching {name}: {e}")
        return None

def sort_by_name(pokemon):
    return pokemon['name']
def sort_by_base_xp(pokemon):
    return pokemon['base_xp']

async def main():
    all_data = []
    async with httpx.AsyncClient() as client:
        tasks = [fetch_pokemon_data(client, name) for name in pokemon_names]
        results = await asyncio.gather(*tasks)
        # Filter out any None results in case of errors
        all_data = [res for res in results if res is not None]
    
    # Sort by name using the separate function
    sorted_data = sorted(all_data, key=sort_by_base_xp,reverse=True)

    for pokemon in sorted_data:
        print(f"{pokemon['name'].capitalize()} - ID: {pokemon['id']}, Base XP: {(pokemon['base_xp'])}")


# Run the main function
asyncio.run(main())