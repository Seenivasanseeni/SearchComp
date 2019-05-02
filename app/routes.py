from app import app
from flask import render_template
from app.forms import LoginForm

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
	form = LoginForm()
	return render_template("login.html",form=form)


@app.route("/create/company",methods=["GET"])
def create_company():
	return render_template("createCompany.html")

