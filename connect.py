import pymysql
DB_NAME = "FSU_TASK_TRACKER_DB"
USER_ID_TABLE = "UID_TABLE" 
TASK_ID_TABLE = "TASK_TABLE"
ARCHIVE_TABLE = "task_archive"

def connectDB():
    conn = pymysql.connect(host="localhost",user="root", password="",database=DB_NAME)
    if conn:
        return conn
    else:
        return -1