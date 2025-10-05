from flask import Flask, render_template,url_for ,request
from task_handler import task_bp
from fetch_task import fetchAll
app = Flask(__name__)
app.secret_key = "##&&"

@app.route('/')
def index():
    output = fetchAll()
    return render_template('index.html',client_data = output)

@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/handle_login',methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username+password)
    if username=="admin" and password == "admin":
        return render_template('index.html')
    else:
        return render_template('login.html')

app.register_blueprint(task_bp)
if __name__ == "__main__":
    app.run(debug=True,port=8000)