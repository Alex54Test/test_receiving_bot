from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


office = InlineKeyboardMarkup(inline_keyboard=[                                 # вибір робіт, офіс
    [InlineKeyboardButton(text='Бухгалтерія', callback_data='accounting')],
    [InlineKeyboardButton(text='Кадри', callback_data='personnel')],
    [InlineKeyboardButton(text='Конструктори', callback_data='constructors')],
    [InlineKeyboardButton(text='Закупівельник', callback_data='buyer')],
    [InlineKeyboardButton(text='Менеджер з постачання', callback_data='supply_manager')],
    [InlineKeyboardButton(text='Менеджер з логістики', callback_data='logistics_manager')]
])

accounting = InlineKeyboardMarkup(inline_keyboard=[                             # вибір робіт, бухгалтерія
    [InlineKeyboardButton(text='Головний бухгалтер', callback_data='chief_accountant')],
    [InlineKeyboardButton(text='Бухгалтер', callback_data='accountant')]
])

personnel = InlineKeyboardMarkup(inline_keyboard=[                              # вибір робіт, карди
    [InlineKeyboardButton(text='Керівник відділу кадрів', callback_data='head_HR_dep')],
    [InlineKeyboardButton(text='Спеціаліст відділу кадрів', callback_data='personnel_dep_specialist')],
    [InlineKeyboardButton(text='Менеджер з персоналу', callback_data='personnel_manager')]
])

constructors = InlineKeyboardMarkup(inline_keyboard=[                             # вибір робіт, бухгалтерія
    [InlineKeyboardButton(text='Головний конструктор', callback_data='chief_designer')],
    [InlineKeyboardButton(text='Конструктор', callback_data='designer')]
])

france = InlineKeyboardMarkup(inline_keyboard=[                                 # вибір робіт, франція
    [InlineKeyboardButton(text='Скалодроми', callback_data='climbing_walls'),
     InlineKeyboardButton(text='Гумові вкладиші', callback_data='rubber_liners')],
    [InlineKeyboardButton(text='Сборка елементу ініціації', callback_data='initiation_element')]
])

climbingWalls = InlineKeyboardMarkup(inline_keyboard=[                          # вибір робіт, скалодроми
    [InlineKeyboardButton(text='Шліфування', callback_data='grinding'),
     InlineKeyboardButton(text='Розкладання за кольором', callback_data='sorting_by_color')],
    [InlineKeyboardButton(text='Ґрунтування', callback_data='padding')],
    [InlineKeyboardButton(text='Нанесення епоксидної смоли', callback_data='applying_epoxy_resin')],
    [InlineKeyboardButton(text='Нанесення повторних шарів епоксидки', callback_data='repeated_layers_epoxy_resin')],
    [InlineKeyboardButton(text='Посипання склом', callback_data='sprinkled_glass'),
     InlineKeyboardButton(text='Нанесення фінального шару', callback_data='applying_final_layer')],
    [InlineKeyboardButton(text='Виправлення дефектів', callback_data='correction_defects'),
     InlineKeyboardButton(text='Зачищення торців', callback_data='cleaning_ends')],
    [InlineKeyboardButton(text='Встановлення бульдогів', callback_data='bulldog_installation')],
    [InlineKeyboardButton(text='Нарізка стикувальних планок', callback_data='cutting_joining_strips')],
    [InlineKeyboardButton(text='Нарізка та склеювання кутових планок', callback_data='cutting_corner_strips')],
    [InlineKeyboardButton(text='Нарізка та збирання їжачків', callback_data='cutting_assembling_hedgehogs')],
    [InlineKeyboardButton(text='Підготовка листів для друку', callback_data='preparing_sheets_printing')],
    [InlineKeyboardButton(text='Монтаж', callback_data='installation')]
])

tests = InlineKeyboardMarkup(inline_keyboard=[                                  # вибір робіт, тестувальники
    [InlineKeyboardButton(text='Керівник тестувальників', callback_data='head_testers'),
     InlineKeyboardButton(text='Тестувальник', callback_data='tester')],
    [InlineKeyboardButton(text='Ремонтні роботи', callback_data='repair_works_t')]
])

electronics = InlineKeyboardMarkup(inline_keyboard=[                                 # вибір робіт, електронщики
    [InlineKeyboardButton(text='SmartB', callback_data='SmartB'),
     InlineKeyboardButton(text='ПП-павук', callback_data='PP_spider')],
    [InlineKeyboardButton(text='Плюша', callback_data='bun'),
     InlineKeyboardButton(text='Маг', callback_data='mag')],
    [InlineKeyboardButton(text='Доплер', callback_data='doppler')]
])
