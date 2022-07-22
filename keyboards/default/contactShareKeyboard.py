
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

concat_button = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📞 Share contact', request_contact=True),
        ],
    ],
    resize_keyboard=True
)