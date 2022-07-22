
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_reply_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📬 Xabarlar'),
            KeyboardButton(text='📊 Statistika'),
            KeyboardButton(text='🔔 Qoidalarni sozlash'),
        ],
    ],
    resize_keyboard=True
)