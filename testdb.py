import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM all_users').fetchall()

    def select_single(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT * FROM all_users WHERE id = ?', (user_id,)).fetchone()

    def find_user(self, username):
        with self.connection:
            user = self.cursor.execute('SELECT * FROM all_users WHERE username = ?', (username,)).fetchone()
            return user

    def count_users(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM all_users').fetchall()
            return len(result)

    def new_user(self, chat, username):
        with self.connection:
            index = len(self.cursor.execute('SELECT * FROM all_users').fetchall()) + 1
            self.cursor.execute(' INSERT INTO all_users(id, chat_id, username) VALUES(?,?,?) ', (index, chat, username))

    def close(self):
        self.connection.close()
