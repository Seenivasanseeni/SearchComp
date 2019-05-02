from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')
print("SEC KEY",app.config['SECRET_KEY'])
from app import routes
