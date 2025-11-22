from flask import Flask, render_template,url_for ,request,session,redirect
from datetime import timedelta
from flask_session import Session
from task_handler import task_bp
from login import login_bp
from fetch_task import fetchAll
from edit import edit_bp
from archive import archive_bp
from completed import completed_bp


app = Flask(__name__)
app.secret_key = "##&&#*#(@&123hello"
app.config["SESSION_PERMANENT"]= True
app.config["SESSION_TYPE"]='filesystem'
app.config["PERMANENT_SESSION_LIFETIME"]= timedelta(seconds=200)

Session(app)


@app.route('/')
def index():
    if not session.get("username"):
        return redirect(url_for('auth.login'))
    #session.permanent=True
    task_type = request.args.get('task_type')
    sort_by= request.args.get('sort_by')
    search_key = request.args.get('search_key')
    output = fetchAll(task_type,sort_by, search_key)
    return render_template('index.html',client_data = output,user_name = session.get("username"))

@app.route('/form')
def form():
    if not session.get("username"):
        return redirect(url_for('auth.login'))
    #session.permanent= True

    # strictly a temporary fix to allow only Aadi and Swoyam to post tasks
    # later will be added to a new table with admins and subadmin capabilities
    print(session.get("role"))
    if  session.get("role")  not in ["Admin"]:
        return "You are not authorized to post a task."
    
    return render_template('form.html',user_name=session.get("username"))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/completed')
def completed():
    return render_template('completed.html')

app.register_blueprint(task_bp)
app.register_blueprint(login_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(archive_bp)
app.register_blueprint(completed_bp)

if __name__ == "__main__":
    app.run(debug=True,port=8000)