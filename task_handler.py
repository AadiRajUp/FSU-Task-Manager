from flask import Flask, render_template,url_for,Blueprint,request,redirect,session
from models import *
from extensions import db,migrate
from connect import connectDB,DB_NAME,TASK_ID_TABLE
from app import app
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
        new_task = TASK_TABLE(task_name=taskTitle,task_assigned_to=individualName,task_assigned_by=session.get("username"),task_deadline=deadline,task_description=taskDescription)
        with app.app_context():
            db.create_all()
            db.session.add(new_task)
            db.session.commit()
        {
        """ conn = connectDB()
        if conn == -1:
            print("Error Connecting to the database")
            return render_template(url_for('form'))
        cur =conn.cursor()

        print("Uploading Data to the database")
        query1 = f"""
        #INSERT INTO {TASK_ID_TABLE} (`task_name`,`task_assigned_to`,`task_assigned_by`,`task_deadline`,`task_description`) VALUES("{taskTitle}","{individualName}","{session.get("username")}","{deadline}","{taskDescription}")
        """
        cur.execute(query1)
        conn.commit()
        output= cur.fetchall()
        print(output)
        cur.close()
        conn.close() """
        }
        return redirect(url_for('index'))
    
"""
tests= [ UID(username="Meyan",password="Meyan123",role="admin"),
    TASK_TABLE(task_name="Sample Task")]
with app.app_context():
    db.create_all()

    for item in tests:
        try:
            db.session.add(item)
            # db.session.add(t)
            db.session.commit()
        except Exception as e:  # if alreay add
            print (e)
            db.session.rollback()
            continue

"""
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
