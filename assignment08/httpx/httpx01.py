import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.example.com")
        print(f'Status Code: {response.status_code}, URL: {response.url}')
        print(f'Error: {response}')

asyncio.run(main())