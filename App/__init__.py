from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from os import path

db = SQLAlchemy()
mail = Mail()
db_Name = "database.db"

def createwebsite():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = "TeamPrimo123"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_Name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config["SECRET_KEY"] = "LKJVKLXJCHVLIHEURHQP"
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    #app.config['MAIL_DEBUG'] = True
    app.config['MAIL_USERNAME'] = 'GVLang1234@gmail.com'
    app.config['MAIL_PASSWORD'] = 'xoqjnshkhmkeukpd'
    #app.config['MAIL_DEFAULT_SENDER'] = 'GVLang1234@gmail.com'
    #app.config['MAIL_MAX_EMAILS'] = None
    #app.config['MAIL_SUPPRESS_SEND'] = False
    #app.config['MAIL_ASCII_ATTACHMENTS'] = False

    mail.init_app(app)
    db.init_app(app) 

    from App.forms.route import forms
    from App.home.route import home
    from App.dashboard.route import dashboard

    app.register_blueprint(forms, url_prefix="/")
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(dashboard, url_prefix="/")

    from App.models import User, Review, tempUser, CebuPlaces

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
