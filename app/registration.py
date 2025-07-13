from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app import states as sts
from app.keyboards import main_kbs as kb

router_r = Router()

@router_r.message(Command('register'))                                # реєстрація
async def register(message: Message, state: FSMContext):
    await state.update_data(tgID=message.from_user.id)
    await state.set_state(sts.Register.firstName)
    await message.answer("Напишіть будьласка ваше ім'я")


@router_r.message(sts.Register.firstName)
async def register_firstName(message: Message, state: FSMContext):
    await state.update_data(firstName=message.text)
    await state.set_state(sts.Register.lastName)
    await message.answer("Напишіть будьласка ваше прізвище")


@router_r.message(sts.Register.lastName)
async def register_lastName(message: Message, state: FSMContext):
    await state.update_data(lastName=message.text)
    await state.set_state(sts.Register.surname)
    await message.answer("Напишіть будьласка ваше по батькові")


@router_r.message(sts.Register.surname)
async def register_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    data = await state.get_data()
    await message.answer(f'Вітаю вас, {data["firstName"]}.\nВаш ID: {data["tgID"]} \nПриємного дня.',
                         reply_markup=kb.main)
    await state.clear()