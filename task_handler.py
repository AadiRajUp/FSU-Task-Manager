from flask import Flask, render_template,url_for,Blueprint,request,redirect
import pymysql
from connect import connectDB
task_bp = Blueprint('taskHandler',__name__)

@task_bp.route('/postTask',methods=['POST'])
def postTask():
    taskTitle = request.form["taskTitle"]
    individualName = request.form["individualName"]
    taskDescription = request.form["taskDescription"]
    deadline= request.form["deadline"]
    conn = connectDB()
    if conn == -1:
        print("Error Connecting to the database")
        return render_template(url_for('form'))
    cur =conn.cursor()

    print("Uploading Data to the database")
    query1 = f"""
    INSERT INTO task_table (`task_name`,`task_assigned_to`,`task_assigned_by`,`task_deadline`,`task_description`) VALUES("{taskTitle}","{individualName}","Admin","{deadline}","{taskDescription}")
    """
    cur.execute(query1)
    conn.commit()
    output= cur.fetchall()
    print(output)
    cur.close()
    conn.close()
    return redirect(url_for('index'))
