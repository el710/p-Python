"""
pip install aiogram==2.25.1
"""
## basic...
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

## for get <state>... to get, keep & use data of users
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import asyncio

from id_bot import tel_token, bot_name
import os

os.system('cls')

"""
    make bot & dispetcher
"""
bot = Bot(token=tel_token)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    address = State()

@dp.message_handler(text="Order")
async def buy(message):
    await message.answer("Send us your address, pleeeese...")
    """
        start catch next message as <address>...
    """
    await UserState.address.set()

"""
    handler for state...
"""
@dp.message_handler(state=UserState.address)
async def fsm_handler(message, state):
    await state.update_data(adr = message.text) ## save as dictionary key = value
    ## get data back from dict
    data = await state.get_data()
    await message.answer(f"We'll send the package to {data['adr']}")
    await state.finish()



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
        write to chat
    """
    await message.answer(f"{bot_name}: '{message.text}' is key-word message")

"""
    Handler for commands... </comm>
"""
@dp.message_handler(commands=['start'])
async def get_command(message):
    for key, value in message:
        print(f"Command: {key}: {value}")
    print()
    await message.answer(f"{bot_name}: Hello there! Nice to see you")
   
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
    await message.answer(f"{bot_name}: you wrote - {message.text.upper()}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
