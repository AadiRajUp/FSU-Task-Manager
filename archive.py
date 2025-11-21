from flask import Blueprint,request,redirect,url_for,session
from connect import connectDB,TASK_ID_TABLE,ARCHIVE_TABLE

archive_bp = Blueprint("archive",__name__)


@archive_bp.route("/archiveTask")
def archiveTask():
    task_id_db= request.args.get('task_id_db')

       # get the task assigned to from the db
    query = f'''
        SELECT * FROM {TASK_ID_TABLE}
        WHERE `task_id` = {task_id_db}
        '''
    
    conn = connectDB()
    cur = conn.cursor()
    cur.execute(query)
    output = cur.fetchall()

    if output[0][3] != session["username"]:
            return "You are not authorized to edit this task."

    conn = connectDB()
    cur = conn.cursor()

    query1 = f"""
    SELECT * FROM {TASK_ID_TABLE}
    WHERE `task_id` = {task_id_db}
    """
    cur.execute(query1)
    output = cur.fetchall()
    query1 = f"""
    DELETE FROM {TASK_ID_TABLE}
    WHERE `task_id`= {task_id_db}
    """
    cur.execute(query1)
    conn.commit()
    query1 =f"""
    INSERT INTO `task_archive` 
    (`task_id`, `task_name`, `task_assigned_to`, `task_assigned_by`, `task_description`) 
    VALUES ({task_id_db}, "{output[0][1]}", "{output[0][2]}", "{output[0][3]}", "{output[0][5]}");
    """
    cur.execute(query1)
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("index"))