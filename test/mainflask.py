
from flask import Flask, url_for
from flask import render_template
from newmain import file
from coursedata import file2

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('main.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/register.html")
def register():
    return render_template('register.html')

@app.route("/departments.html")
def department():
    return render_template('departments.html')

@app.route("/engineering.html")
def engineering():
    return render_template('engineering.html')

@app.route("/CSE.html")
def CES():
    return render_template('CSE.html')

@app.route("/tutors.html")
def tutors():
    return render_template('tutors.html')

@app.route("/professors.html")
def professors():
    return render_template("professors.html", file = file)

@app.route("/courses.html")
def courses():
    return render_template("courses.html", file2 = file2)

@app.route("/clubs.html")
def clubs():
    return render_template('clubs.html')
if __name__ == "__main__":
    app.run(debug = True)