import faker
import sqlite3
from random import randint, choice


def generate_fake_data(number_users, number_tasks):
    statuses = [('new',), ('in progress',), ('completed',)]
    users = []
    tasks = []

    fake_data = faker.Faker()

    for _ in range(number_users):
        users.append((fake_data.name(), fake_data.unique.email(domain=fake_data.domain_name())))

    for index in range(number_tasks):
        tasks.append((
            f'Task#{index}',
            choice([fake_data.text(max_nb_chars=100), None]),
            randint(1, len(statuses)),
            randint(1, number_users)
        ))

    return statuses, users, tasks


def insert_data_to_db(statuses, users, tasks):
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()

        sql_to_status = 'INSERT INTO status(name) VALUES (?)'
        cur.executemany(sql_to_status, statuses)

        sql_to_users = 'INSERT INTO users(fullname, email) VALUES (?,?)'
        cur.executemany(sql_to_users, users)

        sql_to_tasks = 'INSERT INTO tasks(title, description, status_id, user_id) VALUES (?,?,?,?)'
        cur.executemany(sql_to_tasks, tasks)

        con.commit()


if __name__ == '__main__':
    statuses, users, tasks = generate_fake_data(30, 100)
    insert_data_to_db(statuses, users, tasks)
