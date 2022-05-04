from flask import Flask, redirect




def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = "salsa"
   

    from .views import views
    from .auth import auth


    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    return app
    
def __init__(self, name, email):
        self.name = name
        self.email = email
