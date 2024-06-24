import asyncio
import logging
import json
import sys
import requests
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = '7157308982:AAHyoSDXED4metDeZLRCUTwa1TViACneHp8'

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    with open('data.json', 'r') as f:
        page = json.load(f)['page']
    if message.text == 'Next':
        page += 1
    else:
        page -= 1
    with open('data.json', 'w') as f:
        json.dump({'page': page}, f)
    data = requests.get('https://rickandmortyapi.com/api/character?page=' + str(page))
    if data.status_code == 200:
        for i in data.json()['results']:
            await message.answer_photo(photo=i['image'], caption=i['name'])
    else:
        await message.answer('след стр назд!')



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
