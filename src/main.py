from aiogram import Bot, Dispatcher
from src.config import Config
from src.services.sql import create_database
import asyncio


bot = Bot(token=Config.token)
dp = Dispatcher(bot=bot)
create_database()

async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stoped')
