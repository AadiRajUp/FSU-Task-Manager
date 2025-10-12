from flask import Blueprint,render_template,redirect,url_for,request
from connect import connectDB,TASK_ID_TABLE

edit_bp = Blueprint("edit",__name__)


@edit_bp.route("/edit",methods=["GET","POST"])
def edit():
    task_id = request.args.get('task_id')
    task_id_db= request.args.get('task_id_db')
    if request.method == "GET":
        return render_template('edit.html', task_id=task_id,task_id_db=task_id_db)
    
    if request.method == "POST":
        task_id_db = request.form["task_id_db"]
        print("------------------------------------------------------------------------")
        print(task_id_db)
        print("------------------------------------------------------------------------")
        percentageDone = request.form["PercentageDone"]
        progress = request.form["Progress"]
        remainingStuff = request.form["RemainingStuff"]
        peopleWorking = request.form["PeopleWorking"]
        conn = connectDB()
        cur = conn.cursor()
        query1 = f"""
        UPDATE {TASK_ID_TABLE}
        SET `task_progress`="{progress}",`task_remaining`="{remainingStuff}",`task_percentage`={percentageDone},`task_people_working`="{peopleWorking}"
        WHERE `task_id` = {task_id_db}
        """
        cur.execute(query1)
        conn.commit()
        output = cur.fetchall()
        print(output)
        return redirect(url_for('index'))
