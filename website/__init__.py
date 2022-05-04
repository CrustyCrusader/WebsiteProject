from flask import Flask, redirect, session, url_for,render_template, request, flash
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = "salsa"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.permanent_session_lifetime = timedelta(minutes=5)



    from .views import views
    from .auth import auth


    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    return app
    
def __init__(self, name, email):
        self.name = name
        self.email = email
