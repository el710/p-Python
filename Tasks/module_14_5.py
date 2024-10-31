from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from id_tm_bot import api_token, bot_name

import sqlite3
from crud_functions import *

import logging

import os

os.system('cls')
logging.basicConfig(level=logging.INFO)


butt_calc_name = "Calculate"
butt_info_name = "Information"
butt_buy_name = "Buy"
butt_reg_name = "Registration"
butt_calc = KeyboardButton(butt_calc_name)
butt_info = KeyboardButton(butt_info_name)
butt_buy = KeyboardButton(butt_buy_name)
butt_reg = KeyboardButton(butt_reg_name)

out_kb = ReplyKeyboardMarkup(resize_keyboard=True)
out_kb.add(butt_calc)
out_kb.add(butt_info)
out_kb.insert(butt_buy)
out_kb.insert(butt_reg)

butt_calor_id = "calories"
butt_form_id = "formulas"
butt_calor = InlineKeyboardButton("Calculate norma of calories", callback_data=butt_calor_id)
butt_form = InlineKeyboardButton("Formulas of calculation", callback_data=butt_form_id)

in_kb = InlineKeyboardMarkup()
in_kb.insert(butt_calor)
in_kb.insert(butt_form)

butt_prod_1id = "Product 1"
butt_prod_2id = "Product 2"
butt_prod_3id = "Product 3"
butt_prod_4id = "Product 4"
butt_prod_1 = InlineKeyboardButton(butt_prod_1id, callback_data="product_buy")
butt_prod_2 = InlineKeyboardButton(butt_prod_2id, callback_data="product_buy")
butt_prod_3 = InlineKeyboardButton(butt_prod_3id, callback_data="product_buy")
butt_prod_4 = InlineKeyboardButton(butt_prod_4id, callback_data="product_buy")

in_buy_kb = InlineKeyboardMarkup()
in_buy_kb.add(butt_prod_1, butt_prod_2, butt_prod_3, butt_prod_4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


bot = Bot(api_token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def starter(message):
    await message.answer("outer menu: ", reply_markup=out_kb)

"""
    Inner menu handlers
"""
@dp.callback_query_handler(text=butt_form_id)
async def get_formulas(call):
    await call.message.answer("Woman() = 10 * weight + 6.25 * growth - 5 * age - 161")
    await call.message.answer("Man() = 10 * weight + 6.25 * growth - 5 * age + 5")
    await call.answer()

@dp.callback_query_handler(text=butt_calor_id)
async def set_age(call):
    await call.message.answer(f"Write me your age: ")
    await UserState.age.set()

@dp.callback_query_handler(text="product_buy")
async def send_confirm_messages(call):
    await call.message.answer("Thank you for buying!")
    await call.answer()


"""
    Outer menu handlers
"""
@dp.message_handler(text=butt_calc_name)
async def main_menu(message):
    await message.answer("Choose the option:", reply_markup=in_kb)

@dp.message_handler(text=butt_info_name)
async def informer(message):
    await message.answer(f"Info: Me is bot {bot_name}")

@dp.message_handler(text=butt_buy_name)
async def get_buying_list(message):
    db_data = get_all_products()
    for idx, item in enumerate(db_data):
        with open(f"product_{idx + 1}.jpg", "rb") as image:
            await message.answer_photo(image, f"Name: {item[1]}| Desc.: {item[2]} | Price: {item[3]} ")
    await message.answer("Choose our products: ", reply_markup = in_buy_kb)

@dp.message_handler(text=butt_reg_name)
async def sign_up(message):
    await message.answer("Type your name: ")
    await RegistrationState.username.set()


"""
    State machine
"""
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

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username = message.text)
        await message.answer("Type your e-mail: ")
        await RegistrationState.email.set()
    else:
        await message.answer(f"User with name '{message.text}' exists. Choose other name: ")
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Type your age: ")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    new_user = await state.get_data()
    add_user(new_user["username"], new_user["email"], new_user["age"])
    await message.answer(f"Congratuation: user {new_user['username']} has added")
    await state.finish()



"""
    Chat handle...
"""
@dp.message_handler()
async def all_messages(message):
    await message.answer("Hello there! Bot I am, to help for health of your's")
    await message.answer("Type /start to get outer menu")


if __name__ == '__main__':
    initiate_db("not_telegram.dp")
        
    prod_list = [("Mighty Leaf", "Leaf's armor makes you safe", 100),
                ("Eternal Metal", "E-Metal makes you strong or flexible at the right moment", 200),
                ("Cristal", "It makes your mind clear and sharp", 300),
                ("Wise snake", "Makes your mind opened", 400)
    ]
    add_product(prod_list)

    add_user("ghost", "no@mail.com", "0")

    executor.start_polling(dp, skip_updates=True)

