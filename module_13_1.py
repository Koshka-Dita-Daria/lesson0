import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')
async def start_tournament():
    k1 = asyncio.create_task((start_strongman('Pasha', 3)))
    k2 = asyncio.create_task(start_strongman('Denis', 4))
    k3 = asyncio.create_task(start_strongman('Apollon', 5))
    await k1
    await k2
    await k3

start = time.time()
asyncio.run(start_tournament())
finish = time.time()