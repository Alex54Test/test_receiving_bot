from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

router_mh = Router()

@router_mh.message(CommandStart())                                     # Ловимо /start
async def cmd_start(message: Message):
    await message.answer('Для роботи з ботом вам потрібно зареєструватись.\n'
                         'Для реэстраціі натисніть або напишіть команду /register')

@router_mh.message(Command('help'))                                    # Ловимо /help
async def cmd_help(message: Message):
    await message.answer('Ви обрали меню допомоги.')

@router_mh.callback_query(F.data == 'my_acc')                      #Планується лінк на особистий кабінет
async def myaccount(callback: CallbackQuery):
    await callback.answer('В розробці')
    await callback.message.answer('В розробці')





