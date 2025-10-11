from flask import Flask, render_template,url_for,Blueprint,request,redirect,session
import pymysql
from connect import connectDB,DB_NAME,TASK_ID_TABLE
task_bp = Blueprint('taskHandler',__name__)

@task_bp.route('/postTask',methods=['GET','POST'])
def postTask():
    if request.method == "GET":
        return render_template('form.html')
    if request.method == "POST":
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
        INSERT INTO {TASK_ID_TABLE} (`task_name`,`task_assigned_to`,`task_assigned_by`,`task_deadline`,`task_description`) VALUES("{taskTitle}","{individualName}","{session.get("username")}","{deadline}","{taskDescription}")
        """
        cur.execute(query1)
        conn.commit()
        output= cur.fetchall()
        print(output)
        cur.close()
        conn.close()
        return redirect(url_for('index'))
@task_bp.route("/deleteTask")
def deleteTask():
    task_id_db= request.args.get('task_id_db')
    conn= connectDB()
    cur= conn.cursor()
    query1= f"""
    DELETE FROM {TASK_ID_TABLE}
    WHERE task_id = {task_id_db}
    """
    cur.execute(query1)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("index"))