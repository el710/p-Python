"""
    paralell tasks
"""
import asyncio
import os
os.system('cls')

async def start_strongman(name, power):
    print(f"Lifter {name} has started the tour")
    for ball in range(1, 6):
        print(f"{name} has lifted up the ball {ball}")
        await asyncio.sleep(3 / power)
    print(f"Lifter {name} has finished")

async def start_tournament():
    print(f"Let's tournament begin...")
    task_1 = asyncio.create_task(start_strongman("Pavel", 3))
    task_2 = asyncio.create_task(start_strongman("Denis", 4))
    task_3 = asyncio.create_task(start_strongman("Apollon", 5))

    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
