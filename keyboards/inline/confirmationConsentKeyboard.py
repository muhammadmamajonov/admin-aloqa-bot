from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

consent_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Roziman', callback_data='agree')
        ]
    ]
)

consent_en = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ I agree', callback_data='agree')
        ]
    ]
)

consent_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Я согласен', callback_data='agree')
        ]
    ]
)