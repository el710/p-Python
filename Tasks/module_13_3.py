from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from id_tm_bot import bot_name, api_token
import os

os.system('cls')

bot = Bot(api_token)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

@dispatcher.message_handler(commands=['start'])
async def start(message):
    await message.answer("Hello there! Bot i am, for health of your's to help")

@dispatcher.message_handler()
async def all_messages(message):
    await message.answer("Type /start for beginning of conversation...")


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)