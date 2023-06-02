from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,RadioField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo ,Email,ValidationError
from project.models import Student, Instructor

class RegistrationForm(FlaskForm):
    fname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    role = RadioField('Role', choices=[('student', 'Student'), ('instructor', 'Instructor')], validators=[DataRequired()], default='student')

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        student = Student.query.filter_by(username=username.data).first()
        instructor = Instructor.query.filter_by(username=username.data).first()
        if student or instructor:
            raise ValidationError(
                "Username already exists! Please choose a different one"
            )

    def validate_email(self, email):
        student = Student.query.filter_by(email=email.data).first()
        instructor = Instructor.query.filter_by(email=email.data).first()
        if student or instructor:
            raise ValidationError(
                "Email already exists! Please choose a different one"
            )
    

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")