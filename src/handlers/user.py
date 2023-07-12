from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, ChatType, ContentType
from aiogram.dispatcher.filters import Command

from src.main import bot, dp
from src.config import Config

price = [LabeledPrice(label='КР', amount=200000)]



@dp.message_handler(Command('start'))
async def start(message: Message):
    assert isinstance(bot.send_invoice, object)
    await bot.send_invoice(message.chat.id,                             #функция выставляет счет
                           title='Контерольная',
                           description='desc',
                           provider_token=Config.pay_token,
                           currency='rub',
                           need_email='true',
                           prices=price,
                           need_phone_number='true'
                           start_parameter='example',
                           payload='some_invoice',
                           )

@dp.pre_checkout_query_handler(lambda query: True) # выполняется всегда
async def pre_checkout_process(pre_checkout: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)



@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def sucessful_payment(message, Message):
    await bot.send_message(message.chat.id, 'Плвтеж прошел успешно!')
