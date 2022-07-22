from aiogram import types
from aiogram.dispatcher import FSMContext
from states.reply_message_state import ReplyMessage
from loader import dp, db, bot

@dp.callback_query_handler(text_contains='reply_to_this_message=')
async def reply_to_message(callback: types.CallbackQuery, state: FSMContext):
    await ReplyMessage.reply.set()
    message_id = callback.data.split('=')[1]
    await state.update_data(
        {'message_id':message_id}
    )

    await callback.message.answer("Javob Xabarini yuboring.")


@dp.message_handler(state=ReplyMessage.reply)
async def answer_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_id = data.get('message_id')
    user_id = db.select_message(id=message_id)
    
    await bot.send_message(chat_id=user_id[0], text=message.text, reply_to_message_id=message_id)
    await message.answer("✅ Javob xabaringiz yuborildi")
    db.set_replied(message_id)
    await state.finish()
