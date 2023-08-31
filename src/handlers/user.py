from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, ChatType, ContentType, CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, types

import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from src.main import bot, dp
from src.config import Config

from src.keyboards.menu_keyboard import keyboard_start
from src.keyboards.menu_keyboard import keyboard_Variants
from src.keyboards.menu_keyboard import keyboard_Support

from src.handlers.handlers_functions import test
from src.handlers.handlers_functions import process_data_name


@dp.message_handler(commands=['start'])
async def show_inline_keyboard(message: Message):
    await message.answer("Выберите опцию:", reply_markup=keyboard_start)


@dp.callback_query_handler(text=["data", "new_order", "Support", "LINK", "Team"])
async def on_main_keyboard_button_clicked(callback_query: CallbackQuery):
    if callback_query.data == "data":
        await enter_data(callback_query.message)
    if callback_query.data == "new_order":
        await callback_query.message.edit_text("Выберите вариант услуги:", reply_markup=keyboard_Variants)
    if callback_query.data == "LINK":
        await callback_query.message.answer(text=Config.bot_link, disable_web_page_preview=True)
    if callback_query.data == "Team":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")
    elif callback_query.data == "Support":
        await callback_query.message.edit_text("Какой тип поддержки вам нужен:", reply_markup=keyboard_Support)


# Обработчик события для нажатия на кнопки в клавиатуре "Варианты"
@dp.callback_query_handler(text=["CourceTest", "Hw", "back", "Test"])
async def on_variants_keyboard_button_clicked(callback_query: CallbackQuery):
    if callback_query.data == "CourceTest":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")
    if callback_query.data == "Hw":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")

    if callback_query.data == "Test":
        await test(callback_query.message) # применяем функцию

    if callback_query.data == "back":
        await callback_query.message.edit_text("Выберите опцию:", reply_markup=keyboard_start)


# Обработчик события для нажатия на кнопки в клавиатуре "Поддержка"
@dp.callback_query_handler(text=["CallSupport", "TellSupport", "back"])
async def on_support_keyboard_button_clicked(callback_query: CallbackQuery):
    if callback_query.data == "CallSupport":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")
    if callback_query.data == "TellSupport":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")
    if callback_query.data == "back":
        await callback_query.message.edit_text("Выберите опцию:", reply_markup=keyboard_start)




@dp.pre_checkout_query_handler(lambda query: True)  # выполняется всегда
async def pre_checkout_process(pre_checkout: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def sucessful_payment(message, Message):
    await bot.send_message(message.chat.id, 'Плвтеж прошел успешно!')



# обрабоотчик кнопки ввести данные
@dp.message_handler(lambda message: message.text == "Ввести данные")
async def enter_data(message: types.Message):
    await message.answer("Введите данные построчно с маленькой буквы со сносом: "
                         "\n имя(петя) "
                         "\n фамилия(петров) "
                         "\n возраст(20) "
                         "\n университет(мгу) "
                         "\n факультет(физика)")
    dp.register_message_handler(process_data_name)

