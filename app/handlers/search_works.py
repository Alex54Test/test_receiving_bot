from aiogram import F, Router
from aiogram.types import CallbackQuery


import app.keyboards.workshops_areas_kbs as wakb
import app.keyboards.works_selesct_main_WS_kbs as mainwskb
import app.keyboards.works_select_auxiliary_WS_kbs as auxwskb


router_sw = Router()


@router_sw.callback_query(F.data == 'day_start_end')                   # Ловимо вибір робочого звіту
async def day_start_end(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка місце роботи')
    await callback.message.answer('Оберіть будьласка місце роботи.'
                                  ' Мається на увазі місце де ви зараз будете працювати (працювали)',
                                  reply_markup=wakb.workshops)


@router_sw.callback_query(F.data == 'main_WS')                     # Ловимо напрямки, за якими працює людина
async def main_ws(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:',
                                  reply_markup=wakb.mainWS)


@router_sw.callback_query(F.data == 'auxiliary_WS')                # Ловимо напрямки, за якими працює людина
async def auxiliary_ws(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:',
                                  reply_markup=wakb.auxiliaryWS)


@router_sw.callback_query(F.data == 'departments')                 # Ловимо напрямки, за якими працює людина
async def departments(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка напрямок')
    await callback.message.answer('Оберіть будьласка напрямок:',
                                  reply_markup=wakb.departments)


@router_sw.callback_query(F.data == 'bun_handling')                # Ловимо види робіт, плюшки
async def bun_handling(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.bunHandling)


@router_sw.callback_query(F.data == 'making_bagels')               # Ловимо види робіт, бублики
async def making_bagels(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.makingBagels)


@router_sw.callback_query(F.data == 'stamping')                    # Ловимо види робіт, штамп
async def stamping(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.stamping)


@router_sw.callback_query(F.data == 'painting')                    # Ловимо види робіт, покраска
async def painting(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.painting)

@router_sw.callback_query(F.data == 'preparatory_work')            # Ловимо види робіт, підготовчі
async def preparatory_work(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.preparatory_work)

@router_sw.callback_query(F.data == 'pineapple')                    # Ловимо види робіт, ананас
async def pineapple(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.pineapple)

@router_sw.callback_query(F.data == 'corn')                        # Ловимо види робіт, кукурудза
async def corn(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.corn)

@router_sw.callback_query(F.data == 'tubes')                       # Ловимо види робіт, трубочки
async def tubes(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=mainwskb.tubes)

@router_sw.callback_query(F.data == 'repair_shop')                       # Ловимо види робіт, майстерня
async def repair_shop(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=auxwskb.repairShop)

@router_sw.callback_query(F.data == 'cap_assembly')                       # Ловимо види робіт, кришки
async def cap_assembly(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=auxwskb.capAssembly)

@router_sw.callback_query(F.data == 'gun_assembly')                       # Ловимо види робіт, пушечки
async def gun_assembly(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=auxwskb.gunAssembly)

@router_sw.callback_query(F.data == 'milling_cutter')                       # Ловимо види робіт, пушечки
async def milling_cutter(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=auxwskb.milling_cutter)

@router_sw.callback_query(F.data == 'guillotine')                       # Ловимо види робіт, пушечки
async def guillotine(callback: CallbackQuery):
    await callback.answer('Оберіть будьласка вид роботи')
    await callback.message.answer('Оберіть будьласка вид роботи:',
                                  reply_markup=auxwskb.guillotine)











