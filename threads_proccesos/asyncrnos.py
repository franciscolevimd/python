import asyncio
import time  # time.sleep Duerme thread.


async def function_a():
    print("function_a")
    await asyncio.sleep(3)
    print("function_a completed")


async def function_b():
    print("function_b")
    await asyncio.sleep(1)
    print("function_b completed")
    await asyncio.sleep(2)
    print("function_b completed 2")


async def function_c():
    print("function_c")
    await asyncio.sleep(2)
    print("function_c completed")


async def main():
    start = time.time()
    # task_1 = asyncio.create_task(function_a())
    # task_2 = asyncio.create_task(function_b())
    # task_3 = asyncio.create_task(function_c())

    # await task_1  # join
    # await task_2  # join
    # await task_3  # join

    await asyncio.gather(
        function_a(),
        function_b(),
        function_c()
    )

    print(f"Fin de main {time.time() - start}")

asyncio.run(main())
