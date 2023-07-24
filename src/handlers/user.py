from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, ChatType, ContentType, CallbackQuery
from aiogram.dispatcher.filters import Command

from src.main import bot, dp
from src.config import Config
from src.keyboards.menu_keyboard import keyboard

price = [LabeledPrice(label='КР', amount=200000)]



@dp.message_handler(commands=['start'])
async def show_inline_keyboard(message: Message):
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@dp.callback_query_handler(text="button1")
async def on_button1_clicked(callback_query: CallbackQuery):
    await variants(callback_query.message)

async def variants(message: Message):
    assert isinstance(bot.send_invoice, object)
    await bot.send_invoice(message.chat.id,                             #функция выставляет счет
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

@dp.pre_checkout_query_handler(lambda query: True)  # выполняется всегда
async def pre_checkout_process(pre_checkout: PreCheckoutQuery):
    # Здесь вы можете добавить логику обработки предварительного запроса, например,
    # проверку статуса платежа и возврат True или False в зависимости от результата.
    # Верните True, чтобы разрешить платеж, или False, чтобы отклонить его.
    # В этом примере, всегда возвращаем True, чтобы разрешить платеж.
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def sucessful_payment(message, Message):
    await bot.send_message(message.chat.id, 'Плвтеж прошел успешно!')
