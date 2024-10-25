"""
pip install aiogram==2.25.1
"""

from aiogram import Bot, Dispatcher, executor ##, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
 
from id_bot import Teltoken

bot = Bot(token=Teltoken)
dp = Dispatcher(bot, storage=MemoryStorage())


"""
    If one handler cought message then other handlers won't work, so
        First: specific handlers...
"""
"""
    Handler for message == "Urban" or "Oleg" e.t.c
    take care of Up|Down case...
"""
@dp.message_handler(text = ["Urban", "Oleg"])
async def spec_message(message):
    for key, value in message:
        print(f"Call: {key}: {value}")
    print()

"""
    Handler for commands... </comm>
"""
@dp.message_handler(commands=['start'])
async def get_command(message):
    for key, value in message:
        print(f"Command: {key}: {value}")
    print()        
   
"""
    Last, common handlers....
"""
"""
    handler for every message
"""
@dp.message_handler()
async def all_message(message):
    for key, value in message:
        print(f"Call: {key}: {value}")
    print()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
