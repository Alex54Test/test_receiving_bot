from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bunHandling = InlineKeyboardMarkup(inline_keyboard=[                             # вибір робіт, Зборка плюшки
    [InlineKeyboardButton(text='Видавлювання плюшки', callback_data='extrusion_holes'),
     InlineKeyboardButton(text='Свердлівка отворів', callback_data='drilling_holes')],
    [InlineKeyboardButton(text='Зачистка отворів', callback_data='cleaning_holes'),
     InlineKeyboardButton(text='Заклепування плюшок', callback_data='riveting_buns')],
    [InlineKeyboardButton(text='Герметиз. ложемента', callback_data='cradle_sealing'),
     InlineKeyboardButton(text='Встановлення пушечки', callback_data='gun_installation')],
    [InlineKeyboardButton(text='Установка стопорних кілець на пушки', callback_data='installation_retaining_rings')],
    [InlineKeyboardButton(text='Вирівнювання заклепки проточування різьб', callback_data='rivet_alignment')],
    [InlineKeyboardButton(text='Установка канальної трубки', callback_data='channel_tube_install')],
    [InlineKeyboardButton(text='Термоусадження канальної трубки (фен)', callback_data='heat_shrinking')],
    [InlineKeyboardButton(text='Нанесення герметика', callback_data='sealant_application'),
     InlineKeyboardButton(text='Розподілення герметика', callback_data='distribution_sealant')],
    [InlineKeyboardButton(text='ВТК', callback_data='technical_control_dep'),
     InlineKeyboardButton(text='Розкладання плюшек', callback_data='transfer_buns')],
    [InlineKeyboardButton(text='Пакування плюшек', callback_data='packaging_buns')],
])

makingBagels = InlineKeyboardMarkup(inline_keyboard=[                            # вибір робіт, Виготовлення бубликів
    [InlineKeyboardButton(text='Нарізка гуми', callback_data='cutting_rubber'),
     InlineKeyboardButton(text='Проклеювання бублика', callback_data='gluing_bagel')],
    [InlineKeyboardButton(text='Свердлівка бублика', callback_data='bagel_drill')],
    [InlineKeyboardButton(text='Встановлення каналів та штирів', callback_data='channels&pins')],
    [InlineKeyboardButton(text='Проклеювання каналів', callback_data='gluing_channels'),
     InlineKeyboardButton(text='Герметизація каналів', callback_data='sealing_channels')],
    [InlineKeyboardButton(text='Зачистка бублика', callback_data='cleaning_bagel')],
    [InlineKeyboardButton(text='Вибірковий тех. контроль', callback_data='selective_control')]
])

stamping = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, Штамповка
    [InlineKeyboardButton(text='Штампування плюшки', callback_data='bun_stamping'),
     InlineKeyboardButton(text='Штампування кришки', callback_data='cap_stamping')],
    [InlineKeyboardButton(text='Штампування дна', callback_data='bottom_stamping'),
     InlineKeyboardButton(text='Загибання дна', callback_data='bending_of_bottom')],
    [InlineKeyboardButton(text='Калібровка після штамповки плюшки', callback_data='calibration_bun')],
    [InlineKeyboardButton(text='Калібровка після рубки кришки', callback_data='calibration_cap')],
    [InlineKeyboardButton(text='Зинковка кришки', callback_data='drilling_cap')],
    [InlineKeyboardButton(text='Рубка отворів у плюшці', callback_data='cutting_holes_bun')],
    [InlineKeyboardButton(text='Рубка отворів у кришці', callback_data='cutting_holes_cap')],
    [InlineKeyboardButton(text='Шліфовка болгаркою', callback_data='grinding_cap')],
    [InlineKeyboardButton(text='Заміна матриці', callback_data='matrix_replacement')]
])

painting = InlineKeyboardMarkup(inline_keyboard=[                              # вибір робіт, Покраска
    [InlineKeyboardButton(text='Маляр', callback_data='painter'),
     InlineKeyboardButton(text='Підмайстер', callback_data='journeyman_paint')],
])

