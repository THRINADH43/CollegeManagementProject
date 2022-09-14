import sqlite3
from flask import *

app = Flask(__name__)
app.secret_key = "Thrinadh$$04"  # Need to set the secret key to login


def connect_db():
    sql = sqlite3.connect('identifier.sqlite')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/student/login', methods=["POST"])
def student():
    return "You are in student home page"


@app.route('/teacher/login', methods=["POST"])
def teacher_login():
    return "You are in teacher loginin page"


@app.route('/admin/login', methods=["POST"])
def admin_login():
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        cur = db.execute('select * from admindata where id = ? and password = ?', (username, password,))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            return redirect(f'/admin/logged/{username}')
        else:
            return render_template('admin_login.html')
    return render_template('admin_login.html')


# This allows the Dynamic Routing Possible
@app.route('/admin/logged/<id>',methods=["POST","GET"])
def admin_logged_user(id):
    return "<h2>User Logged in</h2>"

if __name__ == '__main__':
    app.run(debug=True)
