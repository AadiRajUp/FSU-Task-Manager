from flask import Flask, render_template,url_for ,request,session,redirect
from datetime import timedelta
from flask_session import Session
from task_handler import task_bp
from login import login_bp
from fetch_task import fetchAll
from edit import edit_bp
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
    output = fetchAll()
    return render_template('index.html',client_data = output,user_name = session.get("username"))

@app.route('/form')
def form():
    if not session.get("username"):
        return redirect(url_for('auth.login'))
    #session.permanent= True
    return render_template('form.html',user_name=session.get("username"))
@app.route('/login')
def login():
    return render_template('login.html')

app.register_blueprint(task_bp)
app.register_blueprint(login_bp)
app.register_blueprint(edit_bp)

if __name__ == "__main__":
    app.run(debug=True,port=8000)