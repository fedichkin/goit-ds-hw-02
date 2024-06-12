import sqlite3


def create_db():
    with open('./structure_db.sql', 'r') as sqlf:
        sql = sqlf.read()

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == '__main__':
    create_db()
