import time
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
MSG = os.getenv('MSG')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await message.reply(f'Привет, {user_full_name}')

    time.sleep(60*60*3)
    await bot.send_message(user_id, MSG)


if __name__ == '__main__':
    executor.start_polling(dp)
