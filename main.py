import asyncio
import os
from aiogram import Bot, Dispatcher

from app.handlers.main_handlers import router_mh
from app.registration import router_r
from app.handlers.search_works import router_sw


async def main():
    # get the token from environment variable or throw an error if not set
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")
    
    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(router_sw)
    dp.include_router(router_mh)
    dp.include_router(router_r)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
