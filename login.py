from flask import Flask, url_for,render_template,Blueprint,request,redirect,session
from connect import connectDB,USER_ID_TABLE
import bcrypt
login_bp = Blueprint("auth",__name__)
@login_bp.route("/login", methods = ["GET","POST"])

# the first login function

def login():
    if request.method == "GET":
        # ✅ Show the login form
        return render_template('login.html')
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        conn= connectDB()
        cur= conn.cursor()
        query1 = f"""SELECT * FROM {USER_ID_TABLE}
        WHERE username = '{username}'
        """
        cur.execute(query1)
        output = cur.fetchall()
        print(output)
        print(len(output))
        if len(output) == 0:
            return render_template('login.html',check_error = True, error_string="Account doesnt exist")
        elif len(output) == 1:
            session["username"]= username
            return redirect(url_for('index'))
        else:
            return render_template('login.html',check_error = True, error_string="Major Bug ask the developers")
