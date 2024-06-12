import sqlite3


def execute_query(sql, params=[]):
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(sql, params)

        return cur.fetchall()


def get_tasks_by_user_id(user_id):
    sql = '''
    SELECT title, description, s.name as status FROM tasks as t
    join status s on s.id = t.status_id
    WHERE t.user_id = ?
    '''

    return execute_query(sql, [str(user_id)])


def get_tasks_by_status(status):
    sql = '''
    SELECT title, description FROM tasks as t
    join status s on s.id = t.status_id
    WHERE s.name = ?
    '''

    return execute_query(sql, [status])


def update_status_of_task(task_id, new_status):
    sql = '''
        UPDATE tasks as t
        SET status_id = (SELECT s.id FROM status as s WHERE s.name = ?)
        WHERE t.id = ?
        '''

    return execute_query(sql, [new_status, str(task_id)])


def add_task(user_id, title, description):
    sql = '''
        INSERT INTO tasks(title, description, status_id, user_id)
        VALUES(?, ?, 1, ?)
        '''

    return execute_query(sql, [title, description, user_id])


def list_users_without_tasks():
    sql = '''
        SELECT u.fullname, u.email FROM users as u 
        WHERE u.id NOT IN (SELECT t.user_id FROM tasks as t)
        '''

    return execute_query(sql)


def get_tasks_is_not_finished():
    sql = '''
        SELECT t.title, t.description FROM tasks t
        where t.status_id IS NOT 3
        '''

    return execute_query(sql)


def delete_task(task_id):
    sql = '''
        DELETE FROM tasks 
        where id = ?
        '''

    return execute_query(sql, [task_id])


def search_users_by_email(email):
    sql = '''
        SELECT u.fullname, u.email FROM users u 
        WHERE u.email LIKE ?
        '''

    return execute_query(sql, [f'%{email}%'])


def update_name_of_user(user_id, new_name):
    sql = '''
        UPDATE users 
        SET fullname = ? 
        WHERE id = ?
    '''

    return execute_query(sql, [new_name, user_id])


def get_count_task_by_each_status():
    sql = '''
        SELECT s.name as status, COUNT(t.id) as count_task FROM tasks as t
        JOIN status as s ON s.id = t.status_id 
        GROUP BY t.status_id 
        '''

    return execute_query(sql)


def get_tasks_by_user_email_domain(domain):
    sql = '''
        SELECT title, description, s.name as status FROM tasks as t
        JOIN status s on s.id = t.status_id
        JOIN users u on u.id = t.user_id 
        WHERE u.email LIKE ?
        '''

    return execute_query(sql, [f'%@{domain}'])


def get_tasks_without_description():
    sql = '''
        SELECT t.title FROM tasks t
        WHERE t.description ISNULL 
        '''

    return execute_query(sql)


def get_tasks_in_progress_with_users():
    sql = '''
        SELECT u.fullname, t.title, t.description FROM users u
        JOIN tasks t ON t.user_id = u.id 
        JOIN status s ON s.id = t.status_id AND s.name = 'in progress'
        '''

    return execute_query(sql)


def get_count_tasks_by_each_user():
    sql = '''
        SELECT u.fullname as user, COUNT(t.id) as count_task FROM users as u
        LEFT JOIN tasks t ON t.user_id = u.id
        GROUP BY u.id 
        '''

    return execute_query(sql)


if __name__ == '__main__':
    print(get_tasks_by_user_id(7))
    print(get_tasks_by_status('new'))
    update_status_of_task(1, 'completed')
    print(list_users_without_tasks())
    add_task(1, 'New Task', 'Bla-bla-bla')
    print(get_tasks_is_not_finished())
    delete_task(99)
    print(search_users_by_email('wil'))
    update_name_of_user(10, 'Black Subbath')
    print(get_count_task_by_each_status())
    print(get_tasks_by_user_email_domain('james.com'))
    print(get_tasks_without_description())
    print(get_tasks_in_progress_with_users())
    print(get_count_tasks_by_each_user())
