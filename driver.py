from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("home.html")

@app.route("/login",methods=["GET"])
def login():
	return render_template("login.html")

@app.route("/create/company",methods=["GET"])
def create_company():
	return render_template("createCompany.html")