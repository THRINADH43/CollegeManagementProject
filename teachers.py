import sqlite3
from flask import *

teachers = Blueprint('teachers',__name__)



@teachers.route('/teacher/login', methods=["POST"])
def teacher_login():
    return "You are in teacher loginin page"

