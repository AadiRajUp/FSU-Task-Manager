from flask import Flask, render_template,url_for ,request,session,redirect
from datetime import timedelta
from flask_session import Session
from task_handler import task_bp
from login import login_bp
from fetch_task import fetchAll
from edit import edit_bp
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from archive import archive_bp

# base class 
class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.secret_key = "##&&#*#(@&123hello"
db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SESSION_PERMANENT"]= True
app.config["SESSION_TYPE"]='filesystem'
app.config["PERMANENT_SESSION_LIFETIME"]= timedelta(seconds=200)
Session(app)
db.init_app(app)


@app.route('/')
def index():
    if not session.get("username"):
        return redirect(url_for('auth.login'))
    #session.permanent=True
    task_type = request.args.get('task_type')
    sort_by= request.args.get('sort_by')
    output = fetchAll(task_type,sort_by)

    return render_template('index.html',client_data = output,user_name = session.get("username"),role=session.get('role'))

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
app.register_blueprint(archive_bp)
if __name__ == "__main__":
    app.run(debug=True,port=8000)