from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons_start = [
    InlineKeyboardButton("заполнить данные", callback_data="data"),
    InlineKeyboardButton("Новый заказ", callback_data="new_order"),
    InlineKeyboardButton("Поддержка", callback_data="Support"),
    InlineKeyboardButton("Хочу в команду", callback_data="Team"),
    InlineKeyboardButton("Скопировать @ссылку для друзей", callback_data="LINK")
]

buttons_new_order = [
    InlineKeyboardButton("Тест", callback_data="Test"),
    InlineKeyboardButton("Контрольная", callback_data="CourceTest"),
    InlineKeyboardButton("Домашнее задание", callback_data="Hw"),
    InlineKeyboardButton("Назад", callback_data="back")
]


buttons_Support = [
    InlineKeyboardButton("Вызвать поддержку", callback_data="CallSupport"),
    InlineKeyboardButton("Сообщить об ошибке", callback_data="TellSupport"),
    InlineKeyboardButton("Назад", callback_data="back")
]


keyboard_start = InlineKeyboardMarkup().add(*buttons_start)
keyboard_Variants = InlineKeyboardMarkup().add(*buttons_new_order)
keyboard_Support = InlineKeyboardMarkup().add(*buttons_Support)

