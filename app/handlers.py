from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import app.keyboard as kb
import app.states as sts

router = Router()

@router.message(CommandStart())                                     # Ловимо /start
async def cmd_start(message: Message):
    await message.answer('Для роботи з ботом вам потрібно зареєструватись.\n'
                         'Для реэстраціі натисніть або напишіть команду /register')

@router.message(Command('help'))                                    # Ловимо /help
async def cmd_help(message: Message):
    await message.answer('Ви обрали меню допомоги.')

@router.callback_query(F.data == 'day_start_end')                   # Ловимо дату колбеків
async def daystartend(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка місце роботи')
    await callback.message.answer('Оберіть будьласка місце роботи.'
                                  ' Мається на увазі місце де ви зараз будете працювати (працювали)',
                                  reply_markup=kb.workshops)

@router.callback_query(F.data == 'my_acc')
async def myaccount(callback: CallbackQuery):
    await callback.answer('В розробці')
    await callback.message.answer('В розробці')

@router.callback_query(F.data == 'main_WS')
async def mainWS(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:', reply_markup=kb.mainWS)

@router.callback_query(F.data == 'auxiliary_WS')
async def auxiliaryWS(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:', reply_markup=kb.auxiliaryWS)

@router.callback_query(F.data == 'departments')
async def departments(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:', reply_markup=kb.departments)

@router.callback_query(F.data == 'bun_handling')
async def bunHandling(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:', reply_markup=kb.bunHandling)

@router.callback_query(F.data == 'making_bagels')
async def makingBagels(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:', reply_markup=kb.makingBagels)

@router.callback_query(F.data == 'stamping')
async def stamping(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:', reply_markup=kb.stamping)

@router.callback_query(F.data == 'painting')
async def painting(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:', reply_markup=kb.painting)



@router.message(Command('register'))                                # реєстрація
async def register(message: Message, state: FSMContext):
    await state.set_state(sts.Register.firstName)
    await message.answer("Напишіть будьласка ваше ім'я")

@router.message(sts.Register.firstName)
async def register_firstName(message: Message, state: FSMContext):
    await state.update_data(firstName=message.text)
    await state.set_state(sts.Register.lastName)
    await message.answer("Напишіть будьласка ваше прізвище")

@router.message(sts.Register.lastName)
async def register_lastName(message: Message, state: FSMContext):
    await state.update_data(lastName=message.text)
    await state.set_state(sts.Register.surname)
    await message.answer("Напишіть будьласка ваше по батькові")

@router.message(sts.Register.surname)
async def register_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    data = await state.get_data()
    await message.answer(f'Вітаю вас, {data["firstName"]}. Приємного дня.', reply_markup=kb.main)





