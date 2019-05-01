from app import app
from flask import render_template

@app.route("/")
def hello():
	return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
	return render_template("login.html")


@app.route("/create/company",methods=["GET"])
def create_company():
	return render_template("createCompany.html")

