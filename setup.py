from connect import connectDB, DB_NAME, USER_ID_TABLE, TASK_ID_TABLE, ARCHIVE_TABLE

def letThereBeLight():
    conn = connectDB()
    cur = conn.cursor()

    sql_script = """
    -- Create table: task_archive
    CREATE TABLE IF NOT EXISTS task_archive (
        task_id INTEGER PRIMARY KEY,
        task_name TEXT NOT NULL,
        task_assigned_to TEXT NOT NULL,
        task_assigned_by TEXT NOT NULL,
        task_description TEXT NOT NULL
    );

    INSERT INTO task_archive (task_id, task_name, task_assigned_to, task_assigned_by, task_description) VALUES
    (16, 'dfs', 'Albert', 'Aadi', 'erwerwr');

    -- Create table: task_table
    CREATE TABLE IF NOT EXISTS task_table (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        task_assigned_to TEXT NOT NULL,
        task_assigned_by TEXT NOT NULL,
        task_deadline TEXT NOT NULL,
        task_description TEXT NOT NULL,
        task_progress TEXT,
        task_remaining TEXT,
        task_percentage INTEGER,
        task_people_working TEXT
    );

    INSERT INTO task_table (task_id, task_name, task_assigned_to, task_assigned_by, task_deadline, task_description, task_progress, task_remaining, task_percentage, task_people_working) VALUES
        (18, 'naya task', 'meyan', 'Aadi', '2025-10-15 00:00:00', 'gdfdg', 's', 'fds', 90, ''),
        (19, 'Aadi lai Aarako', 'Web', 'Swoyam', '2442-03-04 00:00:00', 'asdada', 'fdfdgg', 'sfgdf', 75, 'dsgfds'),
        (20, 'naya task2', 'Albert', 'Aadi', '2025-10-15 00:00:00', 'fgdgfd', NULL, NULL, NULL, NULL),
        (21, 'dfssasda', '5432dafd', 'fsdfs', '2025-10-15 16:21:52', 'sadfsdfsd', 'dasdadas', 'sdad', 45, 'fdsfsfs'),
        (22, 'dfs', 'Albert', 'Aadi', '2422-03-04 00:00:00', 'dfdhd', NULL, NULL, NULL, NULL);

    -- Create table: uid_table
    CREATE TABLE IF NOT EXISTS uid_table (
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        userclass TEXT NOT NULL DEFAULT 'user'
    );

    INSERT INTO uid_table (uid, username, password, userclass) VALUES
        (1, 'Aadi', 'pwdpass', 'Admin'),
        (2, 'meyan', '1', 'auto'),
        (3, 'Swoyam', 'swoyam123', 'Admin');

    """

    cur.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    letThereBeLight()
