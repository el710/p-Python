import asyncio
import time
import os
os.system('cls')
"""
    async function we can run like a thread, called 'Task'
"""
async def notification():
    time.sleep(10)
    print("alarm!!!")

"""
    to use async subfunctions main function must be async
"""
async def main(): ## because of <async> main() is now  'Task-1'

    print("... to start async subfunction inside the functions we create new Task...")
    task = asyncio.create_task(notification()) ## it works pseudo parallel...
    print(f"timer was set: {task}")
    print("wait...")
    print("\n... and here main() is finished, but process wait end of the sleep()")
    print("... if there are no functions like a sleep() then main process will finished and Task-2 will be lost...\n")

"""
    run Main async function...
    ... run() can start a Task in main processs...
"""
asyncio.run(main())
input("press <Enter>...")


"""
Example # 2
"""

async def get_temp():
    print("Get Temp.: ...")
    """
    we use async sleep function and must wait its finish
    """
    await asyncio.sleep(2)
    print("Temp is 25 C")

async def get_pres():
    print("Get air pressure.: ...")
    await asyncio.sleep(4)
    print("Ap is 101 kPa")


async def start():
    print("\nStart:...")
    task_2 = asyncio.create_task(get_temp())
    task_3 = asyncio.create_task(get_pres())

    """
        for not to loose task-2 & task-3 we must wait for them...
    """
    await task_2
    await task_3
    """
        we can't use <await> outside a function...
    """

    print("Finish")


start_time = time.time()
"""
    run() start function inside the main process
"""
asyncio.run(start())
"""
    run() automatically await called async function: ... await start()
"""

finish_time = time.time()
print(f"Work time: {round(finish_time - start_time, 2)} seconds")

input("\nsome magic...")
asyncio.run(get_temp())
