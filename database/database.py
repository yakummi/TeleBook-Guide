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
            price TEXT
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['javascript']} (
            id INT not null generated always as identity primary key,   
            name TEXT,
            image TEXT,
            price TEXT
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['java']} (
            id INT not null generated always as identity primary key,   
            name TEXT,
            image TEXT,
            price TEXT
            )
            """)
            self.conn.commit()

            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLES_NAME_DB_CONFIG['all_users_favourites_books']} (
            id INT not null generated always as identity primary key,   
            id_user INT references {TABLES_NAME_DB_CONFIG['users']} (id) on delete set null,
            name TEXT,
            image TEXT,
            price TEXT
            )
            """)
            self.conn.commit()


    def delete_tables(self):
        password = input("?????????????? ???????????? ?????? ???????????????? ???????????? ???? ????????: ")
        if password == SETTINGS['delete_table_password']:
            with self.conn.cursor() as cur:
                cur.execute(f"""
                DROP TABLE {TABLES_NAME_DB_CONFIG['users']} CASCADE;
                """)
                self.conn.commit()
        else:
            return "???????????? ????????????????!"

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
            version = input("????????????: ")
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

    def insert_python(self, name, image, price):
        with self.conn.cursor() as cur:
            cur.execute(f"""
            INSERT INTO {TABLES_NAME_DB_CONFIG['python']} (name, image, price)
            VALUES ({(name)}, {(image)}, {(price)});
            """)

            self.conn.commit()

    def insert_java(self, name, image, price):
        with self.conn.cursor() as cur:
            cur.execute(f"""
            INSERT INTO {TABLES_NAME_DB_CONFIG['java']} (name, image, price)
            VALUES ({(name)}, {(image)}, {(price)});
            """)

            self.conn.commit()

    def insert_javascript(self, name, image, price):
        with self.conn.cursor() as cur:
            cur.execute(f"""
            INSERT INTO {TABLES_NAME_DB_CONFIG['javascript']} (name, image, price)
            VALUES ({(name)}, {(image)}, {(price)});
            """)

            self.conn.commit()

    def select_python(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT name, image, price
            FROM {TABLES_NAME_DB_CONFIG['python']}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result

    def select_javascript(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT name, image, price
            FROM {TABLES_NAME_DB_CONFIG['javascript']}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result
    
    def select_java(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT name, image, price
            FROM {TABLES_NAME_DB_CONFIG['java']}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result

    def check_parser_python(self, name, image, price):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT *
            FROM {TABLES_NAME_DB_CONFIG['python']}
            WHERE name = {name}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            if result == []:
                self.insert_python(name=name, image=image, price=price)
                self.conn.commit()

    def check_parser_javascript(self, name, image, price):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT *
            FROM {TABLES_NAME_DB_CONFIG['javascript']}
            WHERE name = {name}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            if result == []:
                self.insert_javascript(name=name, image=image, price=price)
                self.conn.commit()

    def check_parser_java(self, name, image, price):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT *
            FROM {TABLES_NAME_DB_CONFIG['java']}
            WHERE name = {name}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            if result == []:
                self.insert_java(name=name, image=image, price=price)
                self.conn.commit()

    def count_strings_python(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT COUNT(name)
            FROM {TABLES_NAME_DB_CONFIG['python']}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result

    def count_strings_java(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT COUNT(name)
            FROM {TABLES_NAME_DB_CONFIG['java']}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result

    def count_strings_javascript(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT COUNT(name)
            FROM {TABLES_NAME_DB_CONFIG['javascript']}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result

    def select_python_id(self, id):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT name, image, price
            FROM {TABLES_NAME_DB_CONFIG['python']}
            WHERE id = {id}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result

    def select_javascript_id(self, id):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT name, image, price
            FROM {TABLES_NAME_DB_CONFIG['javascript']}
            WHERE id = {id}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result

    def select_java_id(self, id):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT name, image, price
            FROM {TABLES_NAME_DB_CONFIG['java']}
            WHERE id = {id}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            return result


    def add_favourite_books_id(self, id_user, name, image, price):
        with self.conn.cursor() as cur:
            cur.execute(f"""
            INSERT INTO {TABLES_NAME_DB_CONFIG['all_users_favourites_books']} (id_user, name, image, price)
            VALUES ({(id_user)}, {(repr(name))}, {repr(image)}, {repr(price)});
            """)

            self.conn.commit()


    def check_favourite_books_id(self, id_user, name, image, price):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT *
            FROM {TABLES_NAME_DB_CONFIG['all_users_favourites_books']}
            WHERE name = {repr(name)} AND id_user = {id_user}
            """

            cur.execute(select_request)
            result = cur.fetchall()

            if result == []:
                self.add_favourite_books_id(id_user=id_user, name=name, image=image, price=price)
                self.conn.commit()


    def get_id_user(self, id_user, name, image, price):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT id
            FROM {TABLES_NAME_DB_CONFIG['users']}
            WHERE id_user = {id_user}
            """

            cur.execute(select_request)
            result = cur.fetchall()
            self.check_favourite_books_id(result[0][0], name, image, price)

    def delete_favourites_books(self, id_user, name, price): # ????????????????
        with self.conn.cursor() as cur:
            cur.execute(f"""
            DELETE FROM {TABLES_NAME_DB_CONFIG['all_users_favourites_books']}
            WHERE id_user = {id_user} AND name = {repr(name)};
            """)

            self.conn.commit()


    def get_id_user_for_delete_favourites_books(self, id_user, name, price):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT id
            FROM {TABLES_NAME_DB_CONFIG['users']}
            WHERE id_user = {id_user}
            """

            cur.execute(select_request)
            result = cur.fetchall()
            self.delete_favourites_books(id_user=result[0][0], name=name, price=price)

    def get_all_users_book(self, name):
        with self.conn.cursor() as cur:
            select_request = f"""
                        SELECT name
                        FROM {TABLES_NAME_DB_CONFIG['all_users_favourites_books']}
                        WHERE name = {name}
                        """

            cur.execute(select_request)
            result = cur.fetchall()
            if result == []:
                return 0
            return len(result[0])

    def get_all_top_books(self):
        with self.conn.cursor() as cur:
            select_request = f"""
            SELECT name
            FROM {TABLES_NAME_DB_CONFIG['all_users_favourites_books']}
            ORDER BY name
            LIMIT 5
            """

            cur.execute(select_request)
            result = cur.fetchall()
            return result

DATABASE = Database()
DATABASE.create_tables()
