from aiogram import Dispatcher, Bot, executor, types
from config.settings import SETTINGS
from database.database import DATABASE
from aiogram.types import InputFile
from buttons import urlkb

bot = Bot(token=SETTINGS['token'])

dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    DATABASE.correct_user(id_user=user_id, first_name=name)
    photo = InputFile("images/start_image.jpg")
    await message.answer("Привет!", reply_markup=urlkb)
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    help_str = """
/start - начать общение
/help - вывести список всех команд
    """
    await message.answer(help_str)


@dp.callback_query_handler(text="catalog")
async def catalog_command(call: types.CallbackQuery):
    await call.message.answer("Это каталог")


# @dp.message_handler()
# async def main_process(message: types.Message):
#     if message.text == '/book':
#         await message.answer("Часть про книжки")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
