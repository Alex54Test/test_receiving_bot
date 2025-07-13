from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bunHandling = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт
    [InlineKeyboardButton(text='Видавлювання плюшки', callback_data='extrusion_holes'),
     InlineKeyboardButton(text='Свердлівка отворів', callback_data='drilling_holes')],
    [InlineKeyboardButton(text='Зачистка отворів', callback_data='cleaning_holes'),
     InlineKeyboardButton(text='Заклепування плюшок', callback_data='riveting buns')],
    [InlineKeyboardButton(text='Герметиз. ложемента', callback_data='cradle_sealing'),
     InlineKeyboardButton(text='Встановлення пушечки', callback_data='gun_installation')],
    [InlineKeyboardButton(text='Установка стопорних\n кілець на пушки', callback_data='installation_retaining_rings'),
     InlineKeyboardButton(text='Вирівнювання заклепки\n проточування різьб', callback_data='rivet_alignment')],
    [InlineKeyboardButton(text='Установка канальної\n трубки', callback_data='channel_tube_install'),
     InlineKeyboardButton(text='Термоусадження канальної\n трубки (фен)', callback_data='heat_shrinking')],
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
     InlineKeyboardButton(text='Встановлення каналів\n та штирів', callback_data='channels&pins')],
    [InlineKeyboardButton(text='Проклеювання каналів', callback_data='gluing_channels'),
     InlineKeyboardButton(text='Герметизація каналів', callback_data='sealing_channels')],
    [InlineKeyboardButton(text='Зачистка бублика', callback_data='cleaning_bagel'),
     InlineKeyboardButton(text='Вибірковий тех.\n контроль бублика', callback_data='selective_control')]
])
stamping = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт
    [InlineKeyboardButton(text='Штампування плюшки', callback_data='bun_stamping'),
     InlineKeyboardButton(text='Штампування кришки', callback_data='cap stamping')],
    [InlineKeyboardButton(text='Штампування дна', callback_data='bottom_stamping'),
     InlineKeyboardButton(text='Загибання дна', callback_data='bending_of_bottom')],
    [InlineKeyboardButton(text='Калібровка після\n штамповки плюшки', callback_data='calibration_bun'),
     InlineKeyboardButton(text='Калібровка після\n рубки кришки', callback_data='calibration_cap')],
    [InlineKeyboardButton(text='Зинковка кришки', callback_data='drilling_cap'),
     InlineKeyboardButton(text='Рубка отворів\n у плюшці', callback_data='cutting_holes_bun')],
    [InlineKeyboardButton(text='Рубка отворів\n у кришці', callback_data='cutting_holes_cap'),
     InlineKeyboardButton(text='Шліфовка болгаркою', callback_data='grinding_cap')],
    [InlineKeyboardButton(text='Заміна матриці', callback_data='matrix_replacement')]
])
painting = InlineKeyboardMarkup(inline_keyboard=[                              # вибір робіт
    [InlineKeyboardButton(text='Маляр', callback_data='painter'),
     InlineKeyboardButton(text='Підмайстер', callback_data='journeyman_paint')],
])