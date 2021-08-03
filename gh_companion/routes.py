from flask import render_template, flash, redirect, url_for
from gh_companion.forms import RegistrationForm, LoginForm
from gh_companion.models import User, Character, Perk
from gh_companion import app

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "Flo" and form.password.data == "123":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)
