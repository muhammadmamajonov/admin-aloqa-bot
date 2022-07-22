from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class Registration(StatesGroup):
    language_seletction = State()
    rules = State()
    contact_share = State()
    address = State()
    fullName = State()