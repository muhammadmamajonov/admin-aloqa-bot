import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.languageKeyboard import language_keyboard
from keyboards.default.admin_keyboard_markup import admin_reply_keyboard
from states.registrationStates import Registration
from data.config import ADMINS
print(ADMINS)
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    try:
        db.add_user(id=message.from_user.id, username=message.from_user.username)
    except sqlite3.IntegrityError as err:
        pass
    
    if f"{message.from_user.id}" in ADMINS:
        await message.answer(f"Salom Admin, botga xush kelibsiz!", reply_markup=admin_reply_keyboard)
    else:
        text = "Davom etish uchun tilni tanlang.\n"
        text += "Select a language to continue.\n"
        text += "Выберите язык, чтобы продолжить"

        await message.answer(f"Salom, {message.from_user.full_name}!")
        await message.answer(text=text, reply_markup=language_keyboard)
        await Registration.language_seletction.set()

