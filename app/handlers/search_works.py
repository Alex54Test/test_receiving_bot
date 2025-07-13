from aiogram import F, Router
from aiogram.types import CallbackQuery


import app.keyboards.workshops_areas_kbs as wakb
import app.keyboards.works_selesct_main_WS_kbs as mainwskb


router_sw = Router()


@router_sw.callback_query(F.data == 'day_start_end')                   # Ловимо вибір робочого звіту
async def day_start_end(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка місце роботи')
    await callback.message.answer('Оберіть будьласка місце роботи.'
                                  ' Мається на увазі місце де ви зараз будете працювати (працювали)',
                                  reply_markup=wakb.workshops)


@router_sw.callback_query(F.data == 'main_WS')                     # Ловимо напрямки, за якими працює людина
async def mainWS(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:',
                                  reply_markup=wakb.mainWS)


@router_sw.callback_query(F.data == 'auxiliary_WS')                # Ловимо напрямки, за якими працює людина
async def auxiliaryWS(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:',
                                  reply_markup=wakb.auxiliaryWS)


@router_sw.callback_query(F.data == 'departments')                 # Ловимо напрямки, за якими працює людина
async def departments(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:',
                                  reply_markup=wakb.departments)


@router_sw.callback_query(F.data == 'bun_handling')                # Ловимо види робіт
async def bunHandling(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.bunHandling)


@router_sw.callback_query(F.data == 'making_bagels')               # Ловимо види робіт
async def makingBagels(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.makingBagels)


@router_sw.callback_query(F.data == 'stamping')                    # Ловимо види робіт
async def stamping(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.stamping)


@router_sw.callback_query(F.data == 'painting')                    # Ловимо види робіт
async def painting(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.painting)