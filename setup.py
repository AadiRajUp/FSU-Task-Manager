import pymysql

DB_NAME = "FSU_TASK_TRACKER_DB"
USER_ID_TABLE = "UID_TABLE" 
TASK_ID_TABLE = "TASK_TABLE"
def connectServer():
    conn = pymysql.connect(host="localhost",user="root",password="")
    cur = conn.cursor()



    print("Database Creation......")
    query1 = f"""
    CREATE DATABASE {DB_NAME} 
    """
    cur.execute(query1)
    output = cur.fetchall()
    print(output)

    # Going into the database
    print("Going into the Database......")
    query1 = f"""
    USE {DB_NAME}
    """
    cur.execute(query1)
    output = cur.fetchall()
    print(output)


    # User Data Holder
    print("User Table Creation.....")
    query1 = f"""
    CREATE TABLE {USER_ID_TABLE} (
    uid INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    userclass VARCHAR(10) NOT NULL 
    )
    """ 
    # Hopefully hash bhara aauxa pwd
    cur.execute(query1)
    output = cur.fetchall()
    print(output)

    # Task Data Table
    print("Creating the task data table")

    query1 = f"""
    CREATE TABLE {TASK_ID_TABLE}(
    task_id INT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    task_assigned_to VARCHAR(255) NOT NULL,
    task_assigned_by VARCHAR(255) NOT NULL,
    task_deadline DATETIME NOT NULL,
    task_description TEXT NOT NULL,
    task_progress TEXT,
    task_remaining TEXT,
    task_percentage TINYINT UNSIGNED)
    """
    cur.execute(query1)
    output = cur.fetchall()
    print(output)


    conn.close()

if __name__=="__main__":
    connectServer()