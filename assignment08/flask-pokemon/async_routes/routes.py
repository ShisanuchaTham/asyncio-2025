import time
import random
import httpx
from flask import Blueprint, render_template, current_app
import asyncio

# Create a Blueprint for sync routes
async_bp = Blueprint("async", __name__)

# Helper function to fetch a single XKCD JSON by URL
async def get_pokemon(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"{time.ctime()} - get {url}")    # Log the request time and URL
        return response.json()

# Helper function to fetch multiple XKCD comics
async def get_pokemons():
    # Get the number of comics to fetch from app config
    NUMBER_OF_POKEMON = current_app.config["NUMBER_OF_POKEMON"]

    rand_list = [random.randint(1, 898) for _ in range(NUMBER_OF_POKEMON)]

    pokemons_data = []
    tasks = [get_pokemon(f'https://pokeapi.co/api/v2/pokemon/{number}') for number in rand_list]
    pokemons_data = await asyncio.gather(*tasks)
    return pokemons_data

# Route: GET /sync/
@async_bp.route('/')
async def home():
    start_time = time.perf_counter()  # Start performance timer
    pokemons = await get_pokemons()               # Fetch random XKCD comics
    end_time = time.perf_counter()    # End performance timer

    # Log time and count
    print(f"{time.ctime()} - Get {len(pokemons)} Pokémon. Time taken: {end_time-start_time} seconds")

    # Render result using Jinja2 template
    return render_template('sync.html'
                           , title="Pokémon Asynchronous Flask"
                           , heading="Pokémon Asynchronous Version"
                           , pokemons=pokemons
                           , end_time=end_time
                           , start_time=start_time)
