from flask import session
from flask import Blueprint
from connect import connectDB
from connect import DB_NAME,TASK_ID_TABLE, USER_ID_TABLE
def fetchAll(taskType,sortBy):
    if taskType == None:
        taskType="all"
    if sortBy == None:
        sortBy="task_deadline"
    print(taskType)
    print(sortBy)
    conn = connectDB()
    cur = conn.cursor()
    query1= f"""
    SELECT * FROM {TASK_ID_TABLE}
    
    """
    if taskType !="all":
        query1 += f"""
        WHERE `{taskType}`= "{session.get("username")}"
        """
    if sortBy !="default":
        query1+=f"ORDER BY `{sortBy}` DESC"
    cur.execute(query1)
    output = cur.fetchall()
    return output
