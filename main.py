import asyncio
import logging.config

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from database.config import LOGGING_CONFIG, TOKEN


logger = logging.getLogger(__name__)
bot = Bot(token=TOKEN)

logging.config.dictConfig(LOGGING_CONFIG)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
