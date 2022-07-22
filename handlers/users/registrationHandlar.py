from aiogram import types
from aiogram.dispatcher import FSMContext
from states.registrationStates import Registration
from keyboards.inline.confirmationConsentKeyboard import consent_uz, consent_en, consent_ru
from keyboards.default.contactShareKeyboard import concat_button
from keyboards.default.replyKeyboardRemove import reply_keyboard_remove
from loader import dp, db

LANGUAGE = None

@dp.callback_query_handler(state=Registration.language_seletction)
async def set_lang(call: types.CallbackQuery):
    await Registration.rules.set()
    
    global LANGUAGE 
    LANGUAGE = call.data

    db.set_language(id=call.from_user.id, language=call.data)

    await call.message.delete()
    rules = db.get_rules()

    if call.data == 'uz':
        await call.message.answer(f"""
        📃 Qoidalar bilan tanishing!
            {rules[1]}""", reply_markup=consent_uz)
    elif call.data == 'en':
        await call.message.answer(f"""
        📃 See the rules!
            {rules[2]}""", reply_markup=consent_en)
    else:
        await call.message.answer(f"""
        📃 Смотрите правила!
            {rules[3]}""", reply_markup=consent_ru)


@dp.callback_query_handler(text='agree', state=Registration.rules)
async def rules_agree(call: types.CallbackQuery):
    
    await Registration.next()
    await call.message.delete()

    # user = db.select_user(id=call.from_user.id)
    if LANGUAGE == 'uz':
        await call.message.answer("Telefon raqamingizni yuborish uchun pastdagi tugmani bosing", reply_markup=concat_button)
    elif LANGUAGE == 'en':
        await call.message.answer("Press the button below to send your phone number", reply_markup=concat_button)
    else:
        await call.message.answer("Нажмите кнопку ниже, чтобы отправить свой номер телефона", reply_markup=concat_button)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Registration.contact_share)
async def get_phone(message: types.Message, state: FSMContext):
   
    await Registration.next()

    await state.update_data(
        {"phone": message.contact.phone_number}
    )
    
    # user = db.select_user(id=message.from_user.id)

    if LANGUAGE == 'uz':
        await message.answer("Manzilingizni kiriting", reply_markup=reply_keyboard_remove)
    elif LANGUAGE == 'en':
        await message.answer("Enter your address", reply_markup=reply_keyboard_remove)
    else:
        await message.answer("Введите свой адрес", reply_markup=reply_keyboard_remove)


@dp.message_handler(state=Registration.address)
async def get_address(message: types.Message, state: FSMContext):
    await Registration.next()
    
    await state.update_data(
        {"address": message.text}
    )

    # user = db.select_user(id=message.from_user.id)

    if LANGUAGE == 'uz':
        await message.answer("Ism va familyangizni kiriting.")
    elif LANGUAGE == 'en':
        await message.answer("Enter your full name.")
    else:
        await message.answer("Введите свое имя и фамилию.")

@dp.message_handler(state=Registration.fullName)
async def get_address(message: types.Message, state: FSMContext):
    data = await state.get_data()
    full_name = message.text
    address = data.get('address')
    phone = data.get('phone')

    db.edit_user(id=message.from_user.id, full_name=full_name, phone=phone, address=address)

    await state.finish()

    if LANGUAGE == 'uz':
        await message.answer("Xabaringizni yuborishingiz mumkin.")
    elif LANGUAGE == 'en':
        await message.answer("You can send your message.")
    else:
        await message.answer("Вы можете отправить свое сообщение.")    