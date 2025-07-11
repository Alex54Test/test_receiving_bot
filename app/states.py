from aiogram.fsm.state import State, StatesGroup



class Register(StatesGroup):
    firstName = State()
    lastName = State()
    surname = State()