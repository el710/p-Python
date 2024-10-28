from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from id_tm_bot import api_token, bot_name
import os

os.system('cls')


butt_calc_name = "Calculate"
butt_info_name = "Information"
butt_calc = KeyboardButton(butt_calc_name)
butt_info = KeyboardButton(butt_info_name)
out_kb = ReplyKeyboardMarkup(resize_keyboard=True)
out_kb.add(butt_calc)
out_kb.add(butt_info)

butt_calor_id = "calories"
butt_form_id = "formulas"
butt_calor = InlineKeyboardButton("Calculate norma of calories", callback_data=butt_calor_id)
butt_form = InlineKeyboardButton("Formulas of calculation", callback_data=butt_form_id)
in_kb = InlineKeyboardMarkup()
in_kb.insert(butt_calor)
in_kb.insert(butt_form)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

bot = Bot(api_token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def starter(message):
    await message.answer("outer menu: ", reply_markup=out_kb)

"""
    Inner menu handlers
"""
@dp.message_handler(text=butt_calc_name)
async def main_menu(message):
    await message.answer("Choose the option:", reply_markup=in_kb)

@dp.callback_query_handler(text=butt_form_id)
async def get_formulas(call):
    await call.message.answer("Woman() = 10 * weight + 6.25 * growth - 5 * age - 161")
    await call.message.answer("Man() = 10 * weight + 6.25 * growth - 5 * age + 5")
    await call.answer()

@dp.callback_query_handler(text=butt_calor_id)
async def set_age(call):
    await call.message.answer(f"Write me your age: ")
    await UserState.age.set()

"""
    Outer menu handlers
"""
@dp.message_handler(text=butt_info_name)
async def informer(message):
    await message.answer(f"Info: Me is bot {bot_name}")

# @dp.message_handler(text=butt_calc_name)
# async def set_age(message):
#     await message.answer(f"Write me your age: ")
#     await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f"Write me your growth: ")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f"Write me weight: ")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
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



@dp.message_handler()
async def all_messages(message):
    await message.answer("Hello there! Bot I am, to help for health of your's")
    await message.answer("Type /start to get outer menu")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

