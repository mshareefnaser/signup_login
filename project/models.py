from project import db, login_manager
from datetime import datetime
# usermixin is a class that has some default implementations that are appropriate for most user model classes, 
# including:
# is_authenticated: a property that is True if the user has valid credentials or False otherwise.
# is_active: a property that is True if the user's account is active or False otherwise.
# is_anonymous: a property that is False for regular users, and True for a special, anonymous user.
# get_id(): a method that returns a unique identifier for the user as a string (unicode, if using Python 2).
from flask_login import UserMixin


@login_manager.user_loader
# this function is used to reload the user object from the user ID stored in the session
def load_user(user_id):
    return Student.query.get(int(user_id))

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    # image = db.Column(db.String(20), nullable=False, default="default.jpg")

    def __repr__(self):
        return f"Student('{self.fname}', '{self.lname}', '{self.username}', '{self.email}')"


class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Instructor('{self.fname}', '{self.lname}', '{self.username}', '{self.email}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Course('{self.name}', '{self.description}')"


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(25), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __repr__(self):
        return f"Lesson('{self.title}', '{self.course_id}')"


# class that represents student attendance for each lesson
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    presence_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_present = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Attendance('{self.student_id}', '{self.lesson_id}', '{self.is_present}')"
