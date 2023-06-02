from project.models import Lesson, Course, Attendance, Student, Instructor
from flask import render_template, url_for, flash, redirect
from project.forms import RegistrationForm, LoginForm
from project import app, db, bcrybt
from flask_login import login_user, current_user, logout_user, login_required
from flask import flash

lessons = [
    {
        "title": "Request Library Course",
        "course": "Python",
        "author": "Omar",
        "thumbnail": "thumbnail.jpg",
    },
    {
        "title": "Request Library Course",
        "course": "Python",
        "author": "Omar",
        "thumbnail": "thumbnail.jpg",
    },
    {
        "title": "Request Library Course",
        "course": "Python",
        "author": "Omar",
        "thumbnail": "thumbnail.jpg",
    },
    {
        "title": "Request Library Course",
        "course": "Python",
        "author": "Omar",
        "thumbnail": "thumbnail.jpg",
    },
    {
        "title": "Request Library Course",
        "course": "Python",
        "author": "Omar",
        "thumbnail": "thumbnail.jpg",
    },
    {
        "title": "Request Library Course",
        "course": "Python",
        "author": "Omar",
        "thumbnail": "thumbnail.jpg",
    },
]

courses = [
    {
        "name": "Python",
        "icon": "python.svg",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
    },
    {
        "name": "Data Analysis",
        "icon": "analysis.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
    },
    {
        "name": "Machine Learning",
        "icon": "machine-learning.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
    },
    {
        "name": "Web Design",
        "icon": "web.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
    },
    {
        "name": "Blockchain",
        "icon": "blockchain.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
    },
    {
        "name": "Tips & Tricks",
        "icon": "idea.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", lessons=lessons, courses=courses)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        #hash password, decode to string
        hashed_password = bcrybt.generate_password_hash(form.password.data).decode('utf-8')
        if form.role.data == "student":
            student = Student(
                fname = form.fname.data,
                lname = form.lname.data,
                username=form.username.data,
                email=form.email.data,
                password=hashed_password,
            )
            #add student to db
            db.session.add(student)
            db.session.commit()
        elif form.role.data == "instructor":

            instructor = Instructor(
                fname = form.fname.data,
                lname = form.lname.data,
                username=form.username.data,
                email=form.email.data,
                password=hashed_password,
            )
            #add instructor to db
            db.session.add(instructor)
            db.session.commit()
        
        flash(f"Account created successfully for {form.username.data}", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        #check if user exists
        student = Student.query.filter_by(email=form.email.data).first()
        instructor = Instructor.query.filter_by(email=form.email.data).first()
        #if user exists and password matches
        if student and bcrybt.check_password_hash(student.password, form.password.data):
            #login user is a flask_login function that takes a user object and make session for it 
            # session will be saved because of remember me 
            login_user(student, remember=form.remember.data)
            return redirect(url_for("home"))
        elif instructor and bcrybt.check_password_hash(instructor.password, form.password.data):
            flash("Login Successful", "success")
            login_user(instructor, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
# dummy password
# PASS!!word123