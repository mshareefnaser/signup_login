# from flask import Flask, render_template, url_for, flash, redirect
# from project.forms import RegistrationForm, LoginForm
# from flask_sqlalchemy import SQLAlchemy
# #import app
from project import app, db


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
