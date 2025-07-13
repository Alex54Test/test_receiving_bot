from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main = InlineKeyboardMarkup(inline_keyboard=[                                  # стартова меню
    [InlineKeyboardButton(text='Початок/завершення\n роботи', callback_data='day_start_end'),
    InlineKeyboardButton(text='Особистий кабінет', callback_data='my_acc')]
])




#main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Початок роботи')],
#                                     [KeyboardButton(text='Завершення роботи')],
#                                     [KeyboardButton(text='Особистий кабінет')]],
#                           resize_keyboard=True,
#                           input_field_placeholder='Оберіть пункт меню...')



## catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кукурудза', callback_data='corn')],
##                                                [InlineKeyboardButton(text='Ананас', callback_data='pineapple')],
##                                                [InlineKeyboardButton(text='Плюшка', callback_data='bun')],
##                                               [InlineKeyboardButton(text='Термос', callback_data='thermos')]])