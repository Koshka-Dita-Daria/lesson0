from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import crud_functions
from admin import *
from crud_functions import *
import asyncio

crud_functions.get_all_products()
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = InlineKeyboardMarkup()
KeyboardButton1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
KeyboardButton2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(KeyboardButton2, KeyboardButton1)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)

InlineButton1 = KeyboardButton(text='Информация')
InlineButton2 = KeyboardButton(text='Рассчитать')
InlineButton3 = KeyboardButton(text='Купить', callback_data='back_to_catalog')
kb1.add(InlineButton2, InlineButton1)
kb1.add(InlineButton3)

buy_kb = InlineKeyboardMarkup(resize_keyboard=True,
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт1', callback_data="product_buying"),
        InlineKeyboardButton(text='Продукт2', callback_data="product_buying"),
        InlineKeyboardButton(text='Продукт3', callback_data="product_buying"),
        InlineKeyboardButton(text='Продукт4', callback_data="product_buying")]
    ]
)
buy_kb.row()
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=["Купить"])
async def get_buying_list(message):
    for i in get_all_products():
        with open(f'Images/{i[0]}.png', "rb") as img:
            await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}', )
            await message.answer_photo(img, )

    await message.answer("Выберите продукт для покупки:", reply_markup=buy_kb)

@dp.callback_query_handler(text=["product_buying"])
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb)
@dp.callback_query_handler(text=["formulas"])
async def get_formulas(call):
    await call.message.answer("10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb1)

@dp.callback_query_handler(text=["calories"])
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    c = 10*float(data['second'])+6.25*float(data['third'])-5*float(data['first'])-161
    await message.answer(f"Ваша норма калорий {c}")
    await state.finish()

@dp.message_handler()
async def other(message):
    await message.answer("Введите команду /start, чтобы начать общение")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
