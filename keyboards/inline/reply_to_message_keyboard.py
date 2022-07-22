from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def reply_markup(message_id):
    reply = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Javob yozish", callback_data=f"reply_to_this_message={message_id}")
            ]
        ]
    )
    return reply