import pymysql
DB_NAME = "FSU_TASK_TRACKER_DB"
USER_ID_TABLE = "uid_table" 
TASK_ID_TABLE = "task_table"
ARCHIVE_TABLE = "task_archive"
import sqlite3
def connectDB():
    conn = sqlite3.connect('database.sqlite')
    if conn:
        return conn
    else:
        return -1