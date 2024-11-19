import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

logging.basicConfig(level=logging.INFO)

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
activity_data = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}

kb_1 = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Информация')
button_2 = KeyboardButton(text='Рассчитать')
kb_1.add(button_1)
kb_1.add(button_2)

inline_kb_1 = InlineKeyboardMarkup()
inline_button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button_4 = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
inline_kb_1.add(inline_button_3)
inline_kb_1.add(inline_button_4)

kb_2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='м'), KeyboardButton(text='ж')]], resize_keyboard=True)


class UserState(StatesGroup):
    sex = State()
    age = State()
    height = State()
    weight = State()
    daily_activity = State()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Введите "Рассчитать", чтобы посчитать свои калории',
                         reply_markup=kb_1)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот помогающий твоему здоровью', reply_markup=kb_1)


@dp.message_handler(text='Рассчитать')
async def calculate(message):
    await message.answer('Выберите вариант', reply_markup=inline_kb_1)


@dp.callback_query_handler(text='calories')
async def set_sex(call):
    await call.message.answer('Введите свой пол: м или ж', reply_markup=kb_2)
    await UserState.sex.set()
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def formula_info(call):
    await call.message.answer('Доработанный вариант формулы Миффлина-Сан Жеора, '
                              'в отличие от упрощенного дает более точную информацию '
                              'и учитывает степень физической активности человека: \n\n'
                              'для мужчин: \n(10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A; '
                              'для женщин: \n(10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A. \n\n'
                              'A – это уровень активности человека, его различают обычно по пяти степеням '
                              'физических нагрузок в сутки: \n\n'
                              'Минимальная активность: A = 1,2. \n'
                              'Слабая активность: A = 1,375. \n'
                              'Средняя активность: A = 1,55. \n'
                              'Высокая активность: A = 1,725. \n'
                              'Экстра-активность: A = 1,9 (под эту категорию обычно подпадают люди, '
                              'занимающиеся, например, тяжелой атлетикой, или другими силовыми видами спорта '
                              'с ежедневными тренировками, а также те, кто выполняет тяжелую физическую работу).')
    await call.answer()


@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    await state.update_data(sex=message.text)
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_height(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_daily_activity(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Ведите свою дневную активность по шкале от 1 до 5\n'
                         '1. Минимальная активность\n'
                         '2. Слабая активность\n'
                         '3. Средняя активность\n'
                         '4. Высокая активность\n'
                         '5. Экстра-активность (под эту категорию обычно подпадают люди,'
                         'занимающиеся, например, тяжелой атлетикой, или другими силовыми'
                         'видами спорта с ежедневными тренировками, а также те,'
                         'кто выполняет тяжелую физическую работу).')
    await UserState.daily_activity.set()


@dp.message_handler(state=UserState.daily_activity)
async def send_calories(message, state):
    await state.update_data(daily_activity=message.text)
    data = await state.get_data()
    sex_index = 5 if data['sex'] == 'м' else -151
    calories = round((10 * int(data['weight']) + 6.25 * int(data['height']) - 5 * int(data['age'])
                      + sex_index) * activity_data[int(data['daily_activity'])])
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
