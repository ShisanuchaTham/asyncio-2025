import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        url = "https://pokeapi.co/api/v2/pokemon/ditto"
        response = await client.get(url)
        print(f'Status Code: {response.status_code}, URL: {response.url}')
        data = response.json()

        print(f"Name: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print(f"Types: {[t["type"]["name"] for t in data['types']]}")  

asyncio.run(main())