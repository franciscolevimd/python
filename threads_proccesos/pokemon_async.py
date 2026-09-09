import asyncio
import requests
import time


async def get_pokemon_name(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        name = response.json().get("forms")[0].get("name")
        return name


async def show_pokemon_info(number):
    name = await get_pokemon_name(number)
    print(name)


async def main():
    start = time.time()
    tasks = [show_pokemon_info(n) for n in range(1, 101)]
    await asyncio.gather(*tasks)
    print(f"Fin de main {time.time() - start}")


if __name__ == '__main__':
    asyncio.run(main())
