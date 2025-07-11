from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboard as kb

router = Router()

@router.message(CommandStart())                                     # Ловимо /start
async def cmd_start(message: Message):
    await message.answer('Для роботи з ботом вам потрібно зареєструватись', reply_markup=kb.main)

@router.message(Command('help'))                                    # Ловимо /help
async def cmd_help(message: Message):
    await message.answer('Ви обрали меню допомоги. Щоб повернутись у головне меню натисніть /home')

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








#@router.message(F.text == 'Початок роботи')
#async def report(message: Message):
#    await message.answer('Оберіть будьласка місце роботи:', reply_markup=kb.workshops)

#@router.message(F.text == 'Завершення роботи')
#async def report(message: Message):
#    await message.answer('Оберіть будьласка місце роботи:', reply_markup=kb.workshops)

#@router.message(F.text == 'Особистий кабінет')
#async def report(message: Message):
#    await message.answer('В розробці')