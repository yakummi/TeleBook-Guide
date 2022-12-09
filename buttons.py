from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Start Command

urlkb = InlineKeyboardMarkup(row_width=2)
urlbutton1 = InlineKeyboardButton(text="Каталог", callback_data="catalog")
urlbutton2 = InlineKeyboardButton(text="Избранные", callback_data="favourites")
urlkb.add(urlbutton1, urlbutton2)

# -----------------------------------------

# Catalog Command