preparatory_work = InlineKeyboardMarkup(inline_keyboard=[                      # вибір робіт, Підготовчі роботи
    [InlineKeyboardButton(text='Нарізка штиря', callback_data='pin_cutting'),
     InlineKeyboardButton(text='Шліфування фаски штиря', callback_data='pin_chamfer_grinding')],
    [InlineKeyboardButton(text='Миття штирів', callback_data='pin_washing'),
     InlineKeyboardButton(text='Миття квадратів', callback_data='washing_squares')],
    [InlineKeyboardButton(text='Нарізка УСБ під ящики', callback_data='cutting_usb_boxes'),
     InlineKeyboardButton(text='Складання ящиків', callback_data='making_boxes')]
])

pineapple = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, Зборка ананасів
    [InlineKeyboardButton(text='Прокат обичайки на вальцях', callback_data='roller_rolling')],
    [InlineKeyboardButton(text='Зварювання лазером', callback_data='laser_welding')],
    [InlineKeyboardButton(text='Точкове зварювання гайки з кришкою', callback_data='spot_welding_nut_cover')],
    [InlineKeyboardButton(text='Вальцювання на токарному верстаті обичайки', callback_data='rolling_on_lathe')],
    [InlineKeyboardButton(text='Зварювання кришки з гайкою до обичайки', callback_data='welding_cover_to_shell')],
    [InlineKeyboardButton(text='Накрутка смуги (первинна)', callback_data='strip_wrapping')],
    [InlineKeyboardButton(text='Встановлення (вкручування) смуги', callback_data='screwing_strip')],
    [InlineKeyboardButton(text='Затягування та приварювання смуги, шліфування',
                          callback_data='strip_tightening_welding_grinding')]
])

corn = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, Зборка кукурудзи
    [InlineKeyboardButton(text='Прокат обичайки на вальцях', callback_data='roller_rolling')],
    [InlineKeyboardButton(text='Зварювання лазером', callback_data='laser_welding')],
    [InlineKeyboardButton(text='Точкове зварювання гайки з кришкою', callback_data='spot_welding_nut_cover')],
    [InlineKeyboardButton(text='Вальцювання на токарному верстаті обичайки', callback_data='rolling_on_lathe')],
    [InlineKeyboardButton(text='Зварювання кришки з гайкою до обичайки', callback_data='welding_cover_to_shell')],
    [InlineKeyboardButton(text='Накрутка смуги (первинна)', callback_data='strip_wrapping')],
    [InlineKeyboardButton(text='Встановлення (вкручування) смуги', callback_data='screwing_strip')],
    [InlineKeyboardButton(text='Затягування та приварювання смуги, шліфування',
                          callback_data='strip_tightening_welding_grinding')]
])

tubes = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, Трубочки
    [InlineKeyboardButton(text='Нарізка термоусадки у розмір', callback_data='cutting_heat_shrink')],
    [InlineKeyboardButton(text='Поклейка штирів', callback_data='gluing_pins')],
    [InlineKeyboardButton(text='Заклепування квадратів', callback_data='rivet_squares')],
    [InlineKeyboardButton(text='Вкручування штир+квадрат+трубка', callback_data='pin_square_tube')],
    [InlineKeyboardButton(text='Обрізка трубки та встановлення заглушки',
                          callback_data='cutting_tubes_installing_plugs')],
    [InlineKeyboardButton(text='Первинна герметизація', callback_data='primary_sealing'),
     InlineKeyboardButton(text='Термоусадження трубки', callback_data='heat_shrink_tube')],
    [InlineKeyboardButton(text='Підрізування термоусадки у розмір', callback_data='cutting_heat_shrink')],
    [InlineKeyboardButton(text='Фінальна герметизація. Оператор', callback_data='final_sealing_operator')],
    [InlineKeyboardButton(text='Фінальна герметизація. Підмайстер', callback_data='final_sealing_journeyman')],
    [InlineKeyboardButton(text='Фінальна герметизація. Різноробочий', callback_data='final_sealing_handyman')],
    [InlineKeyboardButton(text='ВТК упаковка', callback_data='technical_control_package')]
])

