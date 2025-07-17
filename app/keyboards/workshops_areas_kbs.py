from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

workshops = InlineKeyboardMarkup(inline_keyboard=[                              # вибір по цехах
    [InlineKeyboardButton(text='Основний цех', callback_data='main_WS'),
     InlineKeyboardButton(text='Допоміжні цеха', callback_data='auxiliary_WS')],
    [InlineKeyboardButton(text='Відділи', callback_data='departments')]
])

mainWS = InlineKeyboardMarkup(inline_keyboard=[                                 # вибір напрямків
    [InlineKeyboardButton(text='Зборка плюшки', callback_data='bun_handling'),
     InlineKeyboardButton(text='Виготовлення бубликів', callback_data='making_bagels')],
    [InlineKeyboardButton(text='Штамповка', callback_data='stamping'),
     InlineKeyboardButton(text='Покраска', callback_data='painting')],
    [InlineKeyboardButton(text='Зборка ананасів', callback_data='pineapple'),
     InlineKeyboardButton(text='Зборка кукурудзи', callback_data='corn')],
    [InlineKeyboardButton(text='Трубочки', callback_data='tubes'),
     InlineKeyboardButton(text='Підготовчі роботи', callback_data='preparatory_work')]
#     InlineKeyboardButton(text='Термос', callback_data='thermos')]
])

auxiliaryWS = InlineKeyboardMarkup(inline_keyboard=[                              # вибір напрямків
    [InlineKeyboardButton(text='Майстерня', callback_data='repair_shop'),
     InlineKeyboardButton(text='Принтерна', callback_data='printers')],
    [InlineKeyboardButton(text='Фреза', callback_data='milling_cutter'),
     InlineKeyboardButton(text='Гільотина', callback_data='guillotine')],
    [InlineKeyboardButton(text='Погрузка', callback_data='loading')]
])

departments = InlineKeyboardMarkup(inline_keyboard=[                              # вибір напрямків
    [InlineKeyboardButton(text='Офіс', callback_data='office'),
     InlineKeyboardButton(text='Склад', callback_data='warehouse')],
    [InlineKeyboardButton(text='Франція', callback_data='france'),
     InlineKeyboardButton(text='Тести', callback_data='tests')],
    [InlineKeyboardButton(text='Електронщики', callback_data='electronics')]
])


#supervisor = InlineKeyboardMarkup(inline_keyboard=[                              # вибір керівника
#    [InlineKeyboardButton(text='Артем', callback_data='_artem'),
#     InlineKeyboardButton(text='Олександр', callback_data='_olexandr')],
#    [InlineKeyboardButton(text='Ігор', callback_data='_ihor')
#])