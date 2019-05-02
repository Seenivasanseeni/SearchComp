from app import app,db
from flask import render_template, flash, redirect,request, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user,login_required
from app.models import User

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		flash("You are logged on as {}".format(current_user.username))
		return redirect(url_for("create_company"))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Incorrect login credentials')
			return redirect(url_for('login'))
		login_user(user)
		flash("You are logged in sucessfully")
		return redirect(url_for('login'))
	return render_template("login.html",form=form)

@app.route("/logout",methods=["GET","POST"])
def logout():
	if not current_user.is_authenticated:
		flash("You are not logged in")
		return redirect(url_for('login'))
	else:
		logout_user()
		flash("You are logged out sucessfully!")
		return redirect(url_for('home'))

@app.route("/create/company",methods=["GET"])
@login_required
def create_company():
	return render_template("createCompany.html")


@app.route("/create/user",methods=["GET","POST"])
def create_user():
	form = LoginForm()
	if request.method=="GET":
		return render_template("login.html",title="Create User",form=form)

	if form.validate_on_submit:
		user = User(username=form.username.data)
		already_present_user = User.query.filter_by(username=user.username).first()
		if not already_present_user is None:
			flash("User with that username exists!")
			return redirect(url_for('create_user'))
		else:
			user.set_password(form.password.data)
			db.session.add(user)
			db.session.commit()
			flash("User created successfully. You can login now")
			return redirect(url_for('login'))
	return render_template("login.html",form=form)