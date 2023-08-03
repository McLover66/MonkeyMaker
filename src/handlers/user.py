from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, ChatType, ContentType, CallbackQuery
from aiogram.dispatcher.filters import Command

from src.main import bot, dp
from src.config import Config

from src.keyboards.menu_keyboard import keyboard_start
from src.keyboards.menu_keyboard import keyboard_Variants
from src.keyboards.menu_keyboard import keyboard_Support

from src.handlers.handlers_functions import test


@dp.message_handler(commands=['start'])
async def show_inline_keyboard(message: Message):
    await message.answer("Выберите опцию:", reply_markup=keyboard_start)


@dp.callback_query_handler(text=["Variants", "Support", "LINK",])
async def on_main_keyboard_button_clicked(callback_query: CallbackQuery):
    if callback_query.data == "Variants":
        # await callback_query.message.answer("Выберите вариант услуги:", reply_markup=keyboard_Variants)
        await callback_query.message.edit_text("Выберите вариант услуги:", reply_markup=keyboard_Variants)
    if callback_query.data == "LINK":
        await callback_query.message.answer(text=bot_link, disable_web_page_preview=True)
    elif callback_query.data == "Support":
        await callback_query.message.answer("Какой тип поддержки вам нужен:", reply_markup=keyboard_Support)


# Обработчик события для нажатия на кнопки в клавиатуре "Варианты"
@dp.callback_query_handler(text=["CourceTest", "Hw", "back", "Test"])
async def on_variants_keyboard_button_clicked(callback_query: CallbackQuery):
    if callback_query.data == "CourceTest":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")
    if callback_query.data == "Hw":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")
    if callback_query.data == "Test":
        await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")
    if callback_query.data == "back":
        await callback_query.message.edit_text("Выберите опцию:", reply_markup=keyboard_start)


# Обработчик события для нажатия на кнопки в клавиатуре "Поддержка"
@dp.callback_query_handler(text=["CallSupport", "TellSupport"])
async def on_support_keyboard_button_clicked(callback_query: CallbackQuery):
    await callback_query.message.answer(f"Вы нажали кнопку '{callback_query.data}'.")


@dp.callback_query_handler(text="Test")
async def on_test_button_clicked(callback_query: CallbackQuery):
    await test(callback_query.message)


@dp.pre_checkout_query_handler(lambda query: True)  # выполняется всегда
async def pre_checkout_process(pre_checkout: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def sucessful_payment(message, Message):
    await bot.send_message(message.chat.id, 'Плвтеж прошел успешно!')
