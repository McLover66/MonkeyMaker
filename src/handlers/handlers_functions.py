# for sql
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, types



from aiogram.types import Message, LabeledPrice
from src.main import bot
from src.config import Config


price = [LabeledPrice(label='КР', amount=200000)]


async def test(message: Message):
    assert isinstance(bot.send_invoice, object)
    await bot.send_invoice(message.chat.id,  # функция выставляет счет
                           title='Контрольная',
                           description='desc',
                           provider_token=Config.pay_token,
                           currency='rub',
                           need_email='true',
                           prices=price,
                           need_phone_number=True,
                           start_parameter='example',
                           payload='some_invoice',
                           )


async def process_data_name(message: types.Message):
    user_message = message.text

    data = user_message.split("\n")

    if len(data) != 5:
        await message.answer("Пожалуйста, введите данные корректно (со сносом строки): \n имя(петя) \n фамилия(петров) \n возраст(20) \n университет(мгу) \n факультет(физика)")
        return

    name, lastname, age, university, faculty = data

    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO clients (name, lastname, age, university, faculty)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, lastname, age, university, faculty))

    conn.commit()
    print("Data committed to the database.")
    conn.close()

    await message.answer("Данные успешно сохранены!")
