import mysql.connector
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'none'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://dreamprep"

mysql = SQLAlchemy(app)

class Signup(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    StudentName = mysql.Column(mysql.String(100))
    Email = mysql.Column(mysql.String(100))
    MobileNumber = mysql.Column(mysql.String(15))
    DOB = mysql.Column(mysql.Date)
    Password = mysql.Column(mysql.String(100))
    ConfirmPassword = mysql.Column(mysql.String(100))



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login_page.html")

@app.route('/Signup' ,  methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        student_name = request.form['Sname']
        email = request.form['email']
        mobile_number = request.form['mobile_number']
        dob = request.form['dob']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

@app.route('/dashboard' , methods = ['GET','POST'])
def dashboard():
    if request.method=='GET':
        return render_template("dashboard.html")
    if request.method == 'POST':
        Username = request.form['username']
        session['username'] = Username
        return render_template("dashboard.html", name = Username)
    
@app.route('/submit', methods=['POST'])
def submit():

            # Retrieve the selected checkbox values from the form
            selected_interests = request.form.getlist('interests')
            
            # Join the checkbox values into a comma-separated string to store in the database
            interests_string = ', '.join(selected_interests)


            # Commit the transaction
            mysql.session.commit()

            return "Checkbox data stored successfully!"

@app.route('/Timescheduling/UPSC' , methods = ['POST'])
def Timesheduling():
    if request.method == 'POST':
        Courses = request.form['Courses']
        Time = request.form['Time']
        Username = get_username()

        if Courses == "UPSC" and Time == "4 hour":
            return render_template("/Timescheduling/UPSC/4-hour.html", name = Username)
        elif Courses == "UPSC" and Time == "5 hour":
            return render_template("/Timescheduling/UPSC/5-hour.html", name = Username)
        elif Courses == "UPSC" and Time == "6 hour":
            return render_template("/Timescheduling/UPSC/6-hour.html", name = Username)
        elif Courses == "UPSC" and Time == "7 hour":
            return render_template("/Timescheduling/UPSC/7-hour.html", name = Username)
        elif Courses == "UPSC" and Time == "8 hour":
            return render_template("/Timescheduling/UPSC/8-hour.html", name = Username)

@app.route('/Notes')
def Notes():
    return render_template("/Timescheduling/UPSC/Notes.html")

@app.route('/Youtube_Support')
def Youtube_Support():
    return render_template("/Timescheduling/UPSC/Youtube_Support.html")

@app.route('/Mocktest')
def Mocktest():
    return render_template("/Timescheduling/UPSC/Mocktest.html")

@app.route('/Syllabus')
def Syllabus():
    return render_template("./Syllabus.html")

@app.route('/Criteria')
def Criteria():
    return render_template("/Criteria.html")


if __name__ == '__main__':
    app.run(debug=True)



