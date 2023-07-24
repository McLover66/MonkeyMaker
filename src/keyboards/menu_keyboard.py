from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button1 = InlineKeyboardButton("Варианты", callback_data="button1")
button2 = InlineKeyboardButton("Кнопка 2", callback_data="button2")

keyboard = InlineKeyboardMarkup().add(button1, button2)
