from flask import render_template
from flask import Blueprint
from connect import connectDB
from connect import DB_NAME,TASK_ID_TABLE, USER_ID_TABLE
def fetchAll():
    conn = connectDB()
    cur = conn.cursor()
    query1= f"""
    SELECT * FROM {TASK_ID_TABLE}
    """
    cur.execute(query1)
    output = cur.fetchall()
    return output
