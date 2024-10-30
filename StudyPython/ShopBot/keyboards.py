from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Prices"),
            KeyboardButton(text="About")
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Medium game", callback_data="medium")],
        [InlineKeyboardButton(text="Big game", callback_data="big")],
        [InlineKeyboardButton(text="Mega game", callback_data="mega")],
        [InlineKeyboardButton(text="Other games", callback_data="other")]
    ]
)

cell_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Buy", url="https://google.com")],
        [InlineKeyboardButton(text="Back", callback_data="buy_back")]
    ]
)