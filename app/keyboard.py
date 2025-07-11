from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = InlineKeyboardMarkup(inline_keyboard=[                                  # стартова меню
    [InlineKeyboardButton(text='Початок/завершення роботи', callback_data='day_start_end')],
    [InlineKeyboardButton(text='Особистий кабінет', callback_data='my_acc')]
])

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
    [InlineKeyboardButton(text='Трубочки', callback_data='straws'),
     InlineKeyboardButton(text='Термос', callback_data='thermos')]
])

auxiliaryWS = InlineKeyboardMarkup(inline_keyboard=[                              # вибір напрямків
    [InlineKeyboardButton(text='Майстерня', callback_data='repair_shop'),
     InlineKeyboardButton(text='Принтерна', callback_data='printers')],
    [InlineKeyboardButton(text='Фреза', callback_data='Milling_cutter'),
     InlineKeyboardButton(text='Зварювання', callback_data='welding')],
    [InlineKeyboardButton(text='Гільотина', callback_data='guillotine'),
     InlineKeyboardButton(text='Погрузка', callback_data='loading')]
])

departments = InlineKeyboardMarkup(inline_keyboard=[                              # вибір напрямків
    [InlineKeyboardButton(text='Офіс', callback_data='office'),
     InlineKeyboardButton(text='Склад', callback_data='warehouse')],
    [InlineKeyboardButton(text='Франція', callback_data='France'),
     InlineKeyboardButton(text='Тести', callback_data='tests')],
    [InlineKeyboardButton(text='Електронщики', callback_data='electronics')]
])

#supervisor = InlineKeyboardMarkup(inline_keyboard=[                              # вибір керівника
#    [InlineKeyboardButton(text='Артем', callback_data='_artem'),
#     InlineKeyboardButton(text='Олександр', callback_data='_olexandr')],
#    [InlineKeyboardButton(text='Ігор', callback_data='_ihor')
#])

bunHandling = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт
    [InlineKeyboardButton(text='Видавлювання плюшки', callback_data='extrusion_holes'),
     InlineKeyboardButton(text='Свердлівка отворів', callback_data='drilling_holes')],
    [InlineKeyboardButton(text='Зачистка отворів', callback_data='cleaning_holes'),
     InlineKeyboardButton(text='Заклепування плюшок', callback_data='riveting buns')],
    [InlineKeyboardButton(text='Герметиз. ложемента', callback_data='cradle_sealing'),
     InlineKeyboardButton(text='Встановлення пушки', callback_data='gun_installation')],
    [InlineKeyboardButton(text='Установка стопорних кілець на пушки', callback_data='installation_retaining_rings'),
     InlineKeyboardButton(text='Вирівнювання заклепки, проточування різьб', callback_data='rivet_alignment')],
    [InlineKeyboardButton(text='Установка канальної трубки', callback_data='channel_tube_install'),
     InlineKeyboardButton(text='Термоусадження канальної трубки(фен)', callback_data='heat_shrinking')],
    [InlineKeyboardButton(text='Нанесення герметика', callback_data='sealant_application'),
     InlineKeyboardButton(text='Розподілення герметика', callback_data='distribution_sealant')],
    [InlineKeyboardButton(text='ВТК', callback_data='technical_control_dep'),
     InlineKeyboardButton(text='Розкладання плюшек', callback_data='transfer_buns')],
    [InlineKeyboardButton(text='Пакування плюшек', callback_data='packaging_buns')],
])

makingBagels = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт
    [InlineKeyboardButton(text='Нарізка гуми', callback_data='cutting_rubber'),
     InlineKeyboardButton(text='Проклеювання бублика', callback_data='gluing_bagel')],
    [InlineKeyboardButton(text='Свердлівка бублика', callback_data='Bagel drill'),
     InlineKeyboardButton(text='Встановлення каналів та штирів', callback_data='channels&pins')],
    [InlineKeyboardButton(text='Проклеювання каналів', callback_data='gluing_channels'),
     InlineKeyboardButton(text='Герметизація каналів', callback_data='sealing_channels')],
    [InlineKeyboardButton(text='Зачистка бублика', callback_data='cleaning_bagel'),
     InlineKeyboardButton(text='Вибірковий тех. контроль бублика', callback_data='selective_control')]
])

stamping = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт
    [InlineKeyboardButton(text='Штампування плюшки', callback_data='bun_stamping'),
     InlineKeyboardButton(text='Штампування кришки', callback_data='cap stamping')],
    [InlineKeyboardButton(text='Штампування дна', callback_data='bottom_stamping'),
     InlineKeyboardButton(text='Загибання дна', callback_data='bending_of_bottom')],
    [InlineKeyboardButton(text='Калібровка після штамповки плюшки', callback_data='calibration_bun'),
     InlineKeyboardButton(text='Калібровка після рубки кришки', callback_data='calibration_cap')],
    [InlineKeyboardButton(text='Зинковка кришки', callback_data='drilling_cap'),
     InlineKeyboardButton(text='Рубка отворів у плюшці', callback_data='cutting_holes_bun')],
    [InlineKeyboardButton(text='Рубка отворів у кришці', callback_data='cutting_holes_cap'),
     InlineKeyboardButton(text='Шліфовка болгаркою', callback_data='grinding_cap')],
    [InlineKeyboardButton(text='Заміна матриці', callback_data='sealant_application')]
])

painting = InlineKeyboardMarkup(inline_keyboard=[                              # вибір робіт
    [InlineKeyboardButton(text='Маляр', callback_data='painter'),
     InlineKeyboardButton(text='Підмайстер', callback_data='journeyman_paint')],
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