from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from App.models import User, tempUser
from flask_mail import  Message
from App import db, mail
import random


forms = Blueprint("forms", __name__)
vCode = random.randint(11111,99999)


@forms.route("/sign-in", methods=['GET', 'POST'])
def SignInPage():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if email != "":
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in Successfully", category='success')
                    login_user(user)
                    return redirect(url_for("dashboard.dashboardPage", MyAcc=email))
                else:
                    flash("Incorrect password", category="error")  
            else:
                flash("Email does not exist.", category='error')  
            

    return render_template("sign-in.html")



@forms.route("/sign-up", methods=['GET', 'POST'])
def SignUpPage():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user = User.query.filter_by(email=email).first()

        if user:
            print("Account already exists")
            flash("Account already exists", category='error')
        elif len(email) < 4:
            print("email must be greater than 3 characters.")
            flash("email must be greater than 3 characters.", category='error')
        elif len(username) < 2:
            print("Firstname must have greater than 2 characters long.")
            flash("Firstname must have greater than 2 characters long.", category='error')
        elif password1 != password2:
            print("Password1 and Password2 Mismatch")
            flash ("Password1 and Password2 Mismatch", category='error')
        elif len(password1) < 7:
            print("Password1 must have greater that 7 characters")
            flash("Password1 must have greater that 7 characters", category='error')
        else:
            number = str(vCode)

            temp_new_user = tempUser(temp_mail=email, temp_userName=username, temp_password=generate_password_hash(password1, method='sha256'))

            print(temp_new_user.temp_mail)

            db.session.add(temp_new_user)                       
            db.session.commit()

            msg = Message("Your Verification Code is: " + number, sender='GVLang1234@gmail.com', recipients=[email])
            mail.send(msg)
            return redirect(url_for("forms.verify", user_id=temp_new_user.id))  
            
    
    return render_template("sign-up.html")


@forms.route("/sign-up/verify/<int:user_id>", methods=[ 'GET', 'POST'])
def verify(user_id):

    if request.method == 'POST':
        value = request.form.get("value")
        val = int(value)
        
        if val == vCode:
            tempuser = tempUser.query.filter_by(id=user_id).first()


            user = User(email=tempuser.temp_mail, userName=tempuser.temp_userName, password=tempuser.temp_password)

            g_email = tempuser.temp_mail

            db.session.add(user)
            db.session.delete(tempuser)
            db.session.commit()
            
            user = User.query.filter_by(email=g_email).first()

            login_user(user)
            flash('Account created', category='success')

            return redirect(url_for("dashboard.dashboardPage", MyAcc=current_user.email))
        else:
            return "<h1>Incorrect</h1>"
            

    return render_template("verification.html", U_Id=user_id)


@forms.route("/logout")
@login_required
def Logout():
    logout_user()
    return redirect(url_for("home.HomePage"))