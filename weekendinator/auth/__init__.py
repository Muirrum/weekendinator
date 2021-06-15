import uuid

from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash

import flask_login
from flask_login import current_user

from weekendinator import login_manager, db
from weekendinator.models import Users

from weekendinator.auth import forms

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
   form = forms.LoginForm()

   if form.validate_on_submit():
       user = Users.query.filter_by(username=form.username.data).first()
       if user is not None:
           if check_password_hash(user.password_hash, form.password.data):
               flask_login.login_user(user)
               return "Logged in"
           else:
               flash("Incorrect password")
       else:
            flash("Incorrect username")

   return render_template('auth/login.html', form=form, title="Login")

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegisterForm()

    if form.validate_on_submit():
        id = uuid.uuid4()
        user = Users(
                id=id,
                username=form.username.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data),
                )
        db.session.add(user)
        db.session.commit()
        flask_login.login_user(user)
        return redirect(url_for("meta.home"))

    return render_template("auth/register.html", form=form, title="Register")


@login_manager.user_loader
def user_loader(user_id):
    return Users.query.filter_by(user_id=user_id).first()
