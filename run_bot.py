import asyncio
import os

from aiogram import Bot, Dispatcher

from handlers import router
from callback_stores.callback_today_store import router_store_today

from dotenv import load_dotenv

load_dotenv()

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN")) # экземпляр класса бота с токеном
    dp = Dispatcher()                       # диспетчер(то через чего всё работатет,обработчик)

    dp.include_router(router)
    dp.include_router(router_store_today)



    await dp.start_polling(bot)             # отправка запросов на сервера телеграм


if __name__ == "__main__":                  # запуск скрипта(точка входа)
    asyncio.run(main())                 # запуск асинхронной функции