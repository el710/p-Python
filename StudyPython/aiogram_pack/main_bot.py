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

## outline menu buttons
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

## inline menu buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from id_bot import tel_token, bot_name
import os

"""
    import module_13
"""


os.system('cls')

"""
    make bot & dispetcher
"""
bot = Bot(token=tel_token)
dp = Dispatcher(bot, storage=MemoryStorage())

"""
    make outlay buttons
"""
name_button_1 = "Information"
button_1 = KeyboardButton(text=name_button_1)
button_2 = KeyboardButton(text="Order")

## make outlay keyboard
kb = ReplyKeyboardMarkup(resize_keyboard=True) ## resize automatically button for sreen size
kb.add(button_1)
"""
    else: kb.row(<list of buttons>)
          kb.insert() - add button to the end of row or make new row...
"""
kb.insert(button_2)

outline_kb_block = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Inform")], ## one list - one block of buttons
        [
            KeyboardButton(text="shop"),
            KeyboardButton(text="donate")
        ]
    ], resize_keyboard=True
)


"""
    make inline button-menu
"""
butt_info_name = "Inform"
butt_info = InlineKeyboardButton(text=butt_info_name, callback_data="id_info") ## id_info hidden id-key of button

inline_kb = InlineKeyboardMarkup()
inline_kb.add(butt_info)




class UserState(StatesGroup):
    address = State()

@dp.message_handler(text="Order") ## it will also catch text & name_button_1
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
    await message.answer(f"{bot_name}: Hello there! Nice to see you", reply_markup=inline_kb)

"""
    for inline button-menu handler
"""
@dp.callback_query_handler(text="id_info")
async def inline_info(call):
    await call.message.answer(f"This is {bot_name} bot")
    await call.answer() ## - release button

@dp.message_handler(commands='block')
async def start_block(message):
    await message.answer(text=":", reply_markup=outline_kb_block) ## text can't be empty

"""
    use keyword to open outlay menu
"""
@dp.message_handler(commands=['outmenu'])
async def start_outmenu(message):
    await message.answer("Here is message mackets", reply_markup = kb) ## show keyboard with answer

@dp.message_handler(text=name_button_1)
async def inform(message):
    await message.answer(f"This is outline button of {bot_name} bot")

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
    await message.answer(f"{bot_name}: try /outmenu to use outline menu...")
    await message.answer(f"{bot_name}: try /start to use inline menu...")
    await message.answer(f"{bot_name}: try /block to use inline menu...")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

