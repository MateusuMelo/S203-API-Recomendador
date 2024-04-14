import sqlite3


class Database:
    def __init__(self):
        self.db_path = "db.sqlite3"

    def query(self, query):
        connect = sqlite3.connect(self.db_path)
        try:
            cur = connect.cursor()
            result = cur.execute(query)
            return result.fetchall()
        except Exception as e:
            return print(e)
        finally:
            connect.close()


data = Database().query("test")
