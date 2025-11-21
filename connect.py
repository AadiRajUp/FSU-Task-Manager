import pymysql
import sqlite3

DB_NAME = "FSU_TASK_TRACKER_DB"
USER_ID_TABLE = "uid_table" 
TASK_ID_TABLE = "task_table"
ARCHIVE_TABLE = "task_archive"

def connectDB():
    conn = sqlite3.connect('database.sqlite')
    if conn:
        return conn
    else:
        return -1