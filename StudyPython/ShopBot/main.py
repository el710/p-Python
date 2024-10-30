from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio
import os

from config import *
from keyboards import *
import texts

import logging

os.system('cls')

logging.basicConfig(level=logging.INFO)

bot = Bot(tel_token)
dp = Dispatcher(bot, storage=MemoryStorage())

"""
    start_kb
"""
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=start_kb)

@dp.message_handler(text="About")
async def info(message):
    await message.answer(texts.about, reply_markup=start_kb)

@dp.message_handler(text="Prices")
async def prices(message):
    await message.answer(texts.question, reply_markup=catalog_kb)

# @dp.callback_query_handler(text="")
# async def buy_(call):
#     await call.message.answer()
#     await call.answer()
@dp.callback_query_handler(text="medium")
async def buy_m(call):
    await call.message.answer(texts.game_M, reply_markup = cell_kb)
    await call.answer()

@dp.callback_query_handler(text="big")
async def buy_l(call):
    await call.message.answer(texts.game_L, reply_markup = cell_kb)
    await call.answer()

@dp.callback_query_handler(text="mega")
async def buy_xl(call):
    await call.message.answer(texts.game_XL, reply_markup = cell_kb)
    await call.answer()

@dp.callback_query_handler(text="other")
async def buy_oth(call):
    await call.message.answer(texts.other, reply_markup = cell_kb)
    await call.answer()


@dp.message_handler()
async def any_message(message):
    await message.answer("Hi, type /start")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)