import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i + 1} шар.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    tasks = []
    for k, v in competitors.items():
        tasks.append(asyncio.create_task(start_strongman(k, v)))
    for task in tasks:
        await task


competitors = {'Alfa': 3, 'Bravo': 1, 'Charly': 4}
asyncio.run(start_tournament())
