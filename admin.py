import sqlite3
from flask import *
admin = Blueprint('admin',__name__)


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


@admin.route('/admin/login', methods=["POST"])
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
@admin.route('/admin/logged/<id>', methods=["POST", "GET"])
def admin_logged_user(id):
    if request.method == "POST":
        value = request.form['options']
        if value == 'createstudents':
            return redirect('/admin/createstudents')
        elif value == 'createteachers':
            return redirect('/admin/createteachers')
    return render_template('admin_loggedin.html', id=id)


@admin.route('/admin/createstudents', methods=["GET", "POST"])
def admin_createstudents():
    return "<h2>Creating Students</h2>"


@admin.route('/admin/createteachers', methods=["GET", "POST"])
def admin_createteachers():
    return "<h2>Creating Teachers</h2>"
