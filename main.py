from aiogram import Dispatcher, Bot, executor, types
from config.settings import SETTINGS, START_MESSAGE, CATALOG_MESSAGE, TABLES_NAME_DB_CONFIG, IT_CATALOG
from database.database import DATABASE
from aiogram.types import InputFile
import psycopg2
from buttons import urlkb, urlkb_catalog, urlkb_catalog_it, urlkb_catalog_javascript, urlkb_catalog_python, urlkb_catalog_java, urlkb_favourite
import random
from aiogram.utils.markdown import hide_link
import requests

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
    photo = InputFile(IT_CATALOG['images'][0])
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    await call.message.answer(IT_CATALOG['message'], reply_markup=urlkb_catalog_it)


@dp.callback_query_handler(text="exit_it")
async def it_catalog_command(call: types.CallbackQuery):
    photo = InputFile(IT_CATALOG['images'][0])
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    await call.message.answer(IT_CATALOG['message'], reply_markup=urlkb_catalog_it)


@dp.callback_query_handler(text="exit_python")
async def it_catalog_command(call: types.CallbackQuery):
    photo = InputFile(IT_CATALOG['images'][0])
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    await call.message.answer(IT_CATALOG['message'], reply_markup=urlkb_catalog_it)


@dp.callback_query_handler(text="exit_java")
async def it_catalog_command(call: types.CallbackQuery):
    photo = InputFile(IT_CATALOG['images'][0])
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    await call.message.answer(IT_CATALOG['message'], reply_markup=urlkb_catalog_it)


@dp.callback_query_handler(text="exit_javascript")
async def it_catalog_command(call: types.CallbackQuery):
    photo = InputFile(IT_CATALOG['images'][0])
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    await call.message.answer(IT_CATALOG['message'], reply_markup=urlkb_catalog_it)


@dp.callback_query_handler(text=["python", "next_book_python", 'add_favourite'])
async def next_python(call: types.CallbackQuery):
    number = random.randint(1, DATABASE.count_strings_python()[0][0])
    info = DATABASE.select_python_id(number)
    if call.data == 'add_favourite':
        user_id = call.from_user.id
        DATABASE.get_id_user(user_id, info[0][0], info[0][1])
    else:
        await call.message.answer(f"{info[0][0]}{hide_link(info[0][1])}", parse_mode='HTML', reply_markup=urlkb_catalog_python)



@dp.callback_query_handler(text=["java", "next_book_java", 'add_favourite'])
async def next_java(call: types.CallbackQuery):
    number = random.randint(1, DATABASE.count_strings_java()[0][0])
    info = DATABASE.select_java_id(number)
    if call.data == 'add_favourite':
        user_id = call.from_user.id
        DATABASE.get_id_user(user_id, info[0][0], info[0][1])
    else:
        await call.message.answer(f"{info[0][0]}{hide_link(info[0][1])}", parse_mode='HTML', reply_markup=urlkb_catalog_java)

@dp.callback_query_handler(text=["javascript", "next_book_javascript", "add_favourites"])
async def next_javascript(call: types.CallbackQuery):
    number = random.randint(1, DATABASE.count_strings_javascript()[0][0])
    info = DATABASE.select_javascript_id(number)
    if call.data == 'add_favourite':
        user_id = call.from_user.id
        DATABASE.get_id_user(user_id, info[0][0], info[0][1])
    else:
        await call.message.answer(f"{info[0][0]}{hide_link(info[0][1])}", parse_mode='HTML', reply_markup=urlkb_catalog_javascript)

@dp.callback_query_handler(text=['favourites', "delete_favourite"])
async def get_all_favourites_books_from_user(call: types.CallbackQuery):
    conn = psycopg2.connect(database=SETTINGS["dbname"], user=SETTINGS['user'], password=SETTINGS["password"])
    user_id = call.from_user.id
    with conn.cursor() as cur:
        select_request = f"""
        SELECT id
        FROM {TABLES_NAME_DB_CONFIG['users']}
        WHERE id_user = {user_id}
        """

        cur.execute(select_request)
        result_id = cur.fetchall()

        select_request2 = f"""
        SELECT name, image
        FROM {TABLES_NAME_DB_CONFIG['all_users_favourites_books']}
        WHERE id_user = {result_id[0][0]}
        """

        cur.execute(select_request2)
        books = cur.fetchall()

        if call.data == "delete_favourite":
            print("q")
            cal = call.message.text


        else:

            print(books)

            for book in books:
                await call.message.answer(f"{book[0]}{hide_link(book[1])}", parse_mode='HTML', reply_markup=urlkb_favourite)

            photo = InputFile(START_MESSAGE['images'][0])
            await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
            await call.message.answer(START_MESSAGE['message'], reply_markup=urlkb)

        cur.close()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
