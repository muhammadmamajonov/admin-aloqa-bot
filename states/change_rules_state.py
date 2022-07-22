from aiogram.dispatcher.filters.state import StatesGroup, State

class ChangeRules(StatesGroup):
    change_uz = State()
    change_en = State()
    change_ru = State()