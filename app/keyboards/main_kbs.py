from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main = InlineKeyboardMarkup(inline_keyboard=[                                  # стартова меню
    [InlineKeyboardButton(text='Початок/завершення роботи', callback_data='day_start_end')],
    [InlineKeyboardButton(text='Особистий кабінет', callback_data='my_acc')],
    [InlineKeyboardButton(text='Як працює цей бот', callback_data='help')]
])

