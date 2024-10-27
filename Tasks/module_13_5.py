from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio
from id_tm_bot import api_token
import os

os.system('cls')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

butt_calc_text = "Calculate"
butt_info_text = "Information"

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
butt_calc = KeyboardButton(text=butt_calc_text)
butt_info = KeyboardButton(text=butt_info_text)
keyboard.add(butt_calc)
keyboard.insert(butt_info)


bot = Bot(api_token)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

@dispatcher.message_handler(commands=['start'])
async def start(message):
    await message.answer("Hello there! Bot I am, to help for health of your's", reply_markup=keyboard)

@dispatcher.message_handler(text=butt_calc_text)
async def set_age(message):
    await message.answer(f"Write me your age: ")
    await UserState.age.set()

@dispatcher.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f"Write me your growth: ")
    await UserState.growth.set()

@dispatcher.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f"Write me weight: ")
    await UserState.weight.set()

@dispatcher.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    def f_Miff_Jeor(data):
        age = float(data["age"])
        growth = float(data["growth"])
        weight = float(data["weight"])

        man = 10 * weight + 6.25 * growth - 5 * age + 5
        woman = 10 * weight + 6.25 * growth - 5 * age - 161

        return man, woman
 
    man_norm, woman_norm = f_Miff_Jeor(data)
    await message.answer(f"Calories norma for man: {man_norm}; norma for woman: {woman_norm}")
    await state.finish()
 
    
@dispatcher.message_handler()
async def all_messages(message):
    await message.answer("write /start to begin...")


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)


