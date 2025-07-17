from aiogram.fsm.state import State, StatesGroup



class Register(StatesGroup):
    tgID = str
    firstName = State()
    lastName = State()
    surname = State()

