from concurrent.futures import ThreadPoolExecutor
import os
import time


def is_prime(number):
    if number < 2:
        return 1

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 1

    return number


def valdate_future(function):
    def wrapper(future):
        return function(future.result())
    return wrapper


@valdate_future
def use_prime_with_encrypt(number):
    print(f"Vamos a ralizar un cifrado con {number}")


if __name__ == '__main__':
    start = time.time()
    numbers = [
        709,
        17449,
        1128889,
        304211,
        4535189,
        7474967,
        14161729,
        19734581,
        78644,
        7,
        3324,
        56011909
    ]

    num_cores = os.cpu_count()

    with ThreadPoolExecutor(max_workers=num_cores) as worker:
        for number in numbers:
            future = worker.submit(is_prime, number)
            future.add_done_callback(use_prime_with_encrypt)

    print(f"Fin de programa {time.time() - start}")
