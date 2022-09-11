import re
import time

import surrogates
from aiogram import types, Dispatcher, Bot
from magic import bot
from aiogram import filters






async def start(message: types.message):
    hello = surrogates.decode("	\ud83d\udc4b")
    back = surrogates.decode("	\u2728")
    await message.answer(f"{hello}")
    await message.answer(f"Я могу отправить тебе расписание на определенный день нажми на /Run или отправь мне этот смайлик - {back} (ВАЖНО!: после выбора дня внизу появится кнопочка со смайликом, нажми на нее прежде чем выбирать 2 день)")
    # смайлик красного восклицательного знака


async def keyboard(message: types.message):
    inlinekey = types.InlineKeyboardMarkup()
    inlinekey.add(types.InlineKeyboardButton("Monday", callback_data='Monday'))
    inlinekey.add(types.InlineKeyboardButton("Tuesday", callback_data='Tuesday'))
    inlinekey.add(types.InlineKeyboardButton("Wednesday", callback_data='Wednesday'))
    inlinekey.add(types.InlineKeyboardButton("Thursday", callback_data='Thursday'))
    inlinekey.add(types.InlineKeyboardButton("Friday", callback_data='Friday'))
    back = surrogates.decode("	\u2728")
    await message.answer(f"What day?{back}", reply_markup=inlinekey)


async def keyboardd(message: types.message):
    inlinekey = types.InlineKeyboardMarkup()
    inlinekey.add(types.InlineKeyboardButton("Monday", callback_data='Monday'))
    inlinekey.add(types.InlineKeyboardButton("Tuesday", callback_data='Tuesday'))
    inlinekey.add(types.InlineKeyboardButton("Wednesday", callback_data='Wednesday'))
    inlinekey.add(types.InlineKeyboardButton("Thursday", callback_data='Thursday'))
    inlinekey.add(types.InlineKeyboardButton("Friday", callback_data='Friday'))

    await message.answer(f"What day? {back}", reply_markup=inlinekey)


async def monday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    back = surrogates.decode("	\u2728")
    await bot.answer_callback_query(callback_query.id, text=f"{back} Monday {back}", show_alert=False)
    await bot.send_message(callback_query.from_user.id, "Физика at 8:30 - 9:15")
    await bot.send_message(callback_query.from_user.id, "Алгебра at 9:20 - 10:05")
    await bot.send_message(callback_query.from_user.id, "Казахский язык at 10:20 - 11:05")
    await bot.send_message(callback_query.from_user.id, "География at 11:20 - 12:05")
    await bot.send_message(callback_query.from_user.id, "История Казахстана at 12:10 - 12:55")
    await bot.send_message(callback_query.from_user.id, "Русский язык at 1:00 - 1:45")
    await bot.send_message(callback_query.from_user.id, "Физ-ра at 1:50 - 2:35", reply_markup=retk)
back = surrogates.decode("\u2728")


async def tuesday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Tuesday {back}", show_alert=False)
    await bot.send_message(callback_query.from_user.id, "Алгебра at 8:30 - 9:15")
    await bot.send_message(callback_query.from_user.id, "Химия at 9:20 - 10:05")
    await bot.send_message(callback_query.from_user.id, "Английский язык at 10:20 - 11:05")
    await bot.send_message(callback_query.from_user.id, "Русский язык at 11:20 - 12:05")
    await bot.send_message(callback_query.from_user.id, "Информатика at 12:10 - 12:55")
    await bot.send_message(callback_query.from_user.id, "Биология at 1:00 - 1:45")
    await bot.send_message(callback_query.from_user.id, "Русская литература at 1:50 - 2:35", reply_markup=retk)


async def wednesday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Wednesday {back}", show_alert=False)
    await bot.send_message(callback_query.from_user.id, "Алгебра at 8:30 - 9:15")
    await bot.send_message(callback_query.from_user.id, "Химия at 9:20 - 10:05")
    await bot.send_message(callback_query.from_user.id, "Физ-ра at 10:20 - 11:05")
    await bot.send_message(callback_query.from_user.id, "Английский at 11:20 - 12:05")
    await bot.send_message(callback_query.from_user.id, "Русская литература at 12:10 - 12:55")
    await bot.send_message(callback_query.from_user.id, "Казахский язык at 1:00 - 1:45")
    await bot.send_message(callback_query.from_user.id, "История Казахстана at 1:50 - 2:35", reply_markup=retk)


async def thursday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Thursday {back}", show_alert=False)
    await bot.send_message(callback_query.from_user.id, "Английский язык at 8:30 - 9:15")
    await bot.send_message(callback_query.from_user.id, "Всемирная история at 9:20 - 10:05")
    await bot.send_message(callback_query.from_user.id, "География at 10:20 - 11:05")
    await bot.send_message(callback_query.from_user.id, "Казахский язык at 11:20 - 12:05")
    await bot.send_message(callback_query.from_user.id, "Геометрия at 12:10 - 12:55")
    await bot.send_message(callback_query.from_user.id, "Русская литература at 1:00 - 1:45")
    await bot.send_message(callback_query.from_user.id, "Художественный труд at 1:50 - 2:35", reply_markup=retk)


async def friday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Friday {back}", show_alert=False)
    await bot.send_message(callback_query.from_user.id, "Основы права at 8:30 - 9:15")
    await bot.send_message(callback_query.from_user.id, "Биология at 9:20 - 10:05")
    await bot.send_message(callback_query.from_user.id, "Физика at 10:20 - 11:05")
    await bot.send_message(callback_query.from_user.id, "Геометрия at 11:20 - 12:05")
    await bot.send_message(callback_query.from_user.id, "Казахский язык at 12:10 - 12:55")
    await bot.send_message(callback_query.from_user.id, "св. и осн.религ at 1:00 - 1:45")
    await bot.send_message(callback_query.from_user.id, "Физ-ра at 1:50 - 2:35", reply_markup=retk)


def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(keyboard, text=["/Run", f"{back}"])
    dp.register_callback_query_handler(monday2, text="Monday")
    dp.register_callback_query_handler(tuesday2, text="Tuesday")
    dp.register_callback_query_handler(wednesday2, text="Wednesday")
    dp.register_callback_query_handler(thursday2, text="Thursday")
    dp.register_callback_query_handler(friday2, text="Friday")
