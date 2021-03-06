from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from gh_companion import db, bcrypt
from gh_companion.users.forms import RegistrationForm, LoginForm
from gh_companion.models import User, Character
from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint("users", __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username = form.username.data, password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to login.", "success")
        return redirect(url_for("users.login"))
    return render_template("register.html", title="Register", form=form)

@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next") # access URL parameters
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@users.route("/account")
@login_required
def account():
    image_file = url_for("static", filename=f"profile_pics/{current_user.image_file}")
    user = User.query.filter_by(username=current_user.username).first()
    characters = Character.query.filter_by(user_id = user.id).all()
    return render_template("account.html", title="Account", image_file=image_file, characters=characters) #parameter for template
