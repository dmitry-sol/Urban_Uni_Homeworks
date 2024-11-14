from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
activity_data = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()
    daily_activity = State()

@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.\n'
                         'Введите calories, чтобы посчитать свои калории')


@dp.message_handler(text='calories')
async def set_sex(message):
    await message.answer('Введите свой пол: м или ж')
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    await state.update_data(sex=message.text)
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
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
    calories = round((10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
                      + sex_index) * activity_data[int(data['daily_activity'])])
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
