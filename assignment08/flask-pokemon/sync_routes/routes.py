import time
import random
import requests
from flask import Blueprint, render_template, current_app

# Create a Blueprint for sync routes
sync_bp = Blueprint("sync", __name__)

# Helper function to fetch a single Pokémon JSON by URL
def get_pokemon(url):
    response = requests.get(url)
    print(f"{time.ctime()} - get {url}")  # Log the request time and URL
    return response.json()

# Helper function to fetch multiple Pokémon data
def get_pokemons():
    # Get the number of Pokémon to fetch from app config
    NUMBER_OF_POKEMON = current_app.config["NUMBER_OF_POKEMON"]

    # Generate a list of random Pokémon IDs (1–898, for example)
    rand_list = [random.randint(1, 898) for _ in range(NUMBER_OF_POKEMON)]

    pokemons_data = []
    for number in rand_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        pokemon_json = get_pokemon(url)  # Fetch Pokémon JSON
        pokemons_data.append(pokemon_json)
    return pokemons_data

# Route: GET /sync/
@sync_bp.route('/')
def home():
    start_time = time.perf_counter()  # Start performance timer
    pokemons = get_pokemons()          # Fetch random Pokémon data
    end_time = time.perf_counter()     # End performance timer

    # Log time and count
    print(f"{time.ctime()} - Get {len(pokemons)} Pokémon. Time taken: {end_time - start_time} seconds")

    # Render result using Jinja2 template
    return render_template('sync.html',
                           title="Pokémon Synchronous Flask",
                           heading="Pokémon Synchronous Version",
                           pokemons=pokemons,
                           end_time=end_time,
                           start_time=start_time)
