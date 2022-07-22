from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 Uz', callback_data='uz'),
            InlineKeyboardButton(text='🇺🇸 En', callback_data='en'),
            InlineKeyboardButton(text='🇷🇺 Ru', callback_data='ru')
        ]
    ]
)