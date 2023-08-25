# for sql
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

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








