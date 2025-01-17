import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    ball_amount = 5
    for ball_num in range(ball_amount):
        await asyncio.sleep(max_power - power)
        print(f'Силач {name} поднял {ball_num + 1} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    strongman_1 = asyncio.create_task(start_strongman('Cheburashka', 2))
    strongman_2 = asyncio.create_task(start_strongman('Kratos', 5))
    strongman_3 = asyncio.create_task(start_strongman('Yokozuna', 4))
    await strongman_1, strongman_2, strongman_3

max_power = 5.5
asyncio.run(start_tournament())
