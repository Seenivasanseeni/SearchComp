from app import app,db
from flask import render_template, flash, redirect,request, url_for
from app.forms import LoginForm, RegistrationForm, CreateOrganizationForm
from flask_login import current_user, login_user, logout_user,login_required
from app.models import User, Organization

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/home")
@login_required
def home():
	return render_template("home.html",user=current_user)

@app.route("/login",methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		flash("You are logged on as {}".format(current_user.username))
		return redirect(url_for("create_org"))
	
	form = LoginForm()
	if request.method=="GET":
		return render_template('login.html',form=form)

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Incorrect login credentials')
			return redirect(url_for('login'))
		login_user(user)
		flash("You are logged in sucessfully")
		return redirect(url_for('home'))
	return render_template("login.html",form=form)

@app.route("/logout",methods=["GET","POST"])
def logout():
	if not current_user.is_authenticated:
		flash("You are not logged in")
		return redirect(url_for('login'))
	else:
		logout_user()
		flash("You are logged out sucessfully!")
		return redirect(url_for('index'))

@app.route("/create/org",methods=["GET","POST"])
@login_required
def create_org():
	form = CreateOrganizationForm()
	if request.method == "GET":
		return render_template("createCompany.html",user=current_user,form=form)
	if form.validate_on_submit():
		org = Organization(name=form.name.data,website=form.website.data,mission=form.mission.data)
		if org.exists():
			flash("Company with that name already exists")
		else:
			org.save()		
			flash("Organization created for {}".format(org.name))
	return render_template("createCompany.html",user=current_user,form=form)

@app.route("/create/user",methods=["GET","POST"])
def register_user():
	form = RegistrationForm()
	if request.method=="GET":
		return render_template("registration.html",title="Register User",form=form)

	if form.validate_on_submit():
		user = User(username=form.username.data)
		already_present_user = User.query.filter_by(username=user.username).first()
		if not already_present_user is None:
			flash("User with that username exists!")
			return redirect(url_for('register_user'))
		else:
			user.set_password(form.password.data)
			user.save()
			flash("User created successfully. You can login now")
			return redirect(url_for('login'))
	return render_template("registration.html",form=form)