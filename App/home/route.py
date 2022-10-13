from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/")
def HomePage():

    return render_template("index.html")

@home.route("/home/about")
def AboutPage():

    return render_template("about.html")


