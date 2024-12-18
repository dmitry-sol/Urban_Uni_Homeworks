import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    tasks = []
    for name, power in competitors.items():
        tasks.append(asyncio.create_task(start_strongman(name, power)))
    for task in tasks:
        await task


competitors = {'Alfa': 3, 'Bravo': 1, 'Charly': 4, 'Delta': 1.3}
asyncio.run(start_tournament())
