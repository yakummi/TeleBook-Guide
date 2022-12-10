import psycopg2
from config.settings import SETTINGS, TABLES_NAME_DB_CONFIG

class Database:
    conn = psycopg2.connect(database=SETTINGS["dbname"], user=SETTINGS['user'], password=SETTINGS["password"])

    def create_tables(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['users']} (
            id INT not null generated always as identity primary key,
            id_user BIGINT,
            first_name TEXT 
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['version']} (
            id INT not null generated always as identity primary key,   
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            version TEXT      
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['python']} (
            id INT not null generated always as identity primary key,   
            name TEXT,
            image TEXT,
            description TEXT 
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['javascript']} (
            id INT not null generated always as identity primary key,   
            name TEXT,
            image TEXT,
            description TEXT 
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['java']} (
            id INT not null generated always as identity primary key,   
            name TEXT,
            image TEXT,
            description TEXT 
            )
            """)
            self.conn.commit()


            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['c_plus2']} (
            id INT not null generated always as identity primary key,   
            name TEXT,
            image TEXT,
            description TEXT 
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['all_users_favourites_books_python']} (
            id INT not null generated always as identity primary key,   
            id_user INT references {TABLES_NAME_DB_CONFIG['users']} (id) on delete set null,
            id_book INT references {TABLES_NAME_DB_CONFIG['python']} (id) on delete set null
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['all_users_favourites_books_c_plus2']} (
            id INT not null generated always as identity primary key,   
            id_user INT references {TABLES_NAME_DB_CONFIG['users']} (id) on delete set null,
            id_book INT references {TABLES_NAME_DB_CONFIG['c_plus2']} (id) on delete set null
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['all_users_favourites_books_javascript']} (
            id INT not null generated always as identity primary key,   
            id_user INT references {TABLES_NAME_DB_CONFIG['users']} (id) on delete set null,
            id_book INT references {TABLES_NAME_DB_CONFIG['javascript']} (id) on delete set null
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['all_users_favourites_books_java']} (
            id INT not null generated always as identity primary key,   
            id_user INT references {TABLES_NAME_DB_CONFIG['users']} (id) on delete set null,
            id_book INT references {TABLES_NAME_DB_CONFIG['java']} (id) on delete set null
            )
            """)
            self.conn.commit()


    def delete_tables(self):
        password = input("Введите пароль для удаления таблиц из базы: ")
        if password == SETTINGS['delete_table_password']:
            with self.conn.cursor() as cur:
                cur.execute(f"""
                DROP TABLE {TABLES_NAME_DB_CONFIG['users']} CASCADE;
                """)
                self.conn.commit()
        else:
            return "Пароль валидный!"

    def add_user(self, id_user, first_name):
        with self.conn.cursor() as cur:
            cur.execute(f'''
            INSERT INTO {TABLES_NAME_DB_CONFIG['users']} (id_user, first_name)
            VALUES (
            {id_user}, {repr(first_name)}
            );
            
            ''')
            self.conn.commit()

    def correct_user(self, id_user, first_name):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT id_user
            FROM {TABLES_NAME_DB_CONFIG['users']}
            WHERE id_user = {id_user}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            if result == []:
                self.add_user(id_user, first_name)
                self.conn.commit()

    def version_add(self):
        with self.conn.cursor() as cur:
            version = input("Версия: ")
            cur.execute(f'''
            INSERT INTO {TABLES_NAME_DB_CONFIG['version']}(version)
            VALUES(
            {repr(version)}
            );
            ''')
            self.conn.commit()

    def version_get(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT version
            FROM {TABLES_NAME_DB_CONFIG['version']}
            ORDER BY id
            DESC LIMIT 1
            """

            cur.execute(select_request)
            version_project = cur.fetchall()

            return version_project[0][0]



DATABASE = Database()
DATABASE.create_tables()