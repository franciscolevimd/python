import time
import requests
from concurrent.futures import ProcessPoolExecutor


def get_pokemon_name(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        name = response.json().get("forms")[0].get("name")
        return name


def validate_future(function):
    def wrapper(future):
        return function(future.result())
    return wrapper


@validate_future
def show_pokemon_name(pokemon_name):
    print(f"El nombre del pokemon es: {pokemon_name}")


if __name__ == '__main__':
    start = time.time()

    with ProcessPoolExecutor(max_workers=10) as worker:
        for n in range(1, 101):
            future = worker.submit(get_pokemon_name, n)
            future.add_done_callback(show_pokemon_name)

    print(f"Fin de programa {time.time() - start}")
