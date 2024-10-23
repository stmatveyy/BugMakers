from aiogram import Bot as bt
from aiogram.enums import ParseMode
from config import CONFIG
import asyncio
import logging
import sys
import atexit
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage, Redis

from handlers import start

# redis = Redis(host='localhost', port=6379)
# storage = RedisStorage(redis=redis)

bot = bt(CONFIG.token, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
loop = asyncio.get_event_loop()


dp.include_router(start.start_router)


@atexit.register
def a_exit() -> None:
    logging.debug("Бот выключается ...")
    loop.close()
    logging.debug("Бот выключен")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    loop.run_until_complete(main())
