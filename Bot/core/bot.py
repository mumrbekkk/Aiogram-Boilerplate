from aiogram import Bot, Dispatcher

from .config import TG_BOT_TOKEN
from .logger import setup_logger
from ..handlers import routers

setup_logger()


bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()


for router in routers:
    dp.include_router(router)


async def main():
    await dp.start_polling(bot)


