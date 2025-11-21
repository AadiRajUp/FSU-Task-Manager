import pymysql
from connect import connectDB,DB_NAME,USER_ID_TABLE,TASK_ID_TABLE,ARCHIVE_TABLE

def letThereBeLight():
    conn = connectDB()
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
    task_percentage TINYINT UNSIGNED,
    task_people_working varchar(255)
    )
    """
    cur.execute(query1)
    output = cur.fetchall()
    print(output)
    # Archive Table
    print("Creating the Archive table")

    query1 = f"""
    CREATE TABLE {ARCHIVE_TABLE}(
	task_id INT PRIMARY KEY NOT NULL,
	task_name varchar(255) NOT NULL,
	task_assigned_to varchar(255) NOT NULL,
    task_assigned_by varchar(255) NOT NULL,
    task_description TEXT NOT NULL
    )
    """
    cur.execute(query1)
    output = cur.fetchall()
    print(output)

    conn.close()

if __name__=="__main__":
    letThereBeLight()