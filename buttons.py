from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Start Command

urlkb = InlineKeyboardMarkup(row_width=2)
urlbutton1 = InlineKeyboardButton(text="Каталог", callback_data="catalog")
urlbutton2 = InlineKeyboardButton(text="Избранные", callback_data="favourites")
urlkb.add(urlbutton1, urlbutton2)

# -----------------------------------------

# Catalog Command

urlkb_catalog = InlineKeyboardMarkup(row_width=2)
urlbutton1_catalog = InlineKeyboardButton(text="IT", callback_data="it_catalog")
urlbutton2_catalog = InlineKeyboardButton(text="Design", callback_data="design_catalog")
urlbutton3_catalog = InlineKeyboardButton(text="Вернуться", callback_data="exit")
urlkb_catalog.add(urlbutton1_catalog, urlbutton2_catalog, urlbutton3_catalog)

# ------------------------------------------

# IT Catalog Command

urlkb_catalog_it = InlineKeyboardMarkup(row_width=2)
urlbutton1_catalog_it = InlineKeyboardButton(text="Python", callback_data="python")
urlbutton2_catalog_it = InlineKeyboardButton(text="Java", callback_data="java")
urlbutton3_catalog_it = InlineKeyboardButton(text="C++", callback_data="c++")
urlbutton4_catalog_it = InlineKeyboardButton(text="JavaScript", callback_data="javascript")
urlbutton5_catalog_it = InlineKeyboardButton(text="Вернуться", callback_data="exit_it")
urlkb_catalog_it.add(urlbutton1_catalog_it, urlbutton2_catalog_it, urlbutton3_catalog_it, urlbutton4_catalog_it, urlbutton5_catalog_it)