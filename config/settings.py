token_path = r"C:\Folders\tokens\token_telebook.txt"

with open(file=token_path, encoding='utf-8') as file:
    token = file.readlines()

SETTINGS = {
    "token": token[0].replace('\n', ''),
    "dbname": "telebookdb",
    "user": "postgres",
    "password": token[1].replace('\n', ''),
    "delete_table_password": token[2].replace('\n', '')
}

TABLES_NAME_DB_CONFIG = {
    'users': 'users',
    'version': 'version'
}

AUTHOR = 'yakummi | Ivan Gorobtsov'

START_MESSAGE = {
    'message': "Привет, это TeleBook!\nЯ помогу тебе найти подходящую книгу для прочтения на досуге!",
    'images': ['images/start_image.jpg']
}

CATALOG_MESSAGE = {
    'message': "Это каталог!"
}