from flask import Flask, url_for,render_template,Blueprint,request,redirect,session
from connect import connectDB,USER_ID_TABLE
from models import UID
import bcrypt

## hey i will change the existing code to make up for the new database system we are using
login_bp = Blueprint("auth",__name__)
@login_bp.route("/login", methods = ["GET","POST"])

# the first login function

def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # get it from the databse
        user = UID.query.filter_by(username=username).first()

        
        # conn= connectDB()
        # cur= conn.cursor()
        # query1 = f"""SELECT * FROM {USER_ID_TABLE}
        # WHERE username = '{username}'
        # """
        # cur.execute(query1)
        # output = cur.fetchall()
        # print(output)
        # print(len(output))
        if not user:
            return render_template('login.html',check_error = True, error_string="Account doesnt exist")
        else:
            session["username"]= username
            session['role'] = user.role
            return redirect(url_for('index'))

