import logging
from random import randint
from aiogram import Bot, Dispatcher
from aiogram import types

bot = Bot(token="5704435807:AAGOVhRrtZxAZ_PcJ9iSZp4tkhV0mN-86aM", parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

