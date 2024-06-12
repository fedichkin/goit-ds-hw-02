-- Table: users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Table: status
DROP TABLE IF EXISTS status;
CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Table: tasks
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_tasks_status_id FOREIGN KEY(status_id) REFERENCES status(id)
        ON DELETE SET NULL,
    CONSTRAINT fk_tasks_user_id FOREIGN KEY(user_id) REFERENCES users(id)
        ON DELETE CASCADE
);
