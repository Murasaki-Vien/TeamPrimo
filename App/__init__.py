from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
db_Name = "database.db"

def createwebsite():
    app.config['SECRET_KEY'] = "TeamPrimo123"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_Name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) 
    
    

    from App.forms.route import forms
    from App.home.route import home

    app.register_blueprint(forms, url_prefix="/")
    app.register_blueprint(home, url_prefix="/")

    from App.models import User, Review, tempUser
    

    login_manager = LoginManager()
    login_manager.login_view = "forms.LoginPage"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    create_database(app)

    return app

def create_database(app):
    if not path.exists('App/' + db_Name):
        db.create_all(app=app)
