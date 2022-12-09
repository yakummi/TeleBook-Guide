from aiogram import Dispatcher, Bot, executor, types
from config.settings import SETTINGS, START_MESSAGE, CATALOG_MESSAGE
from database.database import DATABASE
from aiogram.types import InputFile
from buttons import urlkb, urlkb_catalog, urlkb_catalog_it

bot = Bot(token=SETTINGS['token'])

dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    DATABASE.correct_user(id_user=user_id, first_name=name)
    photo = InputFile(START_MESSAGE['images'][0])
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(START_MESSAGE['message'], reply_markup=urlkb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    help_str = """
/start - начать общение
/help - вывести список всех команд
    """
    await message.answer(help_str)


@dp.callback_query_handler(text="catalog")
async def catalog_command(call: types.CallbackQuery):
    await call.message.answer(CATALOG_MESSAGE['message'], reply_markup=urlkb_catalog)

@dp.callback_query_handler(text="exit")
async def exit_command_from_catalog(call: types.CallbackQuery):
    photo = InputFile(START_MESSAGE['images'][0])
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    await call.message.answer(START_MESSAGE['message'], reply_markup=urlkb)


@dp.callback_query_handler(text="it_catalog")
async def it_catalog_command(call: types.CallbackQuery):
    await call.message.answer("Не забыть картинку", reply_markup=urlkb_catalog_it)

@dp.callback_query_handler(text="exit_it")
async def it_catalog_command(call: types.CallbackQuery):
    await call.message.answer(CATALOG_MESSAGE['message'], reply_markup=urlkb_catalog)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
