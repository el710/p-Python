from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import os

from id_tm_bot import bot_name, api_token

os.system('cls')

## setup bot
tm_bot = Bot(api_token)

## setup dispatcher
dispatcher = Dispatcher(tm_bot, storage=MemoryStorage())

## make handlers
@dispatcher.message_handler(commands=['start'])
async def start(message):
    # for key, value in message:
    #     print(f"Command: {key}: {value}")
    print(f"\n{bot_name}: Hello there! I'm bot to help for your health")

@dispatcher.message_handler()
async def all_messages(message):
    print(f"{bot_name}: Type '/start' for begining conversation...")


## start dispatcher
if __name__ == "__main__":
    print(f"{bot_name} has started...")
    executor.start_polling(dispatcher, skip_updates=True)