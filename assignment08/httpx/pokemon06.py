import asyncio
import httpx

async def fetch_abilities(client):
    url = "https://pokeapi.co/api/v2/ability/?limit=20"
    try:
        Result = []
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        abilities = [ability['name'] for ability in data['results']]

        for ability in abilities:
            url = f"https://pokeapi.co/api/v2/ability/{ability}"
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            pokemon = len(data.get('pokemon', []))
            print(f"Ability: {ability}  -> Pokemon: {pokemon}")
    except (httpx.HTTPStatusError, httpx.RequestError, KeyError) as e:
        print(f"Error fetching abilities: {e}")
    
async def main():
    async with httpx.AsyncClient() as client:
        abilities = await fetch_abilities(client)

asyncio.run(main())