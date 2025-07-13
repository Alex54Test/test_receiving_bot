import asyncio
from aiogram import Bot, Dispatcher

from app.handlers.main_handlers import router_mh
from app.registration import router_r
from app.handlers.search_works import router_sw


async def main():
    bot = Bot(token='7247916657:AAGPzxKSCqd_-fwBEqFBC2vO-CziUXLm6r4')
    dp = Dispatcher()
    dp.include_router(router_sw)
    dp.include_router(router_mh)
    dp.include_router(router_r)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
