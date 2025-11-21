from flask import Blueprint,request, render_template
from connect import ARCHIVE_TABLE
from fetch_task import fetchAll

completed_bp = Blueprint("completed",__name__)

@completed_bp.route("/showCompletedTask")
def showCompletedTask():
    task_type = request.args.get('task_type')
    sort_by= request.args.get('sort_by')
    output = fetchAll(task_type,sort_by,ARCHIVE_TABLE)
    return render_template("completed.html",client_data = output)