import sqlite3
from flask import *

students = Blueprint('students',__name__)

@students.route('/student/login', methods=["POST"])
def student():
    return "You are in student home page"
