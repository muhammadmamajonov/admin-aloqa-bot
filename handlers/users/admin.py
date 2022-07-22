from datetime import datetime, date
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.edit_rules_keyboard import edit_rules_keyboard
from states.change_rules_state import ChangeRules
from data.config import ADMINS
from loader import dp, db, bot



@dp.message_handler(text="📬 Xabarlar")
async def messages(message: types.Message):
    messages = db.select_all_messages()
    messages_list = "<b>📬 Xabarlar ro`yxati !</b>\n"
    for msg in messages:
        user = db.select_user(msg[1])        
        messages_list += f"""
        <b>👤 Kimdan:</b> {user[2]}  
        <b>☎️ Telefon nomer:</b> {user[3]}
        <b>⏰Vaqti:</b> {msg[3]}
        <b>📨 Xabar:</b> {msg[2]}

        ➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """
    
    print(messages_list)
    await message.answer(text=messages_list)

@dp.message_handler(text="📊 Statistika")
async def stats(message: types.Message):
    users_amount = db.count_users()[0]
    messages_amaount = db.count_messages()[0]
   
    stat = f"""
    Bugungi sana: {date.today()}

    👥 Foydalanuvchilar soni: {users_amount} nafar

    📝 Xabarlar soni: {messages_amaount} ta
    """

    await message.answer(text=stat)


@dp.message_handler(text="🔔 Qoidalarni sozlash")
async def set_rules(message: types.Message):
    rules = db.get_rules()

    rules_txt = f"""
{rules[1]}
------------------------
{rules[2]}
------------------------
{rules[3]}
"""

    await message.answer(text=rules_txt, reply_markup=edit_rules_keyboard)

@dp.callback_query_handler(text='change_rules_uz')
async def set_state_change_rules_uz(call: types.CallbackQuery):
    await ChangeRules.change_uz.set()
    await call.message.answer("Yangi qoidalarni kiriting!")

@dp.message_handler(state=ChangeRules.change_uz)
async def change_rules_uz(message: types.Message, state: FSMContext):
    db.set_rules_uz(rules_uz=message.text)
    await message.answer("✅ o'zgartirildi")
    await state.finish()


@dp.callback_query_handler(text='change_rules_en')
async def set_state_change_rules_en(call: types.CallbackQuery):
    await ChangeRules.change_en.set()
    await call.message.answer("Enter new rules!")

@dp.message_handler(state=ChangeRules.change_en)
async def change_rules_en(message: types.Message, state: FSMContext):
    print(message.text)
    db.set_rules_en(rules_en=message.text)
    await message.answer("✅ changed")
    await state.finish()


@dp.callback_query_handler(text='change_rules_ru')
async def set_state_change_rules_ru(call: types.CallbackQuery):
    await ChangeRules.change_ru.set()
    await call.message.answer("Введите новые правила!")

@dp.message_handler(state=ChangeRules.change_ru)
async def change_rules_ru(message: types.Message, state: FSMContext):
    db.set_rules_ru(rules_ru=message.text)
    await message.answer("✅ измененный")
    await state.finish()


    