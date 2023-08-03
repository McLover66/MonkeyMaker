from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons_start = [
    InlineKeyboardButton("Варианты", callback_data="Variants"),
    InlineKeyboardButton("Поддержка", callback_data="Support"),
    InlineKeyboardButton("Хочу в команду", callback_data="Team"),
    InlineKeyboardButton("Скопировать @ссылку для друзей", callback_data="LINK"),
    InlineKeyboardButton("b", callback_data="button5"),
    InlineKeyboardButton("c", callback_data="button6"),
]

buttons_Variants = [
    InlineKeyboardButton("Тест", callback_data="Test"),
    InlineKeyboardButton("Контрольная", callback_data="CourceTest"),
    InlineKeyboardButton("Домашнее задание", callback_data="HW"),
    InlineKeyboardButton("Назад", callback_data="back")
]

buttons_Support = [
    InlineKeyboardButton("Вызвать поддержку", callback_data="CallSupport"),
    InlineKeyboardButton("Сообщить об ошибке", callback_data="TellSupport"),
    InlineKeyboardButton("", callback_data="."),
]


keyboard_start = InlineKeyboardMarkup().add(*buttons_start)
keyboard_Variants = InlineKeyboardMarkup().add(*buttons_Variants)
keyboard_Support = InlineKeyboardMarkup().add(*buttons_Support)

