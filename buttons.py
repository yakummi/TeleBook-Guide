from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Start Command

urlkb = InlineKeyboardMarkup(row_width=2)
urlbutton1 = InlineKeyboardButton(text="Каталог", callback_data="catalog")
urlbutton2 = InlineKeyboardButton(text="Избранные", callback_data="favourites")
urlkb.add(urlbutton1, urlbutton2)

# -----------------------------------------

# Catalog Command

urlkb_catalog = InlineKeyboardMarkup(row_width=1)
urlbutton1_catalog = InlineKeyboardButton(text="IT", callback_data="it_catalog")
urlbutton2_catalog = InlineKeyboardButton(text="Вернуться", callback_data="exit")
urlkb_catalog.add(urlbutton1_catalog, urlbutton2_catalog)

# ------------------------------------------

# IT Catalog Command

urlkb_catalog_it = InlineKeyboardMarkup(row_width=2)
urlbutton1_catalog_it = InlineKeyboardButton(text="Python", callback_data="python")
urlbutton2_catalog_it = InlineKeyboardButton(text="Java", callback_data="java")
urlbutton3_catalog_it = InlineKeyboardButton(text="JavaScript", callback_data="javascript")
urlbutton4_catalog_it = InlineKeyboardButton(text="Вернуться", callback_data="exit_it")
urlkb_catalog_it.add(urlbutton1_catalog_it, urlbutton2_catalog_it, urlbutton3_catalog_it)
urlkb_catalog_it.add(urlbutton4_catalog_it)

# Python Command

urlkb_catalog_python = InlineKeyboardMarkup(row_width=2)
urlbutton1_catalog_python = InlineKeyboardButton(text="В избранные", callback_data="add_favourite")
urlbutton2_catalog_python = InlineKeyboardButton(text="Следующий", callback_data="next_book_python")
urlbutton3_catalog_python = InlineKeyboardButton(text="Вернуться", callback_data="exit_python")
urlkb_catalog_python.add(urlbutton1_catalog_python, urlbutton2_catalog_python, urlbutton3_catalog_python)


# -----------------------------------------------------------


# JavaScript Command

urlkb_catalog_javascript = InlineKeyboardMarkup(row_width=2)
urlbutton1_catalog_javascript = InlineKeyboardButton(text="В избранные", callback_data="add_favourite")
urlbutton2_catalog_javascript = InlineKeyboardButton(text="Следующий", callback_data="next_book_javascript")
urlbutton3_catalog_javascript = InlineKeyboardButton(text="Вернуться", callback_data="exit_javascript")
urlkb_catalog_javascript.add(urlbutton1_catalog_javascript, urlbutton2_catalog_javascript, urlbutton3_catalog_javascript)


# ------------------------------------------------------------


# Java Command

urlkb_catalog_java = InlineKeyboardMarkup(row_width=2)
urlbutton1_catalog_java = InlineKeyboardButton(text="В избранные", callback_data="add_favourite")
urlbutton2_catalog_java = InlineKeyboardButton(text="Следующий", callback_data="next_book_java")
urlbutton3_catalog_java = InlineKeyboardButton(text="Вернуться", callback_data="exit_java")
urlkb_catalog_java.add(urlbutton1_catalog_java, urlbutton2_catalog_java, urlbutton3_catalog_java)


# -----------------------------------------------------------