import email
from flask import Blueprint, render_template
from flask_login import login_required, current_user

home = Blueprint("home", __name__)

@home.route("/")
def HomePage():

    return render_template("index.html")

@home.route("/home/<MyAcc>")
def UserHome(MyAcc):
    return render_template("home1.html", email=MyAcc)

