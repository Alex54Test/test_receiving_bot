from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

repairShop = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, майстерня
    [InlineKeyboardButton(text='Збирання кришок', callback_data='cap_assembly'),
     InlineKeyboardButton(text='Збирання пушечок', callback_data='gun_assembly')],
    [InlineKeyboardButton(text='Збирання автоматичних страховок', callback_data='automatic_insurances')],
    [InlineKeyboardButton(text='Свердління штирів для бубликів', callback_data='drilling_pins_bagels')],
    [InlineKeyboardButton(text='Свердління пластикових заглушок для трубочок',
                          callback_data='drilling_plastic_plugs_tubes')],
    [InlineKeyboardButton(text='Порізка трубочок для ЕДіків', callback_data='cutting_tubes_EDs')],
    [InlineKeyboardButton(text='Перевірка пластикових болтів та доробка різьблення',
                          callback_data='checking_plastic_bolts')],
    [InlineKeyboardButton(text='Виготовлення одиничних приладів', callback_data='manufacturing_single_devices')],
    [InlineKeyboardButton(text='Ремонтні роботи', callback_data='repair_works_m')]
])

capAssembly = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, Збирання кришок
    [InlineKeyboardButton(text='Перевірка, свердлівка різьблення мами', callback_data='check_drill_thread')],
    [InlineKeyboardButton(text='Нанесення герметика на різьблення маму',
                          callback_data='applying_sealant_to_thread')],
    [InlineKeyboardButton(text='Заклепування різьблення мами до кришки', callback_data='thread_riveting')],
    [InlineKeyboardButton(text='Розмазування герметика', callback_data='sealant_smearing')],
    [InlineKeyboardButton(text='Герметизація заклепок', callback_data='sealing_rivets'),
     InlineKeyboardButton(text='Нарізка прокладки EVA', callback_data='cutting_eva_pad')],
    [InlineKeyboardButton(text='Накліювання прокладки EVA', callback_data='gluing_eva_pad'),
     InlineKeyboardButton(text='Пакування', callback_data='packaging')]
])

gunAssembly = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, Збирання пушечок
    [InlineKeyboardButton(text='Первинна перевірка деталей на дефект', callback_data='initial_inspection')],
    [InlineKeyboardButton(text='Нарізка дроту для кілець',
                          callback_data='wire_cutting_ring')],
    [InlineKeyboardButton(text='Нарізка дроту для штифта', callback_data='wire_cutting_pin')],
    [InlineKeyboardButton(text='Згинання дроту для кільця', callback_data='bending_wire')],
    [InlineKeyboardButton(text='Накручування кільця', callback_data='winding_ring'),
     InlineKeyboardButton(text='Збирання втулки', callback_data='bushing_assembly')],
    [InlineKeyboardButton(text="З'єднання втулки з корпусом", callback_data='connection_bushing_body'),
     InlineKeyboardButton(text='Порізка паралону для пушечок', callback_data='cutting_paralon_guns')]
])
#
millingCutter = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, фреза
    [InlineKeyboardButton(text='Виготовлення штампів', callback_data='stamps_production'),
     InlineKeyboardButton(text='Виготовлення плат', callback_data='boards_production')],
    [InlineKeyboardButton(text='Виготовлення одиночних деталей', callback_data='single_parts_production')],
    [InlineKeyboardButton(text='Ремонтні роботи', callback_data='repair_works_f')]
])

guillotine = InlineKeyboardMarkup(inline_keyboard=[                                # вибір робіт, гільотина
    [InlineKeyboardButton(text='Порізка металлу 30*30', callback_data='metal_cut_30'),
     InlineKeyboardButton(text='Порізка металлу 40*40', callback_data='metal_cut_40')],
    [InlineKeyboardButton(text='Порізка металлу 56*56', callback_data='metal_cut_56'),
     InlineKeyboardButton(text='Ремонтні роботи', callback_data='repair_works_g')]
])







