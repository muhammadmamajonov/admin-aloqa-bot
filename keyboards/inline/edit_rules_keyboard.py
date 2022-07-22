from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

edit_rules_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 Uz O\'zgartirish uchun bosing', callback_data='change_rules_uz'),
            InlineKeyboardButton(text='🇺🇸 En Click to change', callback_data='change_rules_en'),
        ],
        [
            InlineKeyboardButton(text='🇷🇺 Ru Нажмите, чтобы изменить', callback_data='change_rules_ru')
        ]
    ]
)