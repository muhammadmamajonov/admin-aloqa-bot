from aiogram import types
from handlers.users.registrationHandlar import LANGUAGE
from keyboards.inline.reply_to_message_keyboard import reply_markup
from aiogram.types import InlineKeyboardButton
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(state=None)
async def get_message(message: types.Message):
    from handlers.users.registrationHandlar import LANGUAGE

    db.add_message(message.message_id, user_id=message.from_user.id, text=message.text)
    user = db.select_user(id=message.from_user.id)
    if message.from_user.id not in ADMINS:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=f"""
            Yangi xabar keldi 📥

    <b>👤 foydalanuvchi ism-familyasi:</b> {user[2]}
    <b>📞Telefon raqami:</b> {user[3]}
    <b>📌 Manzili:</b> {user[4]}
    <b>📝 Foydalanuvchi xabari:</b> \n\t<i>{message.text}</i>
    <b>📍 username:</b> @{user[1]}
            """, reply_markup=reply_markup(message.message_id))
            
        if LANGUAGE == 'uz':
            await message.answer("""✅ Xabaringiz yuborildi !

    ♻️ Xabaringiz 👨🏻‍💻 Admin tomonidan ko`rib chiqilib, ma`qul topilsa, 72 soat ichida javob xabari keladi 👍""")
        elif LANGUAGE == 'en':
            await message.answer("""✅ Your message has been sent!

    ♻️ If your message is reviewed and approved by the admin, you will receive a reply message within 72 hours 👍""")
        else:
            await message.answer("""✅ Ваше сообщение отправлено!

    ♻️ Если ваше сообщение будет рассмотрено и одобрено администратором, вы получите ответное сообщение в течение 72 часов 👍""")   
