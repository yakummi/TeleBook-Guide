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
    'users': 'users'
}

AUTHOR = 'yakummi | Ivan Gorobtsov'
