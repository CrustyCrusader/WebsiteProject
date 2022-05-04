from flask import Blueprint, redirect, session, url_for,render_template, request, flash

auth = Blueprint('auth',__name__)


@auth.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = user.query.filter_by(name=user).first()

        if found_user:
            session["email"] = found_user.email
        else:
            usr = user(user,"")
    

        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")

@auth.route("/logout")
def logout():
    flash(f"You have logged out","info" )
    session.pop("user",None)
    session.pop("email", None)
    return redirect(url_for("login.html"))

@auth.route('/sign_up')
def sign_up():
    return "<p> Sign Up</p>"

@auth.route("/user", methods = ["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
         
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = user.query.filter_by(name=user).first()
            found_user.email=email
            db.session.commit()
            flash("Email saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email = email )
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

