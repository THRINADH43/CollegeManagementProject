
from flask import *
from admin import *
from students import *
from teachers import *


app = Flask(__name__)
app.secret_key = "Thrinadh$$04"  # Need to set the secret key to login
app.register_blueprint(admin)
app.register_blueprint(students)
app.register_blueprint(teachers)



@app.route('/')
def start():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)
