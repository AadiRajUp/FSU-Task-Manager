import pymysql
DB_NAME = "FSU_TASK_TRACKER_DB"
USER_ID_TABLE = "uid_table" 
TASK_ID_TABLE = "TASK_TABLE"

def connectDB():
    conn = pymysql.connect(host="localhost",user="root", password="",database=DB_NAME)
    if conn:
        return conn
    else:
        return -1